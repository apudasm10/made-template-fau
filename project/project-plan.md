# Project Plan

## Title
<!-- Give your project a short title. -->
### Capital Bikeshare: Rain or Shine, We'll Predict Your Ride

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do weather conditions (temperature, humidity, situation, wind speed, etc.) affect bike rentals?
2. What is the overall trend in bike rentals over the two years (2011-2012)?
3. Do casual users and registered users display different rental patterns throughout the year?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project analyzes the factors influencing Bike share rentals. By exploring the impact of weather (temperature, humidity, wind speed, etc.) and seasonality, we will try to find trends and patterns in bike rental numbers. Based on these factors, the goal is to develop a predictive model that predicts daily or hourly bike rental demand. Thus, this analysis will provide valuable and practical insights for optimizing eco-friendly mobility in the city, ensuring enough bikes are available when riders need them most.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Bike Sharing

* Metadata URL: <https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset>

* Data URL: <https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip>

* Data Type: Zip -> CSV

The dataset provides hourly and daily rental bike counts from 2011 to 2012, along with corresponding weather and seasonal data.  It can be used to analyze factors influencing Capital bikeshare rentals.

### Datasource2: Seoul Bike Sharing Demand

* Metadata URL: <https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand>

* Data URL: <https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip>

* Data Type: Zip -> CSV

The dataset provides hourly rental bike counts in Seoul from 2017 to 2018, along with corresponding weather data and holiday information.  It can be used to analyze factors influencing Seoul Bike Sharing System.>

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data collection and Pre-processing
2. Exploratory Data Analysis (EDA) and Feature Engineering
3. Statistical Modeling and Hyperparameter Tuning
4. Model Evaluation: preformance, interpretation, and insights
5. Reporting on findings
