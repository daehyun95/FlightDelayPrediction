
To run the file, please downlaod 5 datasets and put in the folder

https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2021.csv&group=owned

* Combined_Flights_2018.csv
* Combined_Flights_2019.csv
* Combined_Flights_2020.csv
* Combined_Flights_2021.csv
* Combined_Flights_2022.csv

Since first two pages Visualization and DataFile needs to read all datafiles which is extremly large, it takes about 5 mins to run.
For faster look, you can comment out line 39-43 and use line 32-36 which is just using 500rows of each datasets of 2018 to 2022

Currently, default one is the 500 rows of each data files to easily view the web page

# Using just 500 rows of each file
df_2018 = pd.read_csv(flight2018, nrows=500)<br/>
df_2019 = pd.read_csv(flight2019, nrows=500)<br/>
df_2020 = pd.read_csv(flight2020, nrows=500)<br/>
df_2021 = pd.read_csv(flight2021, nrows=500)<br/>
df_2022 = pd.read_csv(flight2022, nrows=500)<br/>

# Using all
df_2018 = pd.read_csv(flight2018)<br/>
df_2019 = pd.read_csv(flight2019)<br/>
df_2020 = pd.read_csv(flight2020)<br/>
df_2021 = pd.read_csv(flight2021)<br/>
df_2022 = pd.read_csv(flight2022)<br/>
