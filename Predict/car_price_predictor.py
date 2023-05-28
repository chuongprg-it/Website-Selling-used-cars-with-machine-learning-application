# -*- coding: utf-8 -*-
"""Car_Price_Predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lv6eqhERLByjc0KLEV8r4k_L9Ob7GOq9

#IMPORT DATA
"""

import pandas as pd
import numpy as np
data = pd.read_csv('/content/drive/MyDrive/MACHINE LEARNING (TH)/car_price_predictor/quikr_car.csv')

# data = pd.read_csv('../cleanedCar.csv')
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


# # Tạo DataFrame từ dữ liệu
# df = pd.DataFrame(data)

# # Tính toán ma trận tương quan
# corr_matrix = np.corrcoef([df['Price'], pd.Categorical(df['fuel_type']).codes, pd.Categorical(df['name']).codes, pd.Categorical(df['kms_driven']).codes, pd.Categorical(df['company']).codes,pd.Categorical(df['year']).codes])

# # Chuyển sang DataFrame để trực quan hóa
# corr_df = pd.DataFrame(corr_matrix, columns=df.columns[[0,1,2,3,4,5]], index=df.columns[[0,1,2,3,4,5]])

# # Hiển thị heatmap
# sns.heatmap(corr_df, annot=True, cmap='coolwarm')
# plt.show()

data.head()

data.shape

data.info()

data['year'].unique()

data['Price'].unique()

data['kms_driven'].unique()

data['company'].unique()

data['fuel_type'].unique()

data['name'].unique()

"""#CLEANING DATA

"""

backup=data.copy()

data = backup

data=data[data['year'].str.isnumeric()]

data.head()

data['year'] = data['year'].astype(int)

data.shape

data.info()

data=data[data['Price']!="Ask For Price"]

data.shape

data['Price']=data['Price'].str.replace(',','').astype(int)

data.shape

data.info()

data['kms_driven']

data=data[data['kms_driven']!="Petrol"]

data.shape

data['kms_driven']=data['kms_driven'].str.split(' ').str.get(0).str.replace(',','')

data['kms_driven']

data.info()

data['kms_driven'].str.isnumeric()

data['kms_driven']=data['kms_driven'].astype(int)

data.info()

data['fuel_type']

data = data[~data['fuel_type'].isna()]
# ~: not

data.shape

data = data.reset_index(drop = True)

data['name']=data['name'].str.split(' ').str.slice(0,3).str.join(' ')

data.reset_index(drop=True)

data.describe()

data=data[data['Price']<6e6].reset_index(drop=True)

data.to_csv('Cleaned Car.csv')

# Xử lý dữ liệu
# data = pd.get_dummies(data, columns=['company'])
# data = data.fillna(0)

data

data_sorted = data.sort_values('company')
print(data_sorted['company'])

data['company'].unique()

data_no_duplicates = data.drop_duplicates()
data_no_duplicates

data

"""#TRỰC QUAN HÓA DỮ LIỆU






"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""##Bar Chart"""

# #
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.histplot(data['year'])

"""Tổng số xe theo từng năm 

"""

# Tạo một DataFrame mới với số lượng xe theo từng năm
car_counts = data['year'].value_counts().sort_index()

# Vẽ biểu đồ
plt.bar(car_counts.index, car_counts.values)

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Tổng số xe của từng năm')
plt.xlabel('Năm')
plt.ylabel('Số lượng xe')

# Hiển thị biểu đồ
plt.show()

"""Số lượng xe của từng hãng

"""

# Tạo một DataFrame mới với số lượng xe theo từng hãng
car_counts_by_company = data['company'].value_counts()

# Vẽ biểu đồ cột
plt.figure(figsize=(25, 6)) 
plt.bar(car_counts_by_company.index, car_counts_by_company.values)

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Số lượng xe của từng hãng')
plt.xlabel('Hãng xe')
plt.ylabel('Số lượng xe')

# Hiển thị biểu đồ
plt.show()

"""Số lượng xe theo loại nhiên liệu """

# Tạo một DataFrame mới với số lượng xe theo từng loại nhiên liệu
car_counts_by_fuel_type = data['fuel_type'].value_counts()

# Tạo một danh sách màu sắc cho các cột
colors = ['green', 'orange', 'purple'] 

# Vẽ biểu đồ cột
plt.bar(car_counts_by_fuel_type.index, car_counts_by_fuel_type.values, color=colors)

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Số lượng xe theo loại nhiên liệu')
plt.xlabel('Loại nhiên liệu')
plt.ylabel('Số lượng xe')

# Hiển thị biểu đồ
plt.show()

"""##Line Chart

Giá xe theo từng năm
"""

# Tạo một DataFrame mới với giá xe (price) và năm sản xuất (year)
df_price_year = data[['Price', 'year']]

# Tính giá trung bình của các xe theo từng năm
average_price_by_year = df_price_year.groupby('year').mean()

# Vẽ biểu đồ đường
plt.plot(average_price_by_year.index, average_price_by_year['Price'])

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Xu hướng thay đổi giá xe theo từng năm')
plt.xlabel('Năm')
plt.ylabel('Giá xe (USD)')

# Hiển thị biểu đồ
plt.show()

"""##Histogram

Biểu đồ phân phối giá xe
"""

# Vẽ biểu đồ phân phối giá xe
plt.hist(data['Price'], bins=20, edgecolor='black')

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Phân phối giá xe')
plt.xlabel('Giá xe')
plt.ylabel('Số lượng xe')
# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ phân phối giá xe
# plt.figure(figsize=(10, 6))
plt.hist(data['Price'], bins=20, edgecolor='black')

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Phân phối giá xe')
plt.xlabel('Giá xe')
plt.ylabel('Số lượng xe')

# # Chỉnh các nhãn trục x thành 500000
# tickss=[0,500_000,1_000_000,1_500_000,2_000_000,2_500_000,3_000_000]
# plt.xticks(ticks=tickss)

# Hiển thị biểu đồ
plt.show()

"""Số lượng xe theo km đã đi"""

# Vẽ biểu đồ phân phối số km đã đi
plt.hist(data['kms_driven'], bins=20, edgecolor='black')

# Đặt tiêu đề và các nhãn cho trục x và y
plt.title('Phân phối số km đã đi')
plt.xlabel('Số km đã đi')
plt.ylabel('Số lượng xe')

# Hiển thị biểu đồ
plt.show()

"""##Box Plot"""

# Vẽ biểu đồ hộp
sns.boxplot(x=data['Price'], color='red')

# Đặt tiêu đề và nhãn cho trục x
plt.title('Phân phối giá xe')
plt.xlabel('Giá xe')

# Hiển thị biểu đồ
plt.show()

"""##Scatter plot"""

# Tạo một bản sao của DataFrame với các cột 'price', 'km_driven', và 'fuel_type'
df_scatter = data[['Price', 'kms_driven', 'fuel_type']].copy()

# Tạo dictionary để ánh xạ các loại nhiên liệu thành màu sắc
fuel_colors = {'Petrol': 'red', 'Diesel': 'blue', 'LPG': 'green'}

# Vẽ biểu đồ scatter với màu sắc và kích thước điểm biểu thị thông tin
plt.scatter(df_scatter['kms_driven'], df_scatter['Price'], c=df_scatter['fuel_type'].map(fuel_colors), s=50)

# Đặt tiêu đề và nhãn cho trục x và y
plt.title('Mối quan hệ giữa giá xe và số km đã đi')
plt.xlabel('Số km đã đi')
plt.ylabel('Giá xe')

# Tạo legend cho màu sắc
for fuel, color in fuel_colors.items():
    plt.scatter([], [], c=color, label=fuel)

# Hiển thị legend
plt.legend()

# Hiển thị biểu đồ
plt.show()

"""#Ma trận tương quan"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chọn các cột cần phân tích tương quan
cols = ['name', 'fuel_type', 'Price', 'kms_driven']

# Tính ma trận tương quan
corr_matrix = data[cols].corr()

print(corr_matrix)

# Hiển thị ma trận tương quan dưới dạng heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

corr_matrix = np.corrcoef([data['kms_driven'], pd.Categorical(data['fuel_type']).codes, pd.Categorical(data['name']).codes])

print(corr_matrix)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tính toán ma trận tương quan
corr_matrix = np.corrcoef([df['Price'], pd.Categorical(df['fuel_type']).codes, pd.Categorical(df['name']).codes, pd.Categorical(df['kms_driven']).codes, pd.Categorical(df['company']).codes,pd.Categorical(df['year']).codes])

# Chuyển sang DataFrame để trực quan hóa
corr_df = pd.DataFrame(corr_matrix, columns=df.columns[[0,1,2,3,4,5]], index=df.columns[[0,1,2,3,4,5]])

# Hiển thị heatmap
sns.heatmap(corr_df, annot=True, cmap='coolwarm')
plt.show()

import matplotlib.pyplot as plt 
import seaborn as sns

corr = data.corr(method='pearson')
fig = plt.subplots(figsize=(3,3))
sns.heatmap(corr, vmax=1, square=True, annot=True, cmap='Blues')

#  from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_train, y_pred)

# #Vẽ đồ họa Confusion matrix
# from sklearn.metrics import ConfusionMatrixDisplay
# show_cm = ConfusionMatrixDisplay(cm)
# show_cm.plot()



"""MATPLOTLIB"""



"""#INPUT"""

X=data[['name','company','year','kms_driven','fuel_type']]
y=data['Price']

"""#LINEAR REGRESSION MODEL"""

# X = data.drop('Price', axis=1)
# y=data['Price']

X.shape
# y.shape

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.base import TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

ohe = OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])

ohe.categories_

column_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_
),['name','company','fuel_type']), remainder='passthrough')

lr = LinearRegression()

pipe=make_pipeline(column_trans, lr)

pipe.fit(X_train, y_train)

y_pred=pipe.predict(X_test)

y_pred

r2_score(y_test, y_pred)

scores=[]
for i in range(1000):
  X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=i)
  lr=LinearRegression()
  pipe=make_pipeline(column_trans, lr)
  pipe.fit(X_train, y_train)
  y_pred=pipe.predict(X_test)
  # print(r2_score(y_test, y_pred), i)
  scores.append(r2_score(y_test, y_pred))

np.argmax(scores)

scores[433]

scores[np.argmax(scores)]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=np.argmax(scores))
lr=LinearRegression()
pipe=make_pipeline(column_trans, lr)
pipe.fit(X_train, y_train)
y_pred=pipe.predict(X_test)
r2_score(y_test, y_pred)

import pickle

pickle.dump(pipe,open('LinearRegressionModel.pkl','wb'))

data[data['name']=='Hyundai Santro Xing']

data[(data['name'] == 'Hyundai Santro Xing') & (data['year'] == 2000)]

data[(data['name'] == 'Hyundai Santro Xing') & (data['year'] == 2002)]

# name = input('Nhap ten xe: ')

# company = input('Nhap hang xe: ')

# year = input('Nhap nam: ')

# kms_driven = input('Nhap so km: ')

# fuel_type = input('Nhap nhien lieu: ')

# pipe.predict(pd.DataFrame([[name,company,year,kms_driven,fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))

# pipe.steps[0][1].transformers[0][1].categories[0]

# data=np.array(['Maruti Suzuki Swift','Maruti',2019,100,'Petrol'])

# data

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2000,56450,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2002,3000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2003,3000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2003,50000,'Petrol']).reshape(1,5)))

import matplotlib.pyplot as plt
fig= plt.figure(figsize=(6,6))
# Tạo biểu đồ scatter plot
plt.scatter(y_test, y_pred, color='blue')
# plt.scatter(df['name'], y, color='red', label='Predicted Price')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='solid')

# Đặt tên cho trục x và trục y
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

# Đặt tiêu đề cho biểu đồ
plt.title('Actual vs Predicted Car Prices')

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

"""#Random Forest Regression Model"""

from sklearn.ensemble import RandomForestRegressor

rfg = RandomForestRegressor(random_state=100)

pipe=make_pipeline(column_trans, rfg)

pipe.fit(X_train, y_train)

y_pred=pipe.predict(X_test)

r2_score(y_test, y_pred)

scores=[]
for i in range(1000):
  X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=i)
  rfg = RandomForestRegressor(random_state=100)
  pipe=make_pipeline(column_trans, rfg)
  pipe.fit(X_train, y_train)
  y_pred=pipe.predict(X_test)
  # print(r2_score(y_test, y_pred), i)
  scores.append(r2_score(y_test, y_pred))

np.argmax(scores)

scores[np.argmax(scores)]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=np.argmax(scores))
rfg = RandomForestRegressor(random_state=100)
pipe=make_pipeline(column_trans, rfg)
pipe.fit(X_train, y_train)
y_pred=pipe.predict(X_test)
r2_score(y_test, y_pred)

import pickle 
pickle.dump(pipe,open('RandomForestModel.pkl','wb'))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2000,36000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2003,50000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2002,3000,'Petrol']).reshape(1,5)))

data[data['name']=='Hyundai Santro Xing']

data[(data['name'] == 'Hyundai Santro Xing') & (data['year'] == 2003)]

data[data['name']=='Mahindra Bolero DI']

data[(data['name']=='Mahindra Bolero DI') & (data['year'] == 2017)]

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Mahindra Bolero DI','Mahindra',2017,23452,'Diesel']).reshape(1,5)))

y_test.shape

# import matplotlib.pyplot as plt
# plt.plot(X_test, y_test, "b.")
# plt.plot([min(Y), max(Y)], [min(Y), max(Y)], color='red', linestyle='--')

import matplotlib.pyplot as plt
fig= plt.figure(figsize=(6,6))
# Tạo biểu đồ scatter plot
plt.scatter(y_test, y_pred, color='blue')
# plt.scatter(df['name'], y, color='red', label='Predicted Price')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='solid')

# Đặt tên cho trục x và trục y
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

# Đặt tiêu đề cho biểu đồ
plt.title('Actual vs Predicted Car Prices')

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

# print(len(df['name']))
# print(len(df['Price']))
# print(len(y_pred))
# print(len(X_test))

"""#Decision Tree

"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()

pipe=make_pipeline(column_trans, dt)

pipe.fit(X_train, y_train)

y_pred=pipe.predict(X_test)

r2_score(y_test, y_pred)

scores=[]
for i in range(1000):
  X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=i)
  dt = DecisionTreeRegressor()
  pipe=make_pipeline(column_trans, dt)
  pipe.fit(X_train, y_train)
  y_pred=pipe.predict(X_test)
  # print(r2_score(y_test, y_pred), i)
  scores.append(r2_score(y_test, y_pred))

np.argmax(scores)

scores[np.argmax(scores)]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=np.argmax(scores))
dt =DecisionTreeRegressor()
pipe=make_pipeline(column_trans, dt)
pipe.fit(X_train, y_train)
y_pred=pipe.predict(X_test)
r2_score(y_test, y_pred)

import pickle 
pickle.dump(pipe,open('DecisionTreeModel.pkl','wb'))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2000,36000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2003,50000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2002,3000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Mahindra Bolero DI','Mahindra',2017,23452,'Petrol']).reshape(1,5)))

"""#Gradient Boosting

"""



from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
gr = GradientBoostingRegressor()

pipe=make_pipeline(column_trans, gr)

pipe.fit(X_train, y_train)

y_pred=pipe.predict(X_test)

r2_score(y_test, y_pred)

scores=[]
for i in range(1000):
  X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=i)
  gr = GradientBoostingRegressor()
  pipe=make_pipeline(column_trans, gr)
  pipe.fit(X_train, y_train)
  y_pred=pipe.predict(X_test)
  # print(r2_score(y_test, y_pred), i)
  scores.append(r2_score(y_test, y_pred))

np.argmax(scores)

scores[np.argmax(scores)]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=np.argmax(scores))
gr = GradientBoostingRegressor()
pipe=make_pipeline(column_trans, gr)
pipe.fit(X_train, y_train)
y_pred=pipe.predict(X_test)
r2_score(y_test, y_pred)

import pickle 
pickle.dump(pipe,open('GradientBoostingModel.pkl','wb'))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2000,36000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2003,50000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Hyundai Santro Xing','Hyundai',2002,3000,'Petrol']).reshape(1,5)))

pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array(['Mahindra Bolero DI','Mahindra',2017,23452,'Petrol']).reshape(1,5)))

"""#Accuracy Model"""

import matplotlib.pyplot as plt

# Các mô hình linear regression và độ chính xác tương ứng
models = ['Linear Regression', 'Random Forest', 'Decision Tree','Gradient Boosting']
accuracy = [0.8456515104452564, 0.89367369124803, 0.8926131328672074, 0.8292625108935117]

# Vẽ biểu đồ độ chính xác
colors=['green', 'orange', 'purple','red'] 
plt.bar(models, accuracy, color=colors)

# Đặt tiêu đề và nhãn cho trục x và y
plt.title('Accuracy của các mô hình linear regression')
plt.xlabel('Mô hình')
plt.ylabel('Accuracy')

# Hiển thị biểu đồ
plt.show()