from collections import deque
from datetime import datetime

def update_window(windows, device_id, timestamp_str, value):
    """Actualiza la ventana del dispositivo y devuelve la media actual."""
    
    if device_id not in windows:
        windows[device_id] = deque()
    
    window = windows[device_id]
    now = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    
    # Insertar nuevo punto
    window.append((now, value))
    
    # Purgar puntos fuera de la ventana (más de 30 segundos)
    cutoff = now.timestamp() - 30
    while window and window[0][0].timestamp() < cutoff:
        window.popleft()
    
    # Calcular media
    if len(window) == 0:
        return None
    mean_value = sum(v for _, v in window) / len(window)
    return round(mean_value, 2)


def window_alarm(mean: float, device_id:str):
    if device_id == 's-termometer-01':
        if mean > 810: #Celsius
            print(f"[INGESTA][Warning]: valor de temperatura excesivo: {data})")
    if device_id == 's-barometer-01':
        if mean < 800: #hPa
            print(f"[INGESTA][Warning]: valor de presión demasiado bajo: {data}")