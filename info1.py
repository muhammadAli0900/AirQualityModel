import pandas as pd

# Load dataset
file_path = r"C:\Users\HT COMPUTERS\Desktop\Air_Quality_model\data\cleaned\concatenated_testing_cleaned.csv"
df = pd.read_csv(file_path)

# Basic dataset info
print("=== Dataset Info ===")
print(df.info())
print("\n=== First 5 rows ===")
print(df.head())

# AQI statistics
print("\n=== AQI Statistics ===")
print("Min AQI:", df['main_aqi'].min())
print("Max AQI:", df['main_aqi'].max())
print("Average AQI:", df['main_aqi'].mean())

# Pollutants statistics
pollutants = ['components_pm2_5', 'components_pm10', 'components_no', 
              'components_no2', 'components_o3', 'components_so2', 'components_co', 'components_nh3']
print("\n=== Pollutants Statistics ===")
print(df[pollutants].describe())

# Weather statistics
weather = ['temperature_2m', 'relative_humidity_2m', 'dew_point_2m', 
           'precipitation', 'surface_pressure', 'wind_speed_10m', 'shortwave_radiation']
print("\n=== Weather Statistics ===")
print(df[weather].describe())

# Seasonal AQI (if 'season' exists)
if 'season' in df.columns:
    print("\n=== Average AQI by Season ===")
    season_map = {0:'Spring',1:'Summer',2:'Autumn',3:'Winter'}
    print(df.groupby('season')['main_aqi'].mean().rename(index=season_map))
