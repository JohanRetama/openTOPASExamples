import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


archivo = 'Dosis.csv'
data = pd.read_csv(archivo, sep=",", skiprows=8, usecols=[2,3,4], header=None)

#[2] Bin Z
#[3] Dosis [Gy]
#[4] Desviación Estandar

ancho_bin = 0.5
dosisPorcentual = data[3]/max(data[3])*100

plt.plot(data[2]*ancho_bin, dosisPorcentual, label='150 MeV')
plt.xlabel("z [cm]")
plt.ylabel("Dosis Porcentual")
plt.title("PDD Protones")
plt.legend()
plt.grid()
plt.show()