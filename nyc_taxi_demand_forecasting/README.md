# New York Taxi Demand Forecast 
 

The objective is to forecast the demand for taxis by predicting the number of passengers in the next hour.

## Acknowledgements
The data was originally published by the NYC Taxi and Limousine Commission (TLC) and made publicly available 
via [NYC Open Data](https://opendata.cityofnewyork.us/). For the purpose of this challenge the data was sampled 
and additional weather data was added. The weather data was published on kaggle datasets: 
[Historical Hourly Weather Data 2012-2017](https://www.kaggle.com/selfishgene/historical-hourly-weather-data).

## Data

You are provided with hourly NYC Yellow Cab trip record data from January 2016 to December 2017. The data was
originally sampled on a per-trip basis and aggregated to hourly intervals for this challenge. 
The dataset is not cleaned and can contain invalid data points or outliers.

You must predict the total count of passengers in the next hour, using only information 
available prior to the respective period.

You can choose how you split your data into a training and test sets but the test set should be at least 
15% of the whole dataset (make sure that you don't have any data leakage).

### Attributes  

* timestamp: unix seconds	
* passenger_count (label): 
    The number of passengers in the vehicle (driver entered value), summed up over 1 hour.
* trip_distance: 
    The elapsed trip distance in miles reported by the taximeter, summed up over 1 hour.
* total_amount: 
    The total amount charged to passengers. Does not include cash tips, summed up over 1 hour.
* humidity: Relative humidity.
* pressure: Air pressure.
* temperature: Temperature in Kelvin.
* weather_description: Description of the weather situation.
* wind_direction: Wind direction measured in degrees clockwise.
* wind_speed: Wind speed in m/s.

You can use the available features if you find them useful and apply additional feature engineering. 

  


## For some extra fun (optional)

Use some anomaly detection methods on the label and search for unusual patterns in taxi demands.


