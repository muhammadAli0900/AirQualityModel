# Raw Data Directory

This folder contains the **original, unmodified dataset** used for the AirQualityProject — sourced from the Kaggle dataset *“Pakistan Air Quality & Weather Data (2021–2024)”*.

### 📁 Folder Structure
raw/
│
├── training/
│ ├── islamabad.csv
│ ├── lahore.csv
│ ├── karachi.csv
│ ├── peshawar.csv
│ ├── quetta.csv
│ └── combined_training.csv
│
└── testing/
├── islamabad_test.csv
├── lahore_test.csv
├── karachi_test.csv
├── peshawar_test.csv
├── quetta_test.csv
└── combined_testing.csv (optional)

### 📝 Description
- **training folder** contains hourly pollutant + weather data for 5 major cities.
- **testing folder** contains separate files for each city used for validation.
- **combined_training.csv** is a concatenation of all training city files for unified modeling.
- **combined_testing.csv** (optional) is a merged version of all test datasets.

### 🔗 Dataset Source
Pakistan Air Quality & Weather Data (2021–2024)  
Kaggle Link:  
https://www.kaggle.com/datasets/hajramohsin/pakistan-air-quality-pollutant-concentrations

### ⚠️ Note
- These files are **raw and unchanged**.  
- Any preprocessing should be done in `data/processed/`.  
- Do not manually edit or modify raw data files.