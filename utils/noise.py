import numpy as np

def add_gaussian_noise(measure: float, median: float, std_d: float) -> float:
    "Añade ruido a una señal simulada con una distribución Gaussiana"
    noise = np.random.normal(median, std_d)
    print(noise)
    return measure + noise