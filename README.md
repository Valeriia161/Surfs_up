
<img src="https://user-images.githubusercontent.com/110998103/194392848-43c8f344-e0a0-4143-8379-204491b03237.jpg" width=30% height=50%>

# ` Surfs-Up Challenge`
 ## `Project Overview ` <br/>
I was tasked with pulling weather information for Oahu that would be used to determine whether opening a Surf and Ice Cream shop was a good idea (based on weather trends year around). <br/>
This information would be presented to investors. <br/>
In this analysis, I determined the Summary Statistics for June. Then I determine the Summary Statistics for December. Finally, I submitted a written report  for the statistical climate analysis.  <br/>
 #### Resources
•	Data Source: [Google]( Google). <br/>
•	Software: Python, Jupyter, Git Bash, SQLAlchemy, Flask.
## `Results `
1.	Using Python, Pandas functions and methods, and SQLAlchemy, I  filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. Then I converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics. June Statistics for the Temperature and Precipitation can be found below:


![](https://user-images.githubusercontent.com/110998103/194391324-36040659-1ca3-4314-9f01-7fd8141c932b.png)
 


2.	After that, using Python, Pandas functions and methods, and SQLAlchemy, I filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December. Then I converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics. DEcember Statistics for the Temperature and Precipitation can be found below:


![December_temps](https://user-images.githubusercontent.com/110998103/194391443-1fabc3ee-5733-4137-906e-4434708028f7.png)


## ` Summary`
Based on the previous analysis I'd like to share my observations: <br/>
1.	The mean temperatures for both periods is only a difference of less than 4 degrees between June, 74.9°F, and December, 71.0°F. Both of which are in a comfortable zone for surfing. <br/>
2.	The max and min of the temperature values for both periods, are also in near comparison. <br/>
3.	December has a slightly smaller sample size that June. <br/>

The data suggests that the temperature in Oahu is ideal year-round for an ice cream / surf shop.


