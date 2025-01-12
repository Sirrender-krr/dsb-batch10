import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # for split data
from sklearn.linear_model import LinearRegression # for linear regression
from sklearn.tree import DecisionTreeRegressor # for decision tree regression
from sklearn.neighbors import KNeighborsRegressor # for KNN regression
from sklearn.ensemble import RandomForestRegressor # for random forest regression
from sklearn.linear_model import Ridge # for Ridge regression
from sklearn.metrics import mean_squared_error # for measuring
url = 'https://raw.githubusercontent.com/Sirrender-krr/dsb-batch10/refs/heads/main/R_programing/game_data_all.csv'
df = pd.read_csv(url,index_col=0)
df.head(6)

# Basic Info to know
# Inspect data
d = { 'col_name':df.columns,'sum_na':df.isna().sum()}
NA = pd.DataFrame(d).reset_index(drop=True)
display(df.info())
display(NA)

# Manipulate Data
df['release'] = pd.to_datetime(df['release'],format='%Y-%m-%d')
df['year'] = df['release'].dt.year

# Total game release each year
yearly_count = df['year'].value_counts().reset_index().sort_values('year')
yearly_count.columns = ['year','total games',]
yearly_count.plot.bar(x='year',y='total games',figsize=(16,9),rot=45,title='Yearly Release');

# Top 10 rating game in 2022
df2022 = df[df['year']==2022]
too_few = df2022['total_reviews'] < 10000
too_few
df2022 = df2022[~too_few]
df2022[['game','rating','total_reviews']].sort_values('rating',ascending=False).reset_index(drop=True).head(10)

# prepare data
x = df[['peak_players','positive_reviews','negative_reviews','total_reviews']] #choose features
y = df["rating"] #choose label
# split data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, \
random_state = 42) #random_state == set.seed() in R

#Linear Regression
# train model
model_ml = LinearRegression() # change model here
model_ml.fit(x_train,y_train)
# prediction
p_test = model_ml.predict(x_test)
p_train = model_ml.predict(x_train)
# evaluate
r_train = model_ml.score(x_train,y_train) # reture r-square
r_test = model_ml.score(x_test,y_test) # reture r-square
mse_test = mean_squared_error(y_test,p_test)
rmse_test = np.sqrt(mse_test)
mse_train = mean_squared_error(y_train,p_train)
rmse_train = np.sqrt(mse_train)
print(f"""Test result
RMSE: {rmse_test}
R-square:{r_test}
Train result
RMSE: {rmse_train}
R-square: {r_train}""")

#KNN
# train model
model_kn = KNeighborsRegressor() # change model here
model_kn.fit(x_train,y_train)
# prediction
p_test = model_kn.predict(x_test)
p_train = model_kn.predict(x_train)
# evaluate
r_train = model_kn.score(x_train,y_train) # reture r-square
r_test = model_kn.score(x_test,y_test) # reture r-square
mse_test = mean_squared_error(y_test,p_test)
rmse_test = np.sqrt(mse_test)
mse_train = mean_squared_error(y_train,p_train)
rmse_train = np.sqrt(mse_train)
print(f"""Test result
RMSE: {rmse_test}
R-square:{r_test}
Train result
RMSE: {rmse_train}
R-square: {r_train}""")

#Ridge
# train model
model_rd = Ridge() # change model here
model_rd.fit(x_train,y_train)
# prediction
p_test = model_rd.predict(x_test)
p_train = model_rd.predict(x_train)
# evaluate
r_train = model_rd.score(x_train,y_train) # reture r-square
r_test = model_rd.score(x_test,y_test) # reture r-square
mse_test = mean_squared_error(y_test,p_test)
rmse_test = np.sqrt(mse_test)
mse_train = mean_squared_error(y_train,p_train)
rmse_train = np.sqrt(mse_train)
print(f"""Test result
RMSE: {rmse_test}
R-square:{r_test}
Train result
RMSE: {rmse_train}
R-square: {r_train}""")

#Decision Tree
# train model
model_tr = DecisionTreeRegressor(random_state=0) # change model here
model_tr.fit(x_train,y_train)
# prediction
p_test = model_tr.predict(x_test)
p_train = model_tr.predict(x_train)
# evaluate
r_train = model_rd.score(x_train,y_train) # reture r-square
r_test = model_rd.score(x_test,y_test) # reture r-square
mse_test = mean_squared_error(y_test,p_test)
rmse_test = np.sqrt(mse_test)
mse_train = mean_squared_error(y_train,p_train)
rmse_train = np.sqrt(mse_train)
print(f"""Test result
RMSE: {rmse_test}
R-square:{r_test}
Train result
RMSE: {rmse_train}
R-square: {r_train}""")

#Random Forest
# train model
model_rf = RandomForestRegressor(random_state=0) # change model here
model_rf.fit(x_train,y_train)
# prediction
p_test = model_rf.predict(x_test)
p_train = model_rf.predict(x_train)
# evaluate
r_train = model_rf.score(x_train,y_train) # reture r-square
r_test = model_rf.score(x_test,y_test) # reture r-square
mse_test = mean_squared_error(y_test,p_test)
rmse_test = np.sqrt(mse_test)
mse_train = mean_squared_error(y_train,p_train)
rmse_train = np.sqrt(mse_train)
print(f"""Test result
RMSE: {rmse_test}
R-square:{r_test}
Train result
RMSE: {rmse_train}
R-square: {r_train}""")
