from pyexpat import model
import pandas
data= pandas.read_csv("iphone_price.csv")
print(data.head()) 

# import matplotlib.pyplot as plt

# plt.scatter(data['version'],data['price'])
# plt.bar(data['version'],data['price'])
# plt.show()




from sklearn.linear_model import LinearRegression

model= LinearRegression()
model.fit(data[['version']], data[['price']])

print(model.predict([[20]]))