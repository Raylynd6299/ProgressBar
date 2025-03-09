import sys
import time
from typing import Iterable, Tuple, Any


class Progress:
    def __init__(
        self,
        iterable: Iterable[Any],
        length: int = 40,
        prefix: str = "Progress",
        suffix: str = "Complete",
        fill_char: str = "=",
        empty_char: str = "-",
    ) -> None:
        """
        Inicializa la barra de progreso con los parámetros proporcionados.

        :param iterable: El iterable que se va a recorrer (ejemplo: lista, rango, etc.)
        :param length: La longitud de la barra de progreso.
        :param prefix: El texto que aparece antes de la barra de progreso.
        :param suffix: El texto que aparece después de la barra de progreso.
        """
        self.iterable = iterable
        self.total = len(iterable)
        self.length = length
        self.prefix = prefix
        self.suffix = suffix
        self.index = 0
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.start_time = time.time()  # Tiempo de inicio
        self.last_time = self.start_time  # El último tiempo registrado
        self.processed = 0  # Elementos procesados

    def __iter__(self) -> "Progress":
        """Hace que la clase sea iterable."""
        return self

    def __next__(self) -> Tuple[int, Any]:
        """
        Devuelve el siguiente valor del iterable y actualiza la barra de progreso.

        :return: Una tupla con el índice y el valor actual del iterable.
        """
        if self.index >= self.total:
            raise StopIteration  # Termina la iteración cuando se alcanza el final del iterable

        value = self.iterable[self.index]

        # Actualiza la barra de progreso
        self.update_progress(self.index + 1)

        self.index += 1
        return self.index - 1, value  # Devuelve el índice y el valor

    def update_progress(self, current_index: int) -> None:
        """
        Actualiza la barra de progreso durante la iteración.

        :param current: El número de iteración actual.
        """
        percent = (current_index) / self.total * 100
        filled_length = int(self.length * current_index // self.total)
        bar = self.fill_char * filled_length + self.empty_char * (
            self.length - filled_length
        )

        # Calculamos el tiempo transcurrido y estimamos el tiempo restante
        elapsed_time = time.time() - self.start_time
        items_processed = current_index
        if items_processed > 0:
            avg_time_per_item = elapsed_time / items_processed
            remaining_items = self.total - items_processed
            eta = avg_time_per_item * remaining_items
        else:
            eta = 0  # Si no se ha procesado ningún item aún, no hay ETA

        # Formateamos el ETA (tiempo restante en minutos y segundos)
        eta_minutes, eta_seconds = divmod(eta, 60)
        eta_str = f"{int(eta_minutes):02}:{int(eta_seconds):02}"

        # Imprime la barra de progreso en la misma línea
        sys.stdout.write(
            f'\r{self.prefix} |{bar}| {percent:.2f}% [{current_index}/{self.total}] {self.suffix if percent == 100 else ""} ETA:{eta_str}  '
        )
        sys.stdout.flush()  # Asegura que se imprima inmediatamente

    @staticmethod
    def view(iterable: Iterable[Any]) -> "Progress":
        """
        Método estático para crear una instancia de la barra de progreso.

        :param iterable: El iterable que se va a recorrer.
        :return: Una instancia de la clase Progress.
        """
        return Progress(iterable, fill_char="*")



