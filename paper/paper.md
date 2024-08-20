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



# Functionality


# Figures

![Figure 1: The QGIS and Python framework used to build archaeoModelling.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/QGISdiagram.png)

![Figure 2: Diagram of data inputs and outputs that archaeoModelling uses.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/data_inputsoutputs.png)

![Figure 3: archaeoModelling's GUI.](https://github.com/Scotsman1973/archaeo_modelling/blob/main/images/MaxEntGUI.PNG)

# Acknowledgements

I would like to acknowledge my PhD supervisor Associate Professor Carney Matheson for his input and Griffith University for funding my work.  This plugin would not have been possible without [elapid](https://github.com/earth-chris/elapid), begun by Dr Christopher Anderson.

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
