import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


data = pd.read_excel('cau2_train.xlsx',encoding='utf-8')

data_target = data.iloc[:,0] 
print(data_target)

data_train=data.iloc[:,1:61]
print(data_train)

tree=DecisionTreeClassifier()
model_tree=tree.fit(data_train,data_target)

data_predict=pd.read_excel('cau2_predict.xlsx',encoding='utf-8')

data_result=pd.read_excel('cau2_result.xlsx',encoding='utf-8')


result=model_tree.predict(data_predict)

x=accuracy_score(data_result,result)

z=1-x

labels = ['Đúng', 'Sai']
sizes = [x,z]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  
ax.set_title('Kết quả dự đoán')

plt.show()