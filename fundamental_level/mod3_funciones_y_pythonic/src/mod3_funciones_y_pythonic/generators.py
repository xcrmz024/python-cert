# 2. Generador por lotes
# iteradores, yield, generadores


def batch_generator(iterable, batch_size):
    for i in range(0, len(iterable), batch_size):
        yield iterable[i : i + batch_size]
