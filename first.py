import pandas
data= pandas.read_csv("iphone_price.csv")
print(data.head()) 

import matplotlib.pyplot as plt

plt.scatter(data['version'],data['price'])
plt.bar(data['version'],data['price'])
plt.show()