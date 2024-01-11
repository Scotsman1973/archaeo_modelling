<p align="center">
  <img src="https://earth-chris.github.io/elapid/img/elapid-logo.png" alt="elapid logo"/>
</p>

<p align="center">
  <em>QGIS plugin utilizing Maxent for predictive modelling.</em>
</p>

---

**Documentation**: [earth-chris.github.io/elapid](https://earth-chris.github.io/elapid)

**Source code**: [earth-chris/elapid](https://github.com/earth-chris/elapid)

---

## Introduction

This documentation is not designed to be an introduction to QGIS; it gives workflows specific to this plugin.  If you need common operations there is a QGIS resource section.

---

## QGIS resources

GIS, QGIS or ArcGIS, a package of geospatial functions, the same functions are available, using the same data types; if you are used to ArcGIS or think its 'industry standard', don't worry.  Read these resources and you'll be fine, or the easiest option is google.


The `conda` install is recommended for Windows users. While there is a `pip` distribution, you may experience some challenges. The easiest way to overcome them is to use [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/about). Otherwise, see [this page](https://elapid.org/install) for support.

---

**Why use elapid?**

The amount and quality of bioegeographic data has increased dramatically over the past decade, as have cloud-based tools for working with it. `elapid` was designed to provide a set of modern, python-based tools for working with species occurrence records and environmental covariates to map different dimensions of a species' niche.

`elapid` supports working with modern geospatial data formats and uses contemporary approaches to training statistical models. It uses `sklearn` conventions to fit and apply models, `rasterio` to handle raster operations, `geopandas` for vector operations, and processes data under the hood with `numpy`.

This makes it easier to do things like fit/apply models to multi-temporal and multi-scale data, fit geographically-weighted models, create ensembles, precisely define background point distributions, and summarize model predictions.

It does the following things reasonably well:

**Data types**

Select random geographic point samples (aka background or pseudoabsence points) within polygons or rasters, handling `nodata` locations, as well as sampling from bias maps (using `elapid.sample_raster()`, `elapid.sample_vector()`, or `elapid.sample_bias_file()`).

**Merging rasters**

Transform covariate data into derivative `features` to expand data dimensionality and improve prediction accuracy (like `elapid.ProductTransformer()`, `elapid.HingeTransformer()`, or the all-in-one `elapid.MaxentFeatureTransformer()`).

**aspect data**

Train and apply species distribution models based on annotated point data, configured with sensible defaults (like `elapid.MaxentModel()` and `elapid.NicheEnvelopeModel()`).

**slope data**

Compute spatially-explicit sample weights, checkerboard train/test splits, or geographically-clustered cross-validation splits to reduce spatial autocorellation effects (with `elapid.distance_weights()`, `elapid.checkerboard_split()` and `elapid.GeographicKFold()`).

**elevation data**

Apply any pixel-based model with a `.predict()` method to raster data to easily create prediction probability maps (like training a `RandomForestClassifier()` and applying with `elapid.apply_model_to_rasters()`).

**huge file size**

Work with cloud- or web-hosted raster/vector data (on `https://`, `gs://`, `s3://`, etc.) to keep your disk free of temporary files.

Check out some example code snippets and workflows on the [Working with Geospatial Data](https://elapid.org/examples/WorkingWithGeospatialData/) page.

---

:snake: `elapid` requires some effort on the user's part to draw samples and extract covariate data. This is by design.

Selecting background samples, computing sample weights, splitting train/test data, and specifying training parameters are all critical modeling choices that have profound effects on inference and interpretation.

The extra flexibility provided by `elapid` enables more control over the seemingly black-box approach of Maxent, enabling users to better tune and evaluate their models.

---

## Citation

Cite by including this URL: https://github.com/Scotsman1973/archaeo_modelling

---

## Plugin created by [Andrew Prentice](https://digitalarchaeology.com.au)
