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
    orcid: 0000-0000-0000-0000
    corresponding: false
    affiliation: 1
affiliations:
 - name: Griffith University, Australia
   index: 1
date: 06 August 2024
bibliography: paper.bib

---

# Summary

The ```QGIS``` plugin, ‘archaeoModelling’, processes geospatial data and uses a Python implementation of the Maximum Entropy (MaxEnt) algorithm to create predictive models. While designed for archaeological predictive modelling (APM), it has wider application beyond archaeology. By integrating MaxEnt and QGIS, APM will be accessible to anybody able to use Geographic Information System (GIS) software, and hopefully APM becomes commonplace in research and commercial archaeology.  Until recently, APM required the ability to code, propriety software, or convoluted workflows due to unusual data formats, but ‘archaeoModelling’ uses standard data formats and creates GIS-ready and report-ready outputs.  All geospatial inputs are saved as maps, because the process and data leading to a prediction should be explainable and landscape interpretations reproducible.  This plugin lays the foundation for future research into machine learning and landscape archaeology.

# Statement of need

Recently, machine learning (ML) and predictive modelling have become more widespread in archaeology.  MaxEnt is often used for archaeological predictive modelling (Sikk et al., 2022; Rafuse, 2021; Vernon et al., 2022; Galletti et al., 2012), although it was designed for species distribution modelling (@Anderson:2023).  The software package ‘MaxEnt’ is now free-to-use (Phillips et al., 2017), but may be difficult and time consuming to integrate with ML and GIS due to incompatible data types (Phillips, 2017).  Furthermore, the original software is coded in Java and this open-source plugin uses Python, which is more popular, so more users can make changes.

Recent studies have compared MaxEnt to other forms of ML and indicate its suitability for APM and archaeology in general.  MaxEnt can outperform logistic regression (Rafuse, 2021: 2; Vernon et al., 2022) and generalised additive regression (Yaworsky et al., 2020). While Random Forest (Castiello and Tonini, 2021; Yaworsky et al., 2020) has better predictive value than MaxEnt, it can be difficult understand and neural networks even more mysterious (@Wernke:2020).  Although methods used by MaxEnt to arrive at predictions can be unclear (Morales et al., 2017), especially when defaults are accepted, it is easier to explain than some other forms of ML.  Archaeology and/or Cultural Heritage Management (CHM) benefits from transparency, therefore, MaxEnt seems suited to APM.

Often APM falls short of its potential, because it can be difficult to explain how results were arrived at and sometimes interpretations of the landscape are not quantified or illustrated.  The lack of clarity can lead to mistrust, and underuse.  Therefore, a method based on the Analytic Hierarchy Process (Nsanziyera et al. 2018; Mohammed and Sayl 2021; Malaperdas and Zacharias 2019) was developed, and the same process adapted to an area’s elevation and slope.  Reproducibility is important, so quantifying a user’s interpretations of the landscape and outputting them in csv and geotif format was necessary.

# Future releases

ArchaeoModelling only uses environmental co-variates as indicators for archaeological remains; however, other factors may influence site placement.  For example, archaeology that is often project-driven can lead to sampling bias (Boemke et al. 2022), but it is possible to reduce the effects (Barber et al. 2022).  Therefore, future releases of this plugin may incorporate methods to address over and under-sampling.  Importantly, by integrating point-pattern analysis of societal patterns (Sikk et al., 2022; Feinman and Neitzel, 2023), models could be further refined.  For example, settlement location is influenced by environmental factors and possibly by societal patterns, such as fields or mortuary cairns.

# Functionality

The plugin, ‘archaeoModelling’, was built within the QGIS framework (see \autoref{fig:fig2}) using Python and the Qt application, along with the ‘pluginBuilder’ and ‘pluginReloader’ tools. ArchaeoModelling’s Graphical User Interface (GUI) wraps ‘elapid’ [@Anderson:2023], a Python package designed for species distribution modelling using MaxEnt; additionally, archaeoModelling’s geospatial processing was developed specifically for archaeological predictive modelling.  Inputs (see fig. 3) include the ‘activity area’, where an excavation or survey will occur, and the ‘geographic area’, the area geospatial data, such as elevation, refers to.  The activity area can be the same as the geographic area or within its boundaries, but no part can be outside the boundaries.  For simplicity, a landform vector file (polygon or multipolygon) can be used as the geographic area.

When processing, archaeoModelling accesses data’s attribute table, so codes, terminology and any mistakes are the responsibility of the body producing or altering data.  Interpretation of landforms (e.g. soil) can be quantified, giving unique features (e.g. sand or peat) a 1 – 9 weight based on site formation and destruction (Boemke et al., 2022).  The GUI’s default settings rank everything similar to the activity area higher than that which is different, so if an activity area’s slope is 5 – 15 degrees then everywhere in the geographic area with a slope between 5 – 15 degrees will be ranked higher than elsewhere.  However, weights created by default settings can be changed within the GUI.  The results of processing are rasterized, then saved in a nominated directory (fig 1, folder for model). Models are created from all rasters in the directory, limited only by computational power.

Furthermore, geospatial data in raster format can be placed into a folder, bypassing the GUI, so outputs from GIS tools (e.g. viewshed analysis) are usable as inputs.  However, more data may not always make a more accurate prediction.  Geology and/or aspect, for example, may not be relevant to a site type’s location and at some resolutions, factors such as distance to waterway may not alter predictions.  Researchers should consider using their judgement to choose inputs.

This plugin automatically generates maps, including legend and title, in report-ready format (.jpeg) that can be ‘cut-and-paste’ into word-processing documents and GIS-ready maps (.geotif) that can be used with the minimum of effort.  Outputting GIS-ready maps is important because further GIS processing may be needed.  Confidence levels for each model are output in csv files because trust in models with high predictive value may increase if researchers include all levels in reports.  To further increase trust, additional outputs are landform weights and a map of each input.  These outputs may increase trust in the predictions, therefore making APMs more widely used in commercial archaeology.  While MaxEnt predictions are useful, the output from this plugin could form inputs for other types of machine learning and this plugin’s functionality could be extended.

# Acknowledgements

I would like to acknowledge my PhD supervisors, Associate Professor Carney Matheson and Dr Andrea Jalandoni for their input, and Griffith University for funding my work.  This plugin would not have been possible without elapid, begun by Dr Christopher Anderson.

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![archaeoModelling's GUI.\label{fig:fig1}](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/MaxEntGUI.PNG)

Figure sizes can be customized by adding an optional second parameter:
![The QGIS and Python framework used to build archaeoModelling.\label{fig:fig2}](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/QGISdiagram.png)

Figure sizes can be customized by adding an optional second parameter:
![Diagram of data inputs and outputs that archaeoModelling uses.\label{fig:fig3}](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/data_inputsoutputs.png)


# References

Anderson, C. B.  (2023).  Elapid: Species distribution modelling for Python.  Journal of Open Source Software, 8(84), 4930, https://doi.org/10.21105/joss.04930

Barber, R. A., Ball, S. G., Morris, R. K. A., & Gilbert, F. (2022). Target-group backgrounds prove effective at correcting sampling bias in Maxent models. Diversity and Distributions, 28, 128–141. https://doi.org/10.1111/ddi.13442

Boemke, B., Einwögerer, T., Händel, M., & Lehmkuhl, F. (2022). Upper Palaeolithic site probability in Lower Austria - a geoarchaeological multi-factor approach. Journal of Maps, 18(4), 610–618. https://doi.org/10.1080/17445647.2021.2009926

Castiello, M. E., & Tonini, M. (2021). An Explorative Application of Random Forest Algorithm for Archaeological Predictive Modeling. A Swiss Case Study. Journal of Computer Applications in Archaeology, 4(1), 110–125. https://doi.org/10.5334/jcaa.71

Feinman, G. M., & Neitzel, J. E. (2023). The social dynamics of settling down. Journal of Anthropological Archaeology, 69, 101468. https://doi.org/10.1016/j.jaa.2022.101468

Galletti, C. S., Ridder, E., Falconer, S. E., & Fall, P. L. (2013). Maxent modeling of ancient and modern agricultural terraces in the Troodos foothills, Cyprus. Applied Geography (Sevenoaks), 39, 46–56. https://doi.org/10.1016/j.apgeog.2012.11.020

Malaperdas, G., & Zacharias, N. (2019). The habitation Model Trend Calculation (MTC): A new effective tool for predictive modeling in archaeology. Geo-Spatial Information Science, 22(4), 314–331. https://doi.org/10.1080/10095020.2019.1634320

Mohammed, O. A., & Sayl, K. N. (2021). A GIS-Based Multicriteria Decision for Groundwater Potential Zone in the West Desert of Iraq. IOP Conference Series: Earth and Environmental Science, 856(1), 12049. https://doi.org/10.1088/1755-1315/856/1/012049

Nsanziyera, A., Rhinane, H., Oujaa, A., & Mubea, K. (2018). GIS and Remote-Sensing Application in Archaeological Site Mapping in the Awsard Area (Morocco). Geosciences (Basel), 8(6), 207. https://doi.org/10.3390/geosciences8060207

Morales, N. S., Fernández, I. C., & Baca-González, V. (2017). MaxEnt's parameter configuration and small samples: are we paying attention to recommendations? A systematic review. PeerJ (San Francisco, CA), 5, e3093–e3093. https://doi.org/10.7717/peerj.3093

Phillips, Steven J. (2017). A Brief Tutorial on MaxEnt, https://biodiversityinformatics.amnh.org/open_source/maxent/Maxent_tutorial2017.pdf

Phillips, S. J., Anderson, R. P., Dudík, M., Schapire, R. E., & Blair, M. E. (2017). Opening the black box: an open‐source release of Maxent. Ecography (Copenhagen), 40(7), 887–893. https://doi.org/10.1111/ecog.03049

Rafuse, D. J. (2021). A maxent predictive model for hunter-gatherer sites in the southern Pampas, Argentina. Open Quaternary, 7(1). https://doi.org/10.5334/oq.97

Sikk, K., Caruso, G., Rosentau, A., & Kriiska, A. (2022). Comparing contemporaneous hunter-gatherer and early agrarian settlement systems with spatial point process models: Case study of the Estonian Stone Age. Journal of Archaeological Science, Reports, 41, 103330. https://doi.org/10.1016/j.jasrep.2021.103330

Vernon, K. B., Yaworsky, P. M., Spangler, J., Brewer, S., & Codding, B. F. (2022). Decomposing Habitat Suitability Across the Forager to Farmer Transition. Environmental Archaeology : the Journal of Human Palaeoecology, 27(4), 420–433. https://doi.org/10.1080/14614103.2020.1746880

Wernke, S., VanValkenburgh, P., & Saito, A. (2020). Interregional Archaeology in the Age of Big Data: Building Online Collaborative Platforms for Virtual Survey in the Andes. Journal of Field Archaeology, 45(sup1), S61–S74. https://doi.org/10.1080/00934690.2020.1713286

Yaworsky, P. M., Vernon, K. B., Spangler, J. D., Brewer, S. C., & Codding, B. F. (2020). Advancing predictive modeling in archaeology; an evaluation of regression and machine learning methods on the Grand Staircase-Escalante National Monument. PloS One, 2020(10), e0239424. https://doi.org/10.1371/journal.pone.0239424
