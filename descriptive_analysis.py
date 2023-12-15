from scipy import stats
import pandas as pd


data_path="C:/Users/USER/Desktop/Data_Analysis/clean_df.csv"
df=pd.read_csv(data_path)
#print(df[["price","wheel-base"]].head(10))
#print(df.dtypes)
print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())
# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts.head(10))
print(df[["stroke", "price"]].corr())
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  
#pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
#print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)
print(grouped_pivot.fillna(0))