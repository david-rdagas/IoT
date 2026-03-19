# Presión a 500 m ~ 954 hPa
# Presión a 1500 m ~ 845 hPa

"""

"""

import numpy as np


# Esto va en utils
def add_gaussian_noise(measure: float, median: float, std_d: float) -> float:
    "Añade ruido a una señal simulada con una distribución Gaussiana"
    noise = np.random.normal(median, std_d)
    return measure + noise



data = 100
data = add_gaussian_noise(100, 1, 1)