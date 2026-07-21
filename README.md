# Air Quality Prediction — Pakistan

A machine learning project that predicts the Air Quality Index (AQI) for major Pakistani cities using real pollution and weather data collected from 2021 to 2024.

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Scikit-learn](https://img.shields.io/badge/Model-Random%20Forest-orange) ![Streamlit](https://img.shields.io/badge/App-Streamlit-red)

---

## Why this project

Air quality data for Pakistani cities exists but has rarely been put to use in predictive modeling. Most AQI research is built on datasets from the US or China. This project focuses on five Pakistani cities (Islamabad, Karachi, Lahore, Peshawar, and Quetta) to build something that reflects the air quality reality of where we actually live.
---

## Overview

| | |
|---|---|
| **Target variable** | `main_aqi` — Air Quality Index |
| **Cities covered** | Islamabad, Karachi, Lahore, Peshawar, Quetta |
| **Data range** | August 2021 – December 2024 |
| **Best model** | Random Forest Regressor |
| **R²** | 0.9992 |
| **RMSE** | 0.0303 |
| **MAE** | 0.0024 |

---

## Dataset

**Source:** [Pakistan Air Quality & Pollutant Concentrations — Kaggle](https://www.kaggle.com/datasets/hajramohsin/pakistan-air-quality-pollutant-concentrations)

Features fall into three groups:

- **Pollutants** (direct AQI drivers): PM2.5, PM10, NO, NO2, O3, SO2, CO, NH3
- **Weather** (indirect factors): temperature, humidity, dew point, precipitation, wind speed/direction, solar radiation, surface pressure
- **Time features** extracted from datetime: hour, day, weekday, month, season

Full column definitions are in [`/DATA_DICTIONARY.md`](/DATA_DICTIONARY.md).

---

## What we found in EDA

- PM2.5 and PM10 are by far the strongest predictors of AQI
- AQI is consistently worse in winter — temperature inversions trap pollutants near the surface
- Rain has a clear and immediate effect on bringing AQI down
- Ozone (O3) peaks in summer on high-radiation days
- Weekday mornings and evenings show traffic-driven spikes

---

## Model Results

We trained two models and compared them on a held-out test set (Jul–Dec 2024, unseen during training):

| Model | R² | RMSE | MAE |
|---|---|---|---|
| Linear Regression | 0.4536 | 0.8024 | 0.6616 |
| **Random Forest** | **0.9992** | **0.0303** | **0.0024** |

Random Forest performed significantly better, handling the non-linear relationships between weather, pollutants, and AQI that linear regression couldn't capture.

---

## Streamlit App

A simple web app where you enter pollutant and weather values and get an instant AQI prediction with visualizations.

```bash
pip install -r requirements.txt
streamlit run app.py
```

> Live deployment :[https://air-quality-model.streamlit.app/].

---

## Project Structure

```
AirQualityModel/
├── app.py                        # Streamlit web app
├── data/
│   ├── cleaned/                  # Preprocessed train/test CSVs
│   └── models/
│       ├── rf_model.pkl          # Trained Random Forest
│       └── preprocessor.pkl      # Fitted StandardScaler pipeline
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 04_modelTraining.ipynb
├── docs/
│   └── DATA_DICTIONARY.md
└── requirements.txt
```

---

## Future plans

- Integrate live sensor or API data for real-time predictions
- Add multi-day AQI forecasting
- City-wise comparison dashboard

---

**Muhammad Ali** — BS Software Engineering, Sukkur IBA University  
[GitHub](https://github.com/muhammadAli0900)
