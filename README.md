# Bike Sharing Data Analysis and Visualization

## Overview

This project aims to **analyze bike sharing usage patterns** using the Bike Sharing Dataset to answer key **business questions** related to rental trends, weather conditions, and working day behavior. The analysis is conducted through **Exploratory Data Analysis (EDA)** and **data visualization**, and the results are presented in an **interactive dashboard deployed using Streamlit**.

---

## Business Questions

This analysis focuses on answering the following questions:

1. How does the bike rental trend behave throughout the year 2011?
2. How do bike rentals vary across different weather conditions (*weathersit*)?
3. How do bike rental volumes compare between working days and non-working days?

---

## Dataset

The dataset used in this project is the **Bike Sharing Dataset**, which contains information on bike rentals based on time, weather, and user categories.

The dataset directory includes:

* `day.csv` – Daily aggregated bike rental data
* `hour.csv` – Hourly aggregated bike rental data

In this analysis, **only the `day.csv` dataset is used**, as daily data provides a broader view of rental trends without focusing on hourly fluctuations.

---

## Analysis Workflow

The project follows these steps:

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Visualization
5. Insight and Business Interpretation
6. Dashboard Deployment using Streamlit

---

## Key Findings

### 1. Bike Rental Trend in 2011

* Bike rentals show a **gradual increase** from January to mid-year (July–August).
* Rental volume peaks around **June–July**, with several days exceeding **6,000 rentals**.
* After August, rentals **decline steadily**, with a sharper decrease toward the end of the year (November–December).

**Conclusion:**
Bike rentals tend to increase during spring and summer, peak in mid-year, and decline during autumn and winter. To mitigate seasonal drops, **promotional campaigns or discounts during winter** could help maintain user engagement.

---

### 2. Bike Rentals by Weather Condition

* **Clear weather** records the highest average rentals, close to **5,000 rentals per day**.
* **Cloudy weather** shows slightly lower rentals, around **4,000 per day**, but still maintains strong usage.
* **Rainy weather** has the lowest rental volume, below **2,500 per day**, with higher variability.

**Conclusion:**
Weather has a significant impact on bike rentals. **Incentives or promotions during rainy days** may help encourage usage despite unfavorable conditions.

---

### 3. Working Day vs Non-Working Day Comparison

* **Non-working days** have higher rental volumes than working days.
* Average rentals:

  * Working days: approximately **4,200–4,400 per day**
  * Non-working days: approximately **4,500–4,700 per day**
* Non-working days are primarily associated with **recreational usage**, while working days indicate strong **commuter usage**.

**Conclusion:**
Marketing strategies can be optimized by offering **weekend promotions** for recreational users and improving infrastructure or services for commuters on working days, such as safe bike lanes and dedicated parking.

---

## Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

