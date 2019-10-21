import pandas as pd
url_C02 = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Environmental%20footprint%20by%20food%20type%20(protein)%20-%20Clark%20%26%20Tilman%20(2017)/Environmental%20footprint%20by%20food%20type%20(protein)%20-%20Clark%20%26%20Tilman%20(2017).csv'
df_C02 = pd.read_csv(url_C02, error_bad_lines=False)
url_water='https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Water%20footprint%20food%20products%20-%20Mekonnen%20%26%20Hoekstra/Water%20footprint%20food%20products%20-%20Mekonnen%20%26%20Hoekstra.csv'
df_water = pd.read_csv(url_water, error_bad_lines=False)
df_nutrition=pd.read_csv('NutritionalFacts_Fruit_Vegetables_Seafood.csv',encoding='latin-1')
df_nutrition2=pd.read_csv('en.openfoodfacts.org.products.tsv',sep='\t')

url_C02 = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Environmental%20footprint%20by%20food%20type%20(protein)%20-%20Clark%20%26%20Tilman%20(2017)/Environmental%20footprint%20by%20food%20type%20(protein)%20-%20Clark%20%26%20Tilman%20(2017).csv'
df_C02 = pd.read_csv(url_C02, error_bad_lines=False)

df=df_nutrition2[['product_name','main_category','energy_100g','fat_100g','sugars_100g','carbon-footprint_100g','water-hardness_100g']]
df2 = df[np.isfinite(df['carbon-footprint_100g'])]

df33=pd.read_csv('nutrients.csv')

df_definitive=df33[['name','group','protein (g)','carbohydrate (g)','sugars (g)','fat (g)','calories']]

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

connection = mysql.connector.connect(host='remotemysql.com',
                                         database='3sRxPqRiLy',
                                         user='3sRxPqRiLy',
                                         password='dhpwyt9ufA', port=3306)
cursor = connection.cursor()



insertQuery="INSERT INTO foods2 (name,calories,carbohydrates,protein,fat,saturatedFats ,salt ,co2) "
for index,row in df.iterrows():
             insertQuery1=insertQuery+"VALUES('{0}',{6},{4},{1},{2},{3},{5},{7})".format(row[0].replace("'",""),row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             result = cursor.execute(insertQuery1)
             connection.commit()

mycursor = connection.cursor()
insertQuery="INSERT INTO foods2 (name,calories,carbohydrates,protein,fat,saturatedFats ,salt ,co2) VALUES('1',2,3,4,5,6,7,8)"
cursor.execute(insertQuery)
connection.commit()

for index,row in df.iterrows():
    
    b=translator.translate(row[0].lower(), dest='en')
    en_names.append(b.text)
df['product_name']=en_names


from sklearn import linear_model
from sklearn.metrics import mean_squared_error
model=linear_model.LinearRegression()
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
mean_squared_error(y_test, y_predict)
