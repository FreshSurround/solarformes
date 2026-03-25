import time

def timer(func):
    def tiempo(*args, **kwargs):
        starttime = time.time()
        func()
        endtime = time.time()
        return f"Tiempo de ejecución: {endtime - starttime} segundos"
    return tiempo
