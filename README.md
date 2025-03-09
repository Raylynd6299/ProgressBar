# ProgressBar

Implementation 

´´´python
#Ejemplo de uso:
list_data = range(1, 200)  # Un iterable simple para demostración

for index, value in Progress.view(list_data):
    # Simula algún trabajo (por ejemplo, procesamiento de datos)
    time.sleep(0.5)  # Simula un trabajo con un retraso de 50ms
´´´