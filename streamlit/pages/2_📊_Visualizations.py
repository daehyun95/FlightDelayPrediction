import pandas as pd
import plotly.express as px
import streamlit as st
import math
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


st.set_page_config(page_title = "Visualization", page_icon = ":bar_chart:")
st.title("📊Visualizations 2018-2022")



df_2018 = st.session_state["df_2018"] 
df_2019 = st.session_state["df_2019"]
df_2020 = st.session_state["df_2020"] 
df_2021 = st.session_state["df_2021"] 
df_2022 = st.session_state["df_2022"] 



st.write("## Number of Flight each year")
num_flight_year = {"2018": len(df_2018), "2019": len(df_2019) , "2020": len(df_2020),"2021": len(df_2021)}


source= pd.DataFrame( { "Year": ["2018","2019","2020","2021","2022"],
                        "Number of Flight": [len(df_2018),len(df_2019), len(df_2020), len(df_2021), len(df_2022)]
                        })
bar_chart = alt.Chart(source).mark_bar().encode(x="Year", y="Number of Flight")
st.altair_chart(bar_chart, use_container_width=True)



df_2018_numdelayed = df_2018[df_2018["DepDel15"] > 0]
df_2018_numcanceled = df_2018[df_2018["Cancelled"] == True]
df_2019_numdelayed = df_2019[df_2019["DepDel15"] > 0]
df_2019_numcanceled = df_2019[df_2019["Cancelled"] == True]
df_2020_numdelayed = df_2020[df_2020["DepDel15"] > 0]
df_2020_numcanceled = df_2020[df_2020["Cancelled"] == True]
df_2021_numdelayed = df_2021[df_2021["DepDel15"] > 0]
df_2021_numcanceled = df_2021[df_2021["Cancelled"] == True]
df_2022_numdelayed = df_2022[df_2022["DepDel15"] > 0]
df_2022_numcanceled = df_2022[df_2022["Cancelled"] == True]


per_del2018 = len(df_2018_numdelayed)/len(df_2018)
per_del2019 = len(df_2019_numdelayed)/len(df_2019)
per_del2020 = len(df_2020_numdelayed)/len(df_2020)
per_del2021 = len(df_2021_numdelayed)/len(df_2021)


per_can2018 = len(df_2018_numcanceled)/len(df_2018)
per_can2019 = len(df_2019_numcanceled)/len(df_2019)
per_can2020 = len(df_2020_numcanceled)/len(df_2020)
per_can2021 = len(df_2021_numcanceled)/len(df_2021)



df_2018_changedNumeric = df_2018.replace({False: 0, True: 1})
df_2019_changedNumeric = df_2019.replace({False: 0, True: 1})
df_2020_changedNumeric = df_2019.replace({False: 0, True: 1})
df_2021_changedNumeric = df_2019.replace({False: 0, True: 1})
df_2022_changedNumeric = df_2019.replace({False: 0, True: 1})


frames = [df_2018_changedNumeric, df_2019_changedNumeric, df_2020_changedNumeric,df_2021_changedNumeric ,df_2022_changedNumeric ]
df_multiple = pd.concat(frames)

df_mutliple_groupByAirline = df_multiple.groupby('Airline').sum()
df_mutliple_groupByAirline = df_mutliple_groupByAirline.reset_index().rename(columns={df_mutliple_groupByAirline.index.name:'Airline'})
df_mutliple_groupByAirline = df_mutliple_groupByAirline[["Airline", "Cancelled" , "DepDelayMinutes"]] 




left_column, right_column = st.columns(2)
with left_column:
    st.write("## Number of Delayed Flight each year")
    num_delayed_flight_year = {"2018": len(df_2018_numdelayed), "2019": len(df_2019_numdelayed), "2020": len(df_2020_numdelayed),"2021": len(df_2021_numdelayed),"2022": len(df_2022_numdelayed)}
    source = pd.DataFrame(num_delayed_flight_year.items(), columns=["Year", "Number of Flight"])
    bar_chart = alt.Chart(source).mark_bar().encode(x="Year", y="Number of Flight")
    st.altair_chart(bar_chart, use_container_width=True)


    st.write("## Ratio of Delayed Flight each year")
    percentage_delayed_flight_year = {"2018": per_del2018, "2019": per_del2019, "2020": per_del2020,"2021": per_del2021}
    source = pd.DataFrame(percentage_delayed_flight_year.items(), columns=["Year", "Number of Flight"])
    bar_chart = alt.Chart(source).mark_bar().encode(x="Year", y="Number of Flight")
    st.altair_chart(bar_chart, use_container_width=True)

    st.write("## Number of total DepDelayMinutes Each Airline")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(x='Airline', y='DepDelayMinutes', data=df_mutliple_groupByAirline)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)

with right_column:
    st.write("## Number of Canceled Flight each year")
    num_canceled_flight_year = {"2018": len(df_2018_numcanceled), "2019": len(df_2019_numcanceled), "2020": len(df_2020_numcanceled),"2022": len(df_2022_numcanceled)}
    source = pd.DataFrame(num_canceled_flight_year.items(), columns=["Year", "Number of Flight"])
    bar_chart = alt.Chart(source).mark_bar().encode(x="Year", y="Number of Flight")
    st.altair_chart(bar_chart, use_container_width=True)


    st.write("## Ratio of Canceled Flight each year")
    num_canceled_flight_year = {"2018": len(df_2018_numcanceled), "2019": len(df_2019_numcanceled), "2020": len(df_2020_numcanceled),"2021": len(df_2021_numcanceled)}
    source = pd.DataFrame(num_canceled_flight_year.items(), columns=["Year", "Number of Flight"])
    bar_chart = alt.Chart(source).mark_bar().encode(x="Year", y="Number of Flight")
    st.altair_chart(bar_chart, use_container_width=True)


    st.write("## Number of total cancelled Flight Each Airline")
    fig, ax = plt.subplots(figsize=(7,4))
    num_cancell_Airline = sns.barplot(x='Airline', y='Cancelled', data=df_mutliple_groupByAirline)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)


# st.write("## Ratio of 3 Different Delayed Minutes Range")
# delay_type = lambda x:((0,1)[x > 60],2)[x > 120]
# df_multiple['DELAY_LEVEL'] = df_multiple['DepDelayMinutes'].apply(delay_type)
# fig5 = plt.figure(1, figsize=(15,7))
# ax1 = sns.countplot(x="Airline", hue='DELAY_LEVEL', data=df_multiple, palette= ["#00FF00","#FFA500","#FF0000"])
# labels = ax1.get_xticklabels()
# ax1.set_xticklabels(labels)
# plt.setp(ax.get_yticklabels(), fontsize=12, weight = 'normal', rotation = 0)
# plt.setp(ax.get_xticklabels(), fontsize=12, weight = 'normal', rotation = 90)
# ax1.xaxis.label.set_visible(False)
# plt.ylabel('No. of Flights', fontsize=16, weight = 'bold', labelpad=10)
# plt.ticklabel_format(style='plain', axis='y')
# L = plt.legend()
# L.get_texts()[0].set_text('on time (t < 60 min)')
# L.get_texts()[1].set_text('small delay (60 < t < 120 min)')
# L.get_texts()[2].set_text('large delay (t > 120 min)')
# st.pyplot(fig5)

st.write("## Number of flights that have left a particular airport ")
fig = plt.figure(figsize=(10, 10))
axis = sns.countplot(y=df_multiple['Origin'], data = df_multiple,
              order=df_multiple['Origin'].value_counts().iloc[:20].index,palette="Set2")
axis.set_yticklabels(axis.get_yticklabels())
plt.tight_layout()
st.pyplot(fig)


st.write("## Stripplot of Departure Delay Minutes by Airline")
df_multiple = df_multiple.reset_index()
fig, axs = plt.subplots(figsize=(10,10))
sns.despine(bottom=True, left=True)
dfdf=sns.stripplot(x="DepDelayMinutes", y="Airline",data = df_multiple, dodge=True, jitter=True,palette="Set1")
st.pyplot(fig)
