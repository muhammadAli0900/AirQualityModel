#app.py
import streamlit as st
import pickle
import pandas as pd
import numpy

# Load model and preprocessor
with open("data/models/rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("data/models/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

st.title("Air Quality Index (AQI) Prediction")
# ---------------------------
# User Inputs
# ---------------------------
st.sidebar.header("Input Features")

def user_input_features():
    components_co = st.sidebar.number_input("CO (ppm)", 0.0, 10.0, 0.5)
    components_no = st.sidebar.number_input("NO (ppm)", 0.0, 10.0, 0.5)
    components_no2 = st.sidebar.number_input("NO2 (ppm)", 0.0, 10.0, 0.5)
    components_o3 = st.sidebar.number_input("O3 (ppm)", 0.0, 10.0, 0.5)
    components_so2 = st.sidebar.number_input("SO2 (ppm)", 0.0, 10.0, 0.5)
    components_pm2_5 = st.sidebar.number_input("PM2.5 (µg/m³)", 0.0, 500.0, 50.0)
    components_pm10 = st.sidebar.number_input("PM10 (µg/m³)", 0.0, 500.0, 50.0)
    components_nh3 = st.sidebar.number_input("NH3 (ppm)", 0.0, 10.0, 0.5)
    temperature_2m = st.sidebar.number_input("Temperature (°C)", -20.0, 50.0, 25.0)
    relative_humidity_2m = st.sidebar.number_input("Relative Humidity (%)", 0, 100, 50)
    dew_point_2m = st.sidebar.number_input("Dew Point (°C)", -20.0, 50.0, 10.0)
    precipitation = st.sidebar.number_input("Precipitation (mm)", 0.0, 100.0, 0.0)
    surface_pressure = st.sidebar.number_input("Surface Pressure (hPa)", 900.0, 1100.0, 1013.0)
    wind_speed_10m = st.sidebar.number_input("Wind Speed (m/s)", 0.0, 20.0, 5.0)
    wind_direction_10m = st.sidebar.number_input("Wind Direction (°)", 0, 360, 180)
    shortwave_radiation = st.sidebar.number_input("Shortwave Radiation (W/m²)", 0, 1500, 200)
    # Year stays as number input
    year = st.sidebar.number_input("Year", 2021, 2024, 2023)

    # Month with names
    month = st.sidebar.selectbox(
        "Month",
        options=list(range(1, 13)),
        format_func=lambda x: ["January","February","March","April","May","June",
                           "July","August","September","October","November","December"][x-1],
        index=5
    )
    # Day stays as number input
    day = st.sidebar.number_input("Day", 1, 31, 15)
    # Hour stays as number input
    hour = st.sidebar.number_input("Hour", 0, 23, 12)
    # Day of Week with names
    day_of_week = st.sidebar.selectbox(
        "Day of Week",
        options=list(range(0, 7)),
        format_func=lambda x: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][x],
        index=2
    )
    # Is Weekend stays as number input (0=Weekday,1=Weekend)
    is_weekend = st.sidebar.number_input("Is Weekend (0=Weekday,1=Weekend)", 0, 1, 0)
    # Seasons
    season = st.sidebar.selectbox(
        "Season",
        options=list(range(0, 4)),
        format_func=lambda x: ["Spring","Summer","Autumn","Winter"][x],
        index=1
    )

    data = {
        'components_co': components_co,
        'components_no': components_no,
        'components_no2': components_no2,
        'components_o3': components_o3,
        'components_so2': components_so2,
        'components_pm2_5': components_pm2_5,
        'components_pm10': components_pm10,
        'components_nh3': components_nh3,
        'temperature_2m': temperature_2m,
        'relative_humidity_2m': relative_humidity_2m,
        'dew_point_2m': dew_point_2m,
        'precipitation': precipitation,
        'surface_pressure': surface_pressure,
        'wind_speed_10m': wind_speed_10m,
        'wind_direction_10m': wind_direction_10m,
        'shortwave_radiation': shortwave_radiation,
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'day_of_week': day_of_week,
        'is_weekend': is_weekend,
        'season': season
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# ---------------------------
# Prediction
# ---------------------------
input_scaled = preprocessor.transform(input_df)
prediction = model.predict(input_scaled)

st.subheader("Predicted AQI")
st.write(prediction[0])
