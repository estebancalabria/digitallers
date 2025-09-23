from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler #lleva los datos a una escala comun
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
import pandas as pd

print("Bienvenidos a mi evaluador de vinos")

dataset = load_wine()
#print(dataset.DESCR)
#print(dataset)
#print(dataset.feature_names)
#print(dataset.target_names)

#Esto para ver por pantalla los datos en formato tabla
##df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
##df['target'] = dataset.target
#print(df.head())

X = dataset.data     # Features  - Los datos que hay aca son las caracteristicas de los vinos
# Elijo alcoho
# Elijo alcohol, malic_acid, y color_intensity por nombre!
selected_features = ['proline', 'alcohol', 'color_intensity']
feature_indices = [dataset.feature_names.index(f) for f in selected_features]
X = dataset.data[:, feature_indices]



y = dataset.target   # Labels  - Los datos que hay aca la calidad del vino

#Preproceso de datos
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_text, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
accuracy = model.score(X_text, y_test)

print(f"El modelo tiene una precision de {accuracy*100:.2f}%")

#Interfaz grafica

root = tk.Tk()
root.title("Evaluador de Vinos")

def evaluar_vino():
    # Obtener los valores de las entradas
    proline = float(entry_proline.get())
    alcohol = float(entry_alcohol.get())
    color_intensity = float(entry_color_intensity.get())

    # Preprocesar los datos
    X_new = scaler.transform([[proline, alcohol, color_intensity]])
    # Realizar la prediccion
    prediccion = model.predict(X_new)
    label_result.config(text=f"Predicción: {dataset.target_names[prediccion][0]}")

# Crear los elementos de la interfaz
label_proline = tk.Label(root, text="Proline:")
label_proline.pack()
entry_proline = tk.Entry(root)
entry_proline.pack()

label_alcohol = tk.Label(root, text="Alcohol:")
label_alcohol.pack()
entry_alcohol = tk.Entry(root)
entry_alcohol.pack()

label_color_intensity = tk.Label(root, text="Color Intensity:")
label_color_intensity.pack()
entry_color_intensity = tk.Entry(root)
entry_color_intensity.pack()

button_evaluar = tk.Button(root, text="Evaluar Vino", command=evaluar_vino)
button_evaluar.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()