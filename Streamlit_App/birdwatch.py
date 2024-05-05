### KICKOFF - CODING AN APP IN STREAMLIT

### import libraries
import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
#import joblib

#st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
    #This is is just a very small window into its capabilities.')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



#######################################################################################################################################
### Create a title

st.title("BirdWatch App")

# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# An exciting kick off :tada:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>An exciting kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path):

    df = pd.read_csv(path)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates  
    return df


### Load entire BC dataframe
df = load_data("CA_BC_clustered_feederwatch_2011_2023.csv")
df_Cluster_0 = load_data("cluster_0_predictions.csv")
df_Cluster_1 = load_data("cluster_1_predictions.csv")
df_Cluster_2 = load_data("cluster_2_predictions.csv")
df_Cluster_3 = load_data("cluster_3_predictions.csv")
df_Cluster_4 = load_data("cluster_4_predictions.csv")
df_Cluster_5 = load_data("cluster_5_predictions.csv")
df_Cluster_6 = load_data("cluster_6_predictions.csv")
df_Cluster_7 = load_data("cluster_7_predictions.csv")




#######################################################################################################################################
### Bird Observations map

# Function to assign color based on Cluster
def get_marker_color(Cluster):
    if Cluster == 0:
        return (255, 0, 0)
    elif Cluster == 1:
        return (0, 0, 255)
    elif Cluster == 2:
        return (0, 255, 0)
    elif Cluster == 3:
        return (128, 0, 128)
    elif Cluster == 4:
        return (255, 255, 0)
    elif Cluster == 5:
        return (255, 165, 0)
    elif Cluster == 6:
        return (139, 69, 19)
    elif Cluster == 7:
        return (255, 192, 203)
    
# Apply marker color based on 'Species' column
df['marker_color'] = df['Cluster'].apply(get_marker_color)

st.subheader('Location Map - Bird sightings in BC from 2011 to  with Location clusters')      

st.map(df, color='marker_color')   

# Create a legend using HTML and CSS
legend_html = """
<div style="position: absolute; bottom: 50px; right: 50px; padding: 10px; background-color: white; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);">
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(255, 0, 0); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 0</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(0, 0, 255); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 1</span>
    </div>
        <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(0, 255, 0); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 2</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(128, 0, 128); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 3</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(255, 255, 0); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 4</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(255, 165, 0); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 5</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(139, 69, 19); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 6</span>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="width: 20px; height: 20px; background-color: rgb(255, 192, 203); margin-right: 5px;"></div>
        <span style="color: black;">Cluster 7</span>
        
</div>
"""

# Display the legend using st.markdown with unsafe_allow_html=True
st.markdown(legend_html, unsafe_allow_html=True)


##################################################################################################################################
### USER SELECTS BIRD SPECIES

# Display the subheader
st.subheader('Select a species')

# Widget to select a species from the DataFrame
selected_species = st.selectbox('Select a Bird species:', df['american_english_name'].unique())

# Display the selected species
st.write('You selected:', selected_species)

#Add prefix
prefixed_species = "no_of_" + selected_species

################################################################################################################################
### DISPLAY PREDICTIONS

# Display the subheader
st.subheader('Display Predictions for 2024 and 2025')

st.write('Note that the data is only based on surveys during the Winter months (November to April). '
         'Any predictions for the Summer months should not be considered reliable')

df_names = [df_Cluster_0, df_Cluster_1, df_Cluster_2, df_Cluster_3,
            df_Cluster_4, df_Cluster_5, df_Cluster_6, df_Cluster_7]

cluster = 0
for df in df_names:
    if prefixed_species in df.columns:
        st.write(f"{selected_species} may be encountered in Location {cluster}")
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['ds'], y=df[prefixed_species], mode='lines', name="Predictions"))

        fig.update_layout(
        yaxis_title="Sightings", 
        xaxis_title="Date",
        title= (f' Location {cluster} and {selected_species} predictions in 2024 and 2025')
        )

        # activate slider
        #fig.update_xaxes(rangeslider_visible=True, title = "date")
        st.plotly_chart(fig)
    else:
        st.write(f"{selected_species} is not usually found in Location {cluster}")
    cluster = cluster + 1

#######################################################################################################################################




#######################################################################################################################################
### Streamlit Advantages and Disadvantages
    
#st.subheader("Streamlit Advantages and Disadvantages")
#st.write('**Advantages**')
#st.write(' - Easy, Intuitive, Pythonic')
#st.write(' - Free!')
#st.write(' - Requires no knowledge of front end languages')
#st.write('**Disadvantages**')
#st.write(' - Apps all look the same')
#st.write(' - Not very customizable')
#st.write(' - A little slow. Not good for MLOps, therefore not scalable')
