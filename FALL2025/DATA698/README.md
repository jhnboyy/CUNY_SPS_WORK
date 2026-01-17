# Urban Tree Presence and Multifamily Residential Building Energy Use in New York City

_This project seeks to examine the relationship between tree presence within specific proximities of specific NYC residential buildings and their impact on energy use rates for those buildings. This project curated a unique data set from mulitple city-level public datasets._

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

Buildings are the largest source of carbon emissions in New York City, primarily due to heating and cooling demands. At the same time, NYC has invested heavily in urban forestry initiatives, with tools such as the NYC Tree Map estimating substantial energy savings from tree canopy coverage. However, those estimates are largely **model-based and generalized**, rather than empirically tied to **measured building energy use**.

This project bridges that gap by:

- Linking **measured, weather-normalized building energy data** (Local Law 84) with  
- **Observed changes in tree canopy coverage** and  
- **Tree counts within defined proximities to building footprints**

The intended audience includes:
- Urban planners and policy analysts  
- Energy and climate researchers  
- Data scientists working with causal inference and spatial data  

The core idea is to move beyond generalized benefit estimates and toward **empirical, building-specific evidence** of how urban trees influence residential energy use in dense, mixed-use cities like NYC.

---

## ✨ Features

- Integration of **multiple NYC Open Data datasets** into a unified analytical dataset  
- Spatial joins using **building footprints** rather than address centroids  
- Construction of a **panel dataset (2010–2017)** at the building (BBL) level  
- Tree proximity analysis using a **50-foot buffer** around building footprints  
- Application of **difference-in-differences (DiD)** methodology for causal inference  
- Extensive **data cleaning, enrichment, and feature engineering**  
- Reproducible analysis via Jupyter notebooks  

---

## 🗂 Project Structure
Explain your directory structure so contributors understand the layout.
## 🗂 Project Structure

DATA698/
│
├── archive/                       # Archived drafts and older materials
│
├── images/                        # Figures and visualizations used in analysis
│
├── raw_data/                      # Raw datasets pulled from NYC Open Data and APIs
│
├── processed_data/                # Cleaned and intermediate datasets
│
├── BuildingWork_Part1.ipynb       # Building energy data ingestion & enrichment
│
├── TreeWork_Part2.ipynb           # Tree inventory & forestry data processing
│
├── Analysis_Part3.ipynb           # Data aggregation, EDA, and DiD modeling
│
├── Urban Tree Presence and Multifamily Residential Building Energy Use in NYC.pdf
│                                   # Final written capstone paper
│
├── Urban Tree Presence and Multifamily Residential Building Energy Use in NYC.docx
│                                   # Editable paper draft
│
└── README.md                      # Project documentation


---

## 📊 Data Sources

| Source Name | Type | URL | Notes |
|------------|------|-----|------|
| NYC Building Energy & Water Disclosure (LL84) | CSV / API | https://data.cityofnewyork.us/Environment/NYC-Building-Energy-and-Water-Data-Disclosure-for-/5zyy-y8am | Weather-normalized EUI used |
| Tree Canopy Change (2010–2017) | GIS / LiDAR | https://data.cityofnewyork.us/Environment/Tree-Canopy-Change-2010-2017-/by9k-vhck | Gain / Loss / No Change |
| Forestry Tree Points | GIS | https://data.cityofnewyork.us/Environment/Forestry-Tree-Points/hn5i-inap | Tree inventory |
| Forestry Work Orders | GIS | https://data.cityofnewyork.us/Environment/Forestry-Work-Orders/bdjm-n7q4 | Used to estimate removals |
| PLUTO / MapPLUTO | GIS / Tabular | https://www.nyc.gov/site/planning/data-maps/open-data.page | Building characteristics |
| Building Footprints | GIS | https://github.com/CityOfNewYork/nyc-geo-metadata | Accurate spatial boundaries |
| NYC Planning Labs Geosearch API | API | https://geosearch.planninglabs.nyc/ | BBL enrichment |
| Google Maps API | API | https://mapsplatform.google.com/ | Address geocoding |
| 2010 Census Tracts | GIS | https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/bmjq-373p | Spatial context |

## 🤝 Contributing

If you''d like others to contribute, add some guidelines here.
Example:

Contributions are welcome! Please fork the repo, make your changes, and submit a pull request.

## 📜 License

Specify a license so others know how they can use your project.
Example:

This project is licensed under the MIT License - see the LICENSE
 file for details.

