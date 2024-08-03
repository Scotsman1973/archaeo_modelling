## -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import os # library used to manipulate path names and directories
import glob # allows for all files in a certain directory to be targeted
import fnmatch
import shutil # facilitates file removal, including files open in applications other than python

from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsFeatureRequest,
                       QgsProcessingException,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFolderDestination,
                       QgsProcessingParameterField,
                       QgsProcessingParameterString,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterCrs,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterRasterDestination,
                       )
                       
from qgis.core import (QgsFeature, QgsField, QgsFields,
                       QgsGeometry, QgsPoint, QgsVectorFileWriter, QgsProject, 
                       QgsVectorLayer, QgsProcessingFeedback, QgsWkbTypes, QgsFeature, QgsGeometry, QgsPointXY, 
                       QgsProcessingFeatureSource, QgsRasterLayer, QgsMarkerSymbol, QgsProcessingUtils, QgsMapLayer)
                       
from qgis.utils import iface
                       
import processing


class csv_to_map(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    CSV_FILE = 'CSV_FILE'
    BASE_MAP = 'BASE_MAP'
    SEARCH_FIELD = 'SEARCH_FIELD'
    SEARCH_TERM = 'SEARCH_TERM'
    X_FIELD = 'X_FIELD'
    Y_FIELD = 'Y_FIELD'
    #INPUT = 'INPUT'
    CALC_OUTPUT = 'CALC_OUTPUT'
    OUTPUT = 'OUTPUT'
    OUTPUT4 = 'OUTPUT4'
    OUTPUT5 = 'OUTPUT5'
    OUTPUT6 = 'OUTPUT6'
    NEW_CRS = 'NEW_CRS'
    DEST_FOLDER = 'DEST_FOLDER'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Extract the layers within a csv file and create map', string)

    def createInstance(self):
        return csv_to_map()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'csvtomap'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Input table of points and divide by custom search terms')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Example scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'examplescripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This processing function divides a table of data by search terms provided by the user.  The user first chooses the x and y fields, the table's crs.  "
        "If the user wants the data reprojected then the target crs should be entered, if the user does not want the data reprojected then the target crs needs to be set to the same crs as the original crs.  "
        "The field headings must be formatted so that they only contain letters (a - z) upper or lower case and underscores.  "
        "The function works with the following file extentions: .csv, .dbf, .xls, .xlsx but does not work with .ods (open document spreadsheet).  "
        "The search terms must be seperated by a single comma.  Whitespaces are removed automatically from the beginning and end of the search terms.  Search terms must be an exact match.")
    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.BASE_MAP,
                self.tr('base map'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.CSV_FILE,
                self.tr('csv file'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterField(
                self.X_FIELD,
                'Choose X Field',
                '',
                self.CSV_FILE))
                
        self.addParameter(
            QgsProcessingParameterField(
                self.Y_FIELD,
                'Choose Y Field',
                '',
                self.CSV_FILE))
         
        self.addParameter(
            QgsProcessingParameterCrs(
                self.NEW_CRS,
                'Choose target coordinate reference system',
                '',
                False,))
        
        self.addParameter(
            QgsProcessingParameterField(
                self.SEARCH_FIELD,
                'Choose Search Field',
                '',
                self.CSV_FILE))
                
        self.addParameter(
            QgsProcessingParameterString(
                self.SEARCH_TERM,
                self.tr('Input search terms, seperated by a comma')
            )
        )
        
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        # Each sink only seems to be able to hold one type of geometry
        # A dictionary of outputs can be created at the end though 
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Vector from csv'),
                type = QgsProcessing.TypeVectorPoint
            )
        )
       
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT4,
                self.tr('Reprojected base map'),
                type = QgsProcessing.TypeVectorAnyGeometry
            )
        )
        
        
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT5,
                # leaving off the self.tr stops the output overwriting layer names
                # otherwise all layer names are whatever is in self.tr
                type = QgsProcessing.TypeVectorPoint
            )
        )
        
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT6,
                # leaving off the self.tr stops the output overwriting layer names
                # otherwise all layer names are whatever is in self.tr
                type = QgsProcessing.TypeVectorPoint
            )
        )
        
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.DEST_FOLDER,
                self.tr('Destination folder')
            )
        )
        
    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        
        base_map = self.parameterAsVectorLayer(
            parameters,
            self.BASE_MAP,
            context
        )
    
        csv_source = self.parameterAsSource(#must be as source not as vector layer
            parameters,
            self.CSV_FILE,
            context
        )
        
        feedback = QgsProcessingFeedback()
        
        results_folder = "C:/Mythings/PhD/results/*"
        
        project = QgsProject.instance()

        layer_colours = [ '#1f78b4', '#a6cee3', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', 
        '#00fffb', '#f7ff00', '#ff00d9', '#4000ff', '#ff0c00', '#713a48', '#71ee48', '#cdee48', '#ee48c2', '#ee4803', 
        '#e3bbee', '#3a7141', '#82a11c', '#82a1f1', '#f19e82', '#0928f1', '#c44f6a', '#4fc461', '#08160a', '#b430c2', 
        '#9bc230', '#ff9a3c']

        layer_shapes = [ 'circle', 'square', 'triangle', 'diamond', 'circle', 'square', 'triangle', 'diamond', 'circle', 
        'square', 'triangle', 'diamond', 'circle', 'square', 'triangle', 'diamond', 'circle', 'square', 'triangle', 'diamond', 
        'circle', 'square', 'triangle', 'diamond', 'circle', 'square', 'triangle', 'diamond', 'circle', 'square']

        # this empties the directory geoprogramming, just for housekeeping
        files = glob.glob(results_folder)
        for f in files:
            
            # using sutil.rmtree rather than os.remove allows the removal, or ignoring, of files in other applications
            shutil.rmtree(f, ignore_errors = 'True')
        
        ###################################################
        # this is where the base map is added, target projection, if it is a line type vector file
        #############################################################################################
        
        new_crs = self.parameterAsCrs(parameters, self.NEW_CRS, context)

        reproj_base_map = processing.run('native:reprojectlayer', {
        'INPUT': base_map,
        'TARGET_CRS': new_crs,
        'OUTPUT': 'memory:'
        },
        context=context, feedback=feedback)['OUTPUT']
            
        (sink, dest_id4) = self.parameterAsSink(parameters, self.OUTPUT4, context,
                                               reproj_base_map.fields(), reproj_base_map.wkbType(), reproj_base_map.sourceCrs())
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT4))
            
        request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry)
        total = 100.0 / base_map.featureCount() if base_map.featureCount() else 0
        features = base_map.getFeatures()

        for current, feature in enumerate (features):
            if feedback.isCanceled():
                break

            feedback.setProgress(int(current * total))
            sink.addFeature(feature)
            
        del sink
        
        #######################################
        # this bit of script takes a table in csv format and creates a vector point layer
        # it uses the crs that is the user nominated target CRS
        ################################################################
        
        if csv_source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.CSV_FILE))

        fields = csv_source.fields()
        x_field_index = fields.lookupField(self.parameterAsString(parameters, self.X_FIELD, context))
        y_field_index = fields.lookupField(self.parameterAsString(parameters, self.Y_FIELD, context))

        wkb_type = QgsWkbTypes.Point

        (sink, dest_id1) = self.parameterAsSink(parameters, self.OUTPUT, context,
                                               fields, wkb_type, new_crs)
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry)
        features = csv_source.getFeatures(QgsFeatureRequest(), QgsProcessingFeatureSource.FlagSkipGeometryValidityChecks)
        total = 100.0 / csv_source.featureCount() if csv_source.featureCount() else 0

        for current, feature in enumerate(features):
            if feedback.isCanceled():
                break

            feedback.setProgress(int(current * total))
            attrs = feature.attributes()

            try:
                x = float(attrs[x_field_index])
                y = float(attrs[y_field_index])
                point = QgsPoint(x, y)
                feature.setGeometry(QgsGeometry(point))
            except:
                pass  # no geometry

            sink.addFeature(feature)
            
        del sink
        
        # this creates the results dictionary and starts to populate it but doesn't yet return it
        results = {}
        results[self.OUTPUT4] = dest_id4
        
        search_field = self.parameterAsString(parameters, self.SEARCH_FIELD, context)
        search_input = self.parameterAsString(parameters, self.SEARCH_TERM, context)
        destination_path = self.parameterAsString(parameters, self.DEST_FOLDER, context)

        search_terms = search_input.split(',', )
        extracted_layers_list = []
        for index, search_term in enumerate (search_terms):
            
            search_term_clean = search_term.strip()
            
            # the LIKE operator acts like the word contains, the % signs are wildcards so allow the term to appear anywhere
            # by using formatting a variable can be used as the search term
            expression = "{search__field} LIKE \'%{search_term}%\'".format(search__field = search_field, search_term = search_term_clean)
            site_type = "'{search_term}\'".format(search_term = search_term_clean)#this needs string formating to place a variable within a string
            extracted_layer = processing.run("native:extractbyexpression", {'INPUT': dest_id1, 'EXPRESSION': expression, 'OUTPUT':'memory:'}, context=context, feedback=feedback)['OUTPUT']
            calc_output = processing.run("qgis:fieldcalculator", {
            'INPUT': extracted_layer,
            'FIELD_NAME': 'SITE_TYPE',
            'FIELD_TYPE': 2, #0 is float type, 2 is string
            'FIELD_LENGTH': 25,
            'FIELD_PRECISION': 2,
            'FORMULA': site_type,  
            'OUTPUT': 'memory:'
            },
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
            extracted_layer = context.getMapLayer(calc_output)#convert from mapLayer back to vector
            #if there is any information in the selection, create and saves as shapefile
            if (len(extracted_layer) > 0):
                #save the shapefile
                file_name = '{dest_path}/{search_term}.shp'.format( dest_path= destination_path, search_term = search_term_clean)
                writer = QgsVectorFileWriter.writeAsVectorFormat(extracted_layer, file_name, 'utf-8', driverName = 'ESRI Shapefile')
                
                del(writer)
                #this routine adds each layer with features to an output sink, which works
                (sink, dest_id5) = self.parameterAsSink(parameters, self.OUTPUT5, context,
                                                       extracted_layer.fields(), wkb_type, new_crs)
                                                       
                extracted_layer.setName(search_term_clean)
                
                if sink is None:
                    raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT5))
                    
                request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry)
                features = extracted_layer.getFeatures()
                for feature in features:
                    if feedback.isCanceled():
                        break
                    sink.addFeature(feature)
                
                extracted_layer = QgsProcessingUtils.mapLayerFromString(dest_id5, context)
                # these two lines take the symbol and colour at the relevant spot and applies it to the layer
                symbol = QgsMarkerSymbol.createSimple({'name': layer_shapes[index], 'color': layer_colours[index]})
                extracted_layer.renderer().setSymbol(symbol)
                extracted_layer.triggerRepaint()# make the change actual for the layer
                extracted_layer.setName(search_term_clean)#must be here otherwise outputs aren't named
                extracted_layers_list.append(extracted_layer.name())
                del sink
        
        # this syntax continues to create the results dictionary with the result from the loop then returns it
        results[self.OUTPUT5] = dest_id5
        return results

        
