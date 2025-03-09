# ProgressBar

**Descripción**  
Este proyecto proporciona una implementación sencilla de una barra de progreso en Python para monitorear el avance de un proceso iterativo. La barra de progreso puede ser útil al realizar tareas que toman tiempo, como procesamiento de datos o descargas.

---

## Instalación

Puedes instalar este paquete usando `pip`:

```python
#Ejemplo de uso:
list_data = range(1, 200)  # Un iterable simple para demostración

for index, value in Progress.view(list_data):
    # Simula algún trabajo (por ejemplo, procesamiento de datos)
    time.sleep(0.5)  # Simula un trabajo con un retraso de 50ms
```