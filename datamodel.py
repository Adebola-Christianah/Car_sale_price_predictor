from scipy import stats
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
data_path="C:/Users/USER/Desktop/Data_Analysis/clean_df.csv"
df=pd.read_csv(data_path)
X = df[["highway-L/100km"]]
Y = df[['price']]
#print(X.head(10))
#print(Y.head(10))
lm = LinearRegression()
print(lm.fit(X,Y))
Yhat=lm.predict(X)
Yhat[0:5]   
print(lm.intercept_)
print(lm.coef_)
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-L/100km", y="price", data=df)
plt.ylim(0,)