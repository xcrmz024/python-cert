import time

from mod3_funciones_y_pythonic.context_managers import timer
from mod3_funciones_y_pythonic.decorators import retry
from mod3_funciones_y_pythonic.generators import batch_generator

# decorators:
contador = 0


@retry(max_retries=3, backoff=1)
def saludar(nombre):
    global contador
    contador += 1
    print(f"Intento {contador}")

    if contador < 3:
        raise ValueError("Algo salió mal")

    print(f"Hola, {nombre}")


saludar("Ana")


# generators:
numbers = [1, 2, 3, 4, 5, 6, 7]

for batch in batch_generator(numbers, 3):
    print(batch)


# context_manager:
with timer():
    time.sleep(2)
