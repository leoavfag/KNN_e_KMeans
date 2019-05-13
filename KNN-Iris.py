import numpy as np
import pandas as pd
import random
import math
from sklearn import datasets
import matplotlib.pyplot as plt

def dist(x0, y0, x1, y1):
    a = (x1 - x0)**2 + (y1 - y0)**2
    b = math.sqrt(a)
    return b

iris = datasets.load_iris()
data = iris.data[:,0:2]
target = iris.target

k = 7      #Elementos a comparar
Clas = 3   #Numero de classificações
porcentagem = 0.5

df = pd.DataFrame(data,columns=['DataX','DataY'])

df['Classificação'] = 4

porInd = int(len(target)*porcentagem)

for i in range(porInd):
    i1 = random.randint(0,len(target)-1)
    df.loc[i1,'Classificação'] = target[i1]

dif4 = pd.DataFrame()

df['Distancia'] = 0.0

for i in range(len(data)):
    x0 = data[i][0]
    y0 = data[i][1]
    if df.loc[i,'Classificação'] == 4:
        for j in range(len(df['DataX'])):
            x1 = data[j][0]
            y1 = data[j][0]
            if df.loc[j,'Classificação'] != 4:
                df.loc[j,'Distancia'] = dist(x0, y0, x1, y1)
        dif4 = pd.DataFrame(df[df.Classificação != 4])
        dif3 = pd.DataFrame(dif4.sort_values(['Distancia']))
        count = np.zeros(Clas,dtype=int)
        for x in range(k):
            for y in range(Clas):
                Clase = pd.DataFrame(dif3['Classificação'].head(x+1))
                ClasEle = Clase.iloc[0][0]
                if ClasEle == y:
                   count[y] += 1
                   break
        for x in range(Clas):
            countPass = 0
            countIGUAIS = 0
            for y in range(Clas):
                if count[x] > count[y]:
                    countPass +=1
                elif count[x] == count[y]:
                    countIGUAIS += 1
            if countPass == 2:
                df.loc[i,'Classificação'] = x
                break
            elif countIGUAIS == k:
                Clase = dif3['Classificação'].head(1)
                ClasEle = Clase.iloc[0][0]
                df.loc[i,'Classificação'] = ClasEle
                break
               
            
        

print(df)

X = iris.data[:, :2]  # as duas primeiras caracteristicas
y = df.Classificação
plt.subplots()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Comprimento Sepala')
plt.ylabel('Largura Sepala')
plt.grid(True)
plt.show()
