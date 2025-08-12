import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


archivo = 'PhaseSpace.phsp'
data = pd.read_csv(archivo,sep=r"\s+",skiprows=0,usecols=[0,1,5], header=None)

#[0] Pos X
#[1] Pos Y
#[5] Energy [MeV]

# Definir número de bins y rango
bins = 200
range_xy = [[-7, 7], [-7, 7]]  # rango en X e Y

# Crear histograma 2D ponderado por energía
hist, xedges, yedges = np.histogram2d(data[0], data[1], bins=bins, range=range_xy, weights=data[5])

# Graficar
plt.figure(figsize=(6,6))
plt.imshow(np.log10(hist+1).T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='gray')
plt.colorbar(label="log₁₀(Energía acumulada + 1)")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.title("Mapa de impactos ponderado por energía")
plt.savefig("XRays.png", dpi=300)
#plt.show()


