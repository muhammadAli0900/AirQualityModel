# Air Quality Dataset Documentation

This document explains the meaning of each column in the dataset, including abbreviations, definitions, and how each variable affects **main_aqi**.

---

## **What is `main_aqi`?**

**main_aqi (Air Quality Index)** is a standardized numerical value that represents how polluted the air is. Higher AQI = worse air quality.

AQI is calculated using major pollutants: **PM2.5, PM10, NO2, SO2, CO, O3**. Weather conditions indirectly affect AQI by influencing how pollutants spread or accumulate.

---

# **Primary Variables (Pollutants — Direct Impact on AQI)**

These compounds are used directly to compute AQI. Higher concentrations usually increase AQI.

### **1. `components_pm2_5` — PM2.5 (Fine Particulate Matter ≤ 2.5 µm)**

* Very small particles from combustion, smoke, industry
* Penetrates deep into lungs
* **Strongest contributor to AQI**

### **2. `components_pm10` — PM10 (Particulate Matter ≤ 10 µm)**

* Larger dust particles from roads, construction
* Raises AQI, especially in dry/dusty conditions

### **3. `components_no` — Nitric Oxide**

* From vehicle exhaust, power plants
* Converts into NO2; indicator of high traffic pollution

### **4. `components_no2` — Nitrogen Dioxide**

* Toxic gas from vehicles and fossil fuels
* Directly used in AQI calculation

### **5. `components_o3` — Ozone (Ground-Level O3)**

* Formed when sunlight reacts with NOx + VOCs
* High on hot, sunny days
* Major contributor to AQI in summer

### **6. `components_so2` — Sulfur Dioxide**

* Emitted from coal burning, industry
* Causes respiratory issues
* Spikes AQI during industrial activity

### **7. `components_co` — Carbon Monoxide**

* Traffic-heavy urban areas
* Reduces oxygen transport; adds to AQI

### **8. `components_nh3` — Ammonia**

* From agriculture, waste, fertilizers
* Combines with other gases to form PM2.5

---

# **Secondary Variables (Meteorological — Indirect Impact on AQI)**

These do not directly increase AQI but influence pollutant formation, dispersion, and settling.

### **9. `temperature_2m` — Temperature (°C)**

* High temperatures increase ozone formation
* Hot days = higher AQI due to O3

### **10. `relative_humidity_2m` — Relative Humidity (%)**

* High humidity increases PM2.5 absorption
* Can worsen AQI during foggy/moist conditions

### **11. `dew_point_2m` — Dew Point**

* Related to moisture
* Higher dew point = more water vapor → PM2.5 clumping

### **12. `precipitation`**

* Rain reduces PM2.5 and PM10
* More rain = **lower AQI**

### **13. `surface_pressure`**

* High pressure = stagnant air = pollutants trapped
* Low pressure = better air dispersion

### **14. `wind_speed_10m` — Wind Speed**

* Higher wind = pollutants dispersed = lower AQI
* Low wind = pollution accumulates

### **15. `wind_direction_10m` — Wind Direction**

* Determines where pollution travels
* Important for understanding sources

### **16. `shortwave_radiation` — Solar Radiation**

* More sunlight = more ozone formation
* Influences daily AQI patterns

---

# **Datetime Feature (Used to Extract Time Patterns)**

### **17. `datetime`**

Not used directly. We extract:

* Hour
* Day
* Weekday
* Month
* Season
* Weekend/weekday behavior

Pollution typically peaks during:

* Morning & evening traffic hours
* Winter (inversion layer)
* Low wind, dry days

---

# Summary Table

| Column               | Meaning           | Category     | Effect on AQI                 |
| -------------------- | ----------------- | ------------ | ----------------------------- |
| main_aqi             | Air Quality Index | Target       | Higher = worse air            |
| components_pm2_5     | Fine particles    | Primary      | Strong positive effect        |
| components_pm10      | Larger particles  | Primary      | Positive effect               |
| components_no        | Nitric oxide      | Primary      | Traffic-related increase      |
| components_no2       | Nitrogen dioxide  | Primary      | Direct AQI contributor        |
| components_o3        | Ozone             | Primary      | Increases on hot days         |
| components_so2       | Sulfur dioxide    | Primary      | Industrial contributor        |
| components_co        | Carbon monoxide   | Primary      | Traffic/combustion            |
| components_nh3       | Ammonia           | Primary      | Converts to PM2.5             |
| temperature_2m       | Temperature       | Secondary    | Higher temp = more ozone      |
| relative_humidity_2m | Humidity          | Secondary    | Higher humidity = more PM2.5  |
| dew_point_2m         | Dew point         | Secondary    | Moisture increases PM levels  |
| precipitation        | Rain              | Secondary    | Rain lowers AQI               |
| surface_pressure     | Air pressure      | Secondary    | High pressure traps pollution |
| wind_speed_10m       | Wind speed        | Secondary    | Higher wind = lower AQI       |
| wind_direction_10m   | Wind direction    | Secondary    | Moves pollutants              |
| shortwave_radiation  | Sunlight          | Secondary    | More sunlight = more ozone    |
| datetime             | Timestamp         | Time Feature | Extract patterns              |
