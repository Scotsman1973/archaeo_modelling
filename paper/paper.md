---
title: 'archaeoModelling: a QGIS plugin using the MaxEnt algorithm'
tags:
  - Python
  - GIS
  - QGIS
  - predictive modelling
  - archaeology
authors:
  - name: Andrew Prentice
    orcid: 0009-0001-5964-2652
    corresponding: true
    affiliation: 1
  - name: Andrea Jalandoni
    orcid: 0000-0002-4821-7183
    corresponding: false
    affiliation: 1
affiliations:
 - name: Griffith University, Australia
   index: 1
date: 06 August 2024
bibliography: paper.bib

---

# Summary

The [QGIS](https://qgis.org/en/site/index.html) plugin, ```archaeoModelling```, processes geospatial data and uses a Python implementation of the Maximum Entropy (MaxEnt) algorithm to create archaeological predictive models (APM). By integrating MaxEnt and ```QGIS```, APM will be accessible to Geographic Information System (GIS) users. Building on an open-source platform will facilitate APM becoming a commonplace tool in research and commercial archaeology.  Until recently, APM required the ability to code, propriety software, or convoluted workflows due to unusual data formats, but ```archaeoModelling``` uses standard data formats and creates GIS-ready and report-ready outputs.  All geospatial inputs are saved as maps, because the process and data leading to a prediction should be explainable and landscape interpretations reproducible. This plugin lays the foundation for future research into machine learning and landscape archaeology. While designed for APM, it has wider application beyond archaeology, such as species destribution modelling.

# Statement of need

Recently, machine learning (ML) and predictive modelling have become more widespread in archaeology [@Bickler:2021; @Phelan:2020].  MaxEnt is often used for archaeological predictive modelling [@Sikk:2022; @Rafuse:2021; @Vernon:2022; @GallettiEtAl:2013], although it was designed for species distribution modelling [@Anderson:2023].  The software package [MaxEnt](https://github.com/mrmaxent/Maxent) is now free-to-use [@PhillipsEtAl:2017], but may be difficult and time consuming to integrate with ML and GIS due to incompatible data types [@maxentTute].  Furthermore, the original software is coded in Java and this open-source plugin uses Python, which is more popular, so more users can make changes.

Recent studies have compared MaxEnt to other forms of ML and indicate its suitability for APM and archaeology in general.  MaxEnt can outperform logistic regression [@Rafuse:2021; @Vernon:2022] and generalised additive regression [@Yaworsky:2020]. While Random Forest [@CastielloAndTonini:2021; @Yaworsky:2020] has better predictive value than MaxEnt, it can be difficult understand and neural networks are even more mysterious [@Wernke:2020].  Although methods used by MaxEnt to arrive at predictions can be unclear [@MoralesEtAl:2017], especially when defaults are accepted, it is easier to explain than some other forms of ML.  Archaeology and/or Cultural Heritage Management (CHM) benefits from transparency, therefore, MaxEnt seems suited to APM.

Often APM falls short of its potential, because it can be difficult to explain how results were arrived at and sometimes interpretations of the landscape are not quantified or illustrated.  The lack of clarity can lead to mistrust and underuse.  Therefore, a method based on the Analytic Hierarchy Process [@NsanziyeraEtAl:2018; @MohammedAndSayl:2021; @MalaperdasAndNikolaos:2019] was developed in ```archaeoModelling```, and the same process adapted to an area’s elevation and slope.  Reproducibility is important, so quantifying a user’s interpretations of the landscape and outputting them in .csv and .geotif format was necessary.

# Functionality

```archaeoModelling``` was built within the ```QGIS``` framework (figure 1) using Python and the ```Qt Designer``` application, along with the [Plugin Builder](https://github.com/g-sherman/Qgis-Plugin-Builder) and [PluginReloader](https://github.com/borysiasty/plugin_reloader) tools, and its Graphical User Interface (GUI) wraps ```elapid``` [@Anderson:2023], a Python package designed for species distribution modelling using MaxEnt.  Additionally, the geospatial processing was developed specifically for archaeological predictive modelling.  Inputs include the ‘activity area’, where an excavation or survey will occur, and the ‘geographic area’, the area that geospatial data, such as elevation and landform, refers to (figure 2).  The activity area can be the same as the geographic area or within its boundaries, but no part can be outside the boundaries.  For simplicity, a landform vector file (polygon or multipolygon) can be used as the geographic area.

When processing, ```archaeoModelling``` accesses data’s attribute table (figure 3, Geospatial inputs), so, codes, terminology and any mistakes are the responsibility of the body producing or altering data.  Interpretation of landforms (e.g. soil) can be quantified, users giving unique features (e.g. sand or peat) a 1 – 9 weight based on site formation and destruction [@Boemke:2022].  The GUI’s default settings rank everything similar to the activity area higher than that which is different.  For example, if an activity area’s slope is 5 – 15 degrees then everywhere in the geographic area with a slope between 5 – 15 degrees will be ranked higher than elsewhere.  However, weights created by default settings can be changed within the GUI.  The results of processing are rasterized, then saved in a nominated directory (figure 3, folder for model). Models are created from all rasters in the directory, limited only by computational power.

Furthermore, geospatial data in raster format can be placed into a folder, bypassing the GUI, so outputs from GIS tools (e.g. viewshed analysis) are usable as inputs.  However, more data may not always make a more accurate prediction.  Geology and/or aspect, for example, may not be relevant to a site type’s location and at some resolutions, factors such as distance to waterway may not alter predictions.  Researchers should consider using their judgement when choosing inputs.

This plugin automatically generates maps in report-ready .jpeg format, that include legend and title and can be ‘cut-and-paste’ into word-processing documents and GIS-ready .geotif that can be used with the minimum of effort.  Outputting GIS-ready maps is important because further processing may be needed.  Confidence levels for each model are output in .csv files because trust in models with high predictive value may increase if researchers include all levels in reports.  To further increase trust, additional outputs are landform weights and a map of each input.  These outputs may increase trust in the predictions, therefore making APMs more widely used in commercial archaeology.  While MaxEnt predictions are useful, the output from this plugin could form inputs for other types of machine learning and this plugin’s functionality could be extended.

# Acknowledgements

I would like to acknowledge my PhD supervisor Associate Professor Carney Matheson for his input and Griffith University for funding my work.  This plugin would not have been possible without [elapid](https://github.com/earth-chris/elapid), begun by Dr Christopher Anderson.

# Figures

![Figure 1: The QGIS and Python framework used to build archaeoModelling.](images/QGISdiagram.png)

![Figure 2: Diagram of data inputs and outputs that archaeoModelling uses.](images/data_inputsoutputs.png)

![Figure 3: archaeoModelling's GUI.](images/GUI.jpg)

# References

