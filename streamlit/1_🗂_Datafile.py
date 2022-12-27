


import pandas as pd
import plotly.express as px
import streamlit as st
import math
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt



st.set_page_config(page_title = "Flight Prediction",
                    page_icon = ":airplane:",
                    layout="wide")


st.title("DataFile")
st.sidebar.success("Select a page above.")



flight2018 = "Combined_Flights_2018.csv"
flight2019 = "Combined_Flights_2019.csv"
flight2020 = "Combined_Flights_2020.csv"
flight2021 = "Combined_Flights_2021.csv"
flight2022 = "Combined_Flights_2022.csv"



df_2018 = pd.read_csv(flight2018, nrows=500)
df_2019 = pd.read_csv(flight2019, nrows=500)
df_2020 = pd.read_csv(flight2020, nrows=500)
df_2021 = pd.read_csv(flight2021, nrows=500)
df_2022 = pd.read_csv(flight2022, nrows=500)


# df_2018 = pd.read_csv(flight2018)
# df_2019 = pd.read_csv(flight2019)
# df_2020 = pd.read_csv(flight2020)
# df_2021 = pd.read_csv(flight2021)
# df_2022 = pd.read_csv(flight2022)

df_2018 = df_2018[["Year", "FlightDate", "Airline", "Origin", "Dest", "Cancelled", "DepTime", "DepDelayMinutes", "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "Diverted", "DayOfWeek", "DayofMonth"]]
df_2019 = df_2019[["Year", "FlightDate", "Airline", "Origin", "Dest", "Cancelled", "DepTime", "DepDelayMinutes", "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "Diverted", "DayOfWeek", "DayofMonth"]]
df_2020 = df_2020[["Year", "FlightDate", "Airline", "Origin", "Dest", "Cancelled", "DepTime", "DepDelayMinutes", "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "Diverted", "DayOfWeek", "DayofMonth"]]
df_2021 = df_2021[["Year", "FlightDate", "Airline", "Origin", "Dest", "Cancelled", "DepTime", "DepDelayMinutes", "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "Diverted", "DayOfWeek", "DayofMonth"]]
df_2022 = df_2022[["Year", "FlightDate", "Airline", "Origin", "Dest", "Cancelled", "DepTime", "DepDelayMinutes", "DepDel15", "DepartureDelayGroups", "DepTimeBlk", "Diverted", "DayOfWeek", "DayofMonth"]]


st.session_state["df_2018"] = df_2018
st.session_state["df_2019"] = df_2019
st.session_state["df_2020"] = df_2020
st.session_state["df_2021"] = df_2021
st.session_state["df_2022"] = df_2022


###########################################################


option_year = st.multiselect("Which year of datafile do you want to choose",
                            ["2018", "2019", "2020", "2021", "2022"])
submit2 = st.button("Submit Year", key="1")

if submit2:
    st.write("You have entered this year of Dataframe for visualization:")
    combined_list = []
    for year in option_year:
        if year == "2018":
            combined_list.append(df_2018)
        if year == "2019":
            combined_list.append(df_2019)
        if year == "2020":
            combined_list.append(df_2020)
        if year == "2021":
            combined_list.append(df_2021)
        if year == "2022":
            combined_list.append(df_2022)
        st.write(year)
    st.markdown("""---""")

    if len(combined_list) >1:
        df_combined = pd.concat(combined_list)
    elif len(combined_list) == 1:
        df_combined = combined_list[0]
    else:
        df_combined = ""

    st.session_state["Combined_df"] = df_combined

    df_combined = df_combined.replace({False: 0, True: 1})
    st.write("## Show Features:")
    st.write(df_combined.columns)

    df_groupByAirline = df_combined.groupby(['Airline']).agg({'Cancelled':'sum', "DepDelayMinutes": 'sum'})

    st.write("## Sum of delay minutes by airline - Decreasing Order")
    st.write(df_groupByAirline["DepDelayMinutes"].nlargest(len(df_groupByAirline)))

    st.write("## Sum of Canceled by airline - Decreasing Order")
    st.write(df_groupByAirline["Cancelled"].nlargest(len(df_groupByAirline)))



    st.write("## INFO ")
    left_column, middle_column, right_column = st.columns(3)
    # Total Flight 
    with left_column:
        st.subheader("Number of flight in in these years")
        st.subheader(f"{len(df_combined)}")
    # Number of Delayed Flight
    with middle_column:
        df_numdelayed = df_combined[df_combined["DepDel15"] > 0]
        st.subheader("Number of Canceled Flight in in these years")
        st.subheader(f" {len(df_numdelayed)}")
    # Number of Canceled Flight 
    with right_column:
        df_numcanceled = df_combined[df_combined["Cancelled"] == True]
        st.subheader("Number of Canceled flight in in these years")
        st.subheader(f"{len(df_numcanceled)}")

    left_column, right_column = st.columns(2)
    # Ratio of Delayed flight
    with left_column:
        df_delayed = df_combined[df_combined["DepDel15"] > 0]
        st.subheader("Ratio of Delayed flight in these years")
        st.subheader(f"{math.trunc(len(df_delayed)/len(df_combined)*100)}%")

    # Ratio of Canceled flight
    with right_column:
        df_canceled = df_combined[df_combined["Cancelled"] == True]
        st.subheader("Ratio of Canceled flight in these years")
        st.subheader(f"{math.trunc(len(df_canceled)/len(df_combined)*100)}%")
    st.markdown("""---""")


    st.write("## Pie Chart of Airline Ratio")
    fig, axis = plt.subplots(figsize=(10,14))
    Name = df_combined["Airline"].unique()
    size = df_combined["Airline"].value_counts()
    plt.pie(size,labels=Name,autopct='%5.0f%%')
    st.pyplot(fig)


    st.write("## Stripplot of Departure Delay Minutes by Airline")
    df_combined = df_combined.reset_index()

    fig, axs = plt.subplots(figsize=(10,10))
    sns.despine(bottom=True, left=True)
    dfdf=sns.stripplot(x="DepDelayMinutes", y="Airline",data = df_combined, dodge=True, jitter=True,palette="Set1")
    st.pyplot(fig)

    st.markdown("""---""")


    st.write("## Which 'Origin' airport has the most delays?")
    origin_airports_most_delays = df_combined[['Origin','DepDel15']].groupby('Origin').sum().sort_values(by='DepDel15',ascending=False)
    origin_airports_most_delays['PERCENTUAL'] = origin_airports_most_delays['DepDel15']/(origin_airports_most_delays['DepDel15'].sum())*100
    st.write(origin_airports_most_delays.head(10))


    st.write("# Top 10 US origin airports with the most delays for years")
    fig, axs = plt.subplots()
    airport_delay_hist_2018 = sns.histplot(data=origin_airports_most_delays[:10], x='Origin', y='DepDel15', hue='Origin')
    st.pyplot(fig)


    st.write("## Which 'Origin' airport has the most cancellations?")
    origin_airports_hightest_cancell = df_combined[['Origin','Cancelled']].groupby('Origin').sum().sort_values(by='Cancelled',ascending=False)
    origin_airports_hightest_cancell['PERCENTUAL'] = origin_airports_hightest_cancell['Cancelled']/(origin_airports_hightest_cancell['Cancelled'].sum())*100
    st.write(origin_airports_hightest_cancell.head(10))

    st.write("# Top 10 US origin airports with the most cancellation for years")
    fig, axs = plt.subplots()
    airport_delay_hist_2018 = sns.histplot(data=origin_airports_hightest_cancell[:10], x='Origin', y='Cancelled', hue='Origin')
    st.pyplot(fig)

    st.write("## Number of flights that have left a particular airport ")
    fig = plt.figure(figsize=(10, 10))
    axis = sns.countplot(y=df_combined['Origin'], data = df_combined,
                order=df_combined['Origin'].value_counts().iloc[:20].index,palette="Set2")
    axis.set_yticklabels(axis.get_yticklabels())
    plt.tight_layout()
    st.pyplot(fig)


    