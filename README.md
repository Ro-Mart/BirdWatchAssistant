#### Project BirdWatch Assistant



### Project Overview 
FeederWatch is a November-April survey of birds that visit anybody can participate in. The survey collects data about common bird species all over North America. I am using the data collected over many years to make predictions about the occurences of bird species. While the survey collects a lot of information (weather data, location information, etc.) I am focusing on Latitude, Longitude, the bird species, and the bird count in this project. In future project I may come back to investigate further and to make my predictions more stable.

Using Data which has been collected in surveys over the Winter Months in the years of 2011-2023, I am
        - using Clustering to identify location hotspots in British Columbia, Canada
        - using Facebook Prophet timeseries to predict sightings of bird species in the different location hotspots
        - comparing the Facebook Prophet predictions to just calculating the mean of bird species sighting (over the Winter months)
        - constructing an app on top of the models to have an easy user interface
Future Steps include:
        - For those locations and species where the mean performs better than the model (usually due to not enough data, e.g. a total of 45 sightings in BC from 2011-2023), try to find other methods to optimize predictions or call these out in the App
        - making the Streamlit app more user friendly and letting the user choose not only a bird species but also a specific timeframe in which they want to see the birds
        - Extending the analysis to other provinces and states in Canada and in the US


### Current Project Details
I have cleaned data from the years 2011 to 2023. You can find the cleaning and data exploration in the notebook `01_BirdWatch_EDA`. The second notebook contains a first timeseries model for just one chosen bird species. I discovered that it would be more helpful to look at weekly data than monthly data, which is why there are essentially two versions, `02_01_BirdWatch_EDA2_Timeseries_monthly` and `02_01_BirdWatch_EDA2_Timeseries_weekly`. 
The notebook `03_Location_Clustering` is used to identify 8 different Location hotspots in BC. The final Notebook `04_Timeseries_per_location` runs a total of 627 different Prophet models, one for each location and bird species.
Outputs from that notebook are used in my Streamlit App to help users identify good timeframes to find their favourite birds in the different locations.

### Project Organization

* `data` 
    - Raw data can be downloaded here: https://feederwatch.org/explore/raw-dataset-request . Unfortunately, even when zipped, these files are too big to be uploaded on GitHub.
    - The data dictionary can be found on the same website or in the data folder 
    - `CA_BC_feederwatch_2011_2023` contains the data which has been restricted to British Columbia and further cleaned in preparation for modelling
    - `CA_BC_clustered_feederwatch` is the dataset for British Columbia which also contains a column for the location cluster
    - The subfolder `Predictions` contains a total of 8 .csv files, one for every location cluster. These contain predictions for bird sightings in the years 2024-2025.

* `Notebooks` 
    - `01_BirdWatch_EDA`: Initial Cleaning and Exploration of all the used data
        - Input: All raw datasets from the feederwatch website
        - Output: A cleaned dataset containing all the data from 2011 to 2023 in just one csv file 'feederwatch_2011_2023'. Unfortunately, even when zipped, the file is too large to upload on GitHub.
    - `02_BirdWatch_EDA_2_Timeseries_monthly`: Restriction to data from BC, Canada, preparation for time series and first models using Prophet based on monthly data.
        - Inputs: The 'feederwatch_2011_2023' file created in Notebook 01
        - Output: The dataset 'CA_BC_feederwatch_2011_2023' and insights into how to create a prophet model for one selected bird species and the model performance using monthly data
    - `02_BirdWatch_EDA_2_Timeseries_weekly`: Similar to the previous notebook, but with focus on weekly data instead of monthly data for increased model performance. Also looks at simply using the mean over the Winter months for predictions
        - Inputs: The 'feederwatch_2011_2023' file created in Notebook 01
        - Output: Insights
    -`03_Location_Clustering.zip` Note that this notebook is zipped due to its size. It used K-Means clustering to divide the bird sightings in British Columbia into 8 hotspots, using Latitude and Longitude data.
        - Inputs: The dataset 'CA_BC_feederwatch_2011_2023' created in notebook 02
        - Output: The dataset 'CA_BC_clustered_feederwatch_2011_2023'
    -`04_Timeseries_per_location` This final notebook puts all findings together and creates Prophet model for each bird species encountered in each location. We evaluate these models based on two error metrics and compare to the performance of just using the mean. While the mean performs better in some locations, the Prophet model seems to be performing well for species that occur a lot.
    We then use the entire available dataset to train Prophet models and predict on 2024 and 2025.
        - Inputs: The dataset 'CA_BC_clusterd_feederwatch_2011_2023' created in notebook 03
        - Output: The prediction datasets 'cluster_{i}_predictions', where i is a number between 0 and 7
    

* `Streamlit_App`
    - `birdwatch.py` is the Streamlit App which displays the different Location clusters as and prediction plots for any bird species specified by the User
        -Inputs: The dataset 'CA_BC_clustered_feederwatch_2011_2023' and the prediction datasets 'cluster_{i}_predictions'
    - The folder also contains (copies of) the datasets used as inputs for the app