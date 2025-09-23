from sklearn.datasets import load_diabetes
#eSCALADOR
from sklearn.preprocessing import StandardScaler #lleva los datos a una escala comun

dataset = load_diabetes()
print(dataset.DESCR)
print(dataset.feature_names)
#print(dataset.target)

#Transforo el dataset.targer en valores entre 0 y 1
y = dataset.target
y = (y - y.min()) / (y.max() - y.min())
print(y)





##print(dataset.target)
