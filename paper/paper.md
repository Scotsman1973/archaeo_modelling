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

The [QGIS](https://qgis.org/en/site/index.html) plugin, ```archaeoModelling```, processes geospatial data and uses a Python implementation of the Maximum Entropy (MaxEnt) algorithm to create predictive models.  By integrating MaxEnt and ```QGIS```, archaeological predictive modelling (APM) will be accessible to anybody able to use Geographic Information System (GIS) software, and hopefully APM becomes commonplace in research and commercial archaeology.  Until recently, APM required the ability to code, propriety software, or convoluted workflows due to unusual data formats, but ```archaeoModelling``` uses standard data formats and creates GIS-ready and report-ready outputs.  All geospatial inputs are saved as maps, because processes and data leading to a prediction should be explainable and landscape interpretations reproducible.  This plugin lays the foundation for future research into machine learning and landscape archaeology.  While ```archaeoModelling``` was designed for APM, it is easy-to-use and has applications beyond archaeology in fields such as species distribution modelling.

# Statement of need

Recently, machine learning (ML) and predictive modelling have become more widespread in archaeology `[@Bickler:2021; @Phelan:2020]`.  MaxEnt is often used for archaeological predictive modelling `[@Sikk:2022; @Rafuse:2021; @Vernon:2022; @GallettiEtAl:2013]`, although it was designed for species distribution modelling [@Anderson:2023].  The software package [MaxEnt](https://github.com/mrmaxent/Maxent) is now free-to-use [@PhillipsEtAl:2017], but may be difficult and time consuming to integrate with ML and GIS due to incompatible data types [@maxentTute].  Furthermore, the original software is coded in Java and this open-source plugin uses Python, which is more popular, so more users can make changes.

Recent studies have compared MaxEnt to other forms of ML and indicate its suitability for APM and archaeology in general.  MaxEnt can outperform logistic regression `[@Rafuse:2021; @Vernon:2022]` and generalised additive regression [@Yaworsky:2020]. While Random Forest `[@CastielloAndTonini:2021; @Yaworsky:2020]` has better predictive value than MaxEnt, it can be difficult understand and neural networks are even more mysterious [@Wernke:2020].  Although methods used by MaxEnt to arrive at predictions can be unclear [@MoralesEtAl:2017], especially when defaults are accepted, it is easier to explain than some other forms of ML.  Archaeology and/or Cultural Heritage Management (CHM) benefits from transparency, therefore, MaxEnt seems suited to APM.

Often APM falls short of its potential, because it can be difficult to explain how results were arrived at and sometimes interpretations of the landscape are not quantified or illustrated.  The lack of clarity can lead to mistrust and underuse.  Therefore, a method based on the Analytic Hierarchy Process `[@NsanziyeraEtAl:2018; @MohammedAndSayl:2021; @MalaperdasAndNikolaos:2019]` was developed in ```archaeoModelling```, and the same process adapted to an area’s elevation and slope.  Reproducibility is important, so quantifying a user’s interpretations of the landscape and outputting them in .csv and .geotif format was necessary.

# Functionality

```archaeoModelling``` was built within the ```QGIS``` framework (figure 1) using Python and the ```Qt Designer``` application, along with the [Plugin Builder](https://github.com/g-sherman/Qgis-Plugin-Builder) and [PluginReloader](https://github.com/borysiasty/plugin_reloader) tools, and its Graphical User Interface (GUI) wraps ```elapid``` [@Anderson:2023], a Python package designed for species distribution modelling using MaxEnt.  Additionally, the geospatial processing was developed specifically for archaeological predictive modelling.  Inputs include the ‘activity area’, where an excavation or survey will occur, and the ‘geographic area’, the area that geospatial data used to create APMs, such as elevation and landform, refers to (figure 2).  The activity area can be the same as the geographic area or within its boundaries, but no part can be outside the boundaries.  For simplicity, a landform vector file (polygon or multipolygon) can be used as the geographic area.

When processing, ```archaeoModelling``` accesses data’s attribute table (figure 3, Geospatial inputs) so, codes, terminology and any mistakes are the responsibility of the body producing or altering data.  Interpretation of landforms (e.g. soil) can be quantified, users giving unique features (e.g. sand or peat) a 1 – 9 weight based on site formation and destruction [@Boemke:2022].  The GUI’s default settings rank everything similar to the activity area higher than that which is different.  For example, if an activity area’s slope is 5 – 15 degrees then everywhere in the geographic area with a slope between 5 – 15 degrees will be ranked higher than elsewhere.  However, weights created by default settings can be changed within the GUI.  The results of processing are rasterized, then saved in a nominated directory (figure 3, folder for model). Models are created from all rasters in the directory, limited only by computational power.

Furthermore, geospatial data in raster format can be placed into a folder, bypassing the GUI, so outputs from GIS tools (e.g. viewshed analysis) are usable as inputs.  However, more data may not always make a more accurate prediction.  Geology and/or aspect, for example, may not be relevant to a site type’s location and at some resolutions, factors such as distance to waterway may not alter predictions.  Researchers should consider using their judgement when choosing inputs.

This plugin automatically generates maps in report-ready .jpeg format, that include legend and title and can be ‘cut-and-paste’ into word-processing documents and GIS-ready .geotif that can be used with the minimum of effort.  Outputting GIS-ready maps is important because further processing may be needed.  Confidence levels for each model are output in .csv files because trust in models with high predictive value may increase if researchers include all levels in reports.  To further increase trust, additional outputs are landform weights and a map of each input.  These outputs may increase trust in the predictions, therefore making APMs more widely used in commercial archaeology.  While MaxEnt predictions are useful, the output from this plugin could form inputs for other types of machine learning and this plugin’s functionality could be extended.

# Figures

Figure 1: The QGIS and Python framework used to build archaeoModelling.
![Figure 1: The QGIS and Python framework used to build archaeoModelling.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/QGISdiagram.png)

Figure 2: Diagram of data inputs and outputs that archaeoModelling uses.
![Figure 2: Diagram of data inputs and outputs that archaeoModelling uses.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/data_inputsoutputs.png)

Figure 3: archaeoModelling's GUI.
![Figure 3: archaeoModelling's GUI.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/MaxEntGUI.PNG)

# Acknowledgements

I would like to acknowledge my PhD supervisor Associate Professor Carney Matheson for his input and Griffith University for funding my work.  This plugin would not have been possible without [elapid](https://github.com/earth-chris/elapid), begun by Dr Christopher Anderson.

# References

Anderson, C. B.  (2023).  Elapid: Species distribution modelling for Python.  Journal of Open Source Software, 8(84), 4930, https://doi.org/10.21105/joss.04930

Bickler, S. H. (2021). Machine Learning Arrives in Archaeology. Advances in Archaeological Practice, 9(2), 186–191. https://doi.org/10.1017/aap.2021.6

Boemke, B., Einwögerer, T., Händel, M., & Lehmkuhl, F. (2022). Upper Palaeolithic site probability in Lower Austria - a geoarchaeological multi-factor approach. Journal of Maps, 18(4), 610–618. https://doi.org/10.1080/17445647.2021.2009926

Castiello, M. E., & Tonini, M. (2021). An Explorative Application of Random Forest Algorithm for Archaeological Predictive Modeling. A Swiss Case Study. Journal of Computer Applications in Archaeology, 4(1), 110–125. https://doi.org/10.5334/jcaa.71

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
