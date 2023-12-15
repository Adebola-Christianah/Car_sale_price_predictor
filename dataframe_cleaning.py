import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



path="C:/Users/USER/Desktop/Data_Analysis/data_frame.csv"
df=pd.read_csv(path)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
#print(df.head(5))
#print(df.describe())
#print(df.describe(include='all')
df.replace('?',np.nan,inplace=True)
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

df.reset_index(drop=True, inplace=True)
#print(df.head(20)
df["num-of-doors"].replace(np.nan, "four", inplace=True)
avg_normalize_loss=df["normalized-losses"].astype('float').mean()
df["normalized-losses"].replace(np.nan,avg_normalize_loss,inplace=True)
avg_stroke=df['stroke'].astype('float').mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)
avg_bore=df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)
missing_data = df.isnull()
#for columm in missing_data.columns.values.tolist():
  #  print (missing_data[columm].value_counts())
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
avg_price=df['price'].astype('float').mean(axis=0)
df["price"].replace(np.nan, avg_price, inplace=True)
# transform mpg to L/100km by mathematical operation (235 divided by mpg)
df["highway-mpg"] = 235/df["highway-mpg"]

# rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)
# data normalization
df['height'] = df['height']/df['height'].max()
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max() 
df['height'] = df['height']/df['height'].max() 
#print(df[["length","width","height","highway-L/100km"]].head())
#data binning(i.e grouping)
df["horsepower"]=df["horsepower"].astype(float, copy=True)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
#print(df["horsepower-binned"].value_counts())
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
#print(df.head())
df.to_csv('clean_df.csv')

dummy_variable_2 = pd.get_dummies(df['aspiration'])

# change column names for clarity
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
# Plot the histogram
plt.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

# Show the plot
plt.show()