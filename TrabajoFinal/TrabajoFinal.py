
import threading
import time
import random

tiempo_med = int(input("ingrese la cantidad de tiempo total (en segundos) en la que se realizarán mediciones: "))
tiempo_itera = int(input("ingrese cada cuanto tiempo (en segundos) se realizarán una medición: "))
temp_clf = int(input("Ingrese la temperatura de encendido de calefacción : "))



def timer(timer_runs):
    calef = "encedido"
    temp_inicial = int(random.randint(0, 32))
    while timer_runs.is_set():
        if calef == "encendido":
            temp_act = float(temp_inicial + random.randint(0, 2))
        else:
            temp_act = float(temp_inicial - random.randint(0, 2))

        if temp_clf < int(temp_act):
            calef = "Apagado"
        else:
            calef = "Encedido"
        print("Temp actual: ",temp_act," estado: ",calef)

        time.sleep(tiempo_itera)   # 3 segundos.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
# Esperar 10 segundos y luego detener el timer.
time.sleep(tiempo_med)
timer_runs.clear()
print("¡El timer ha sido detenido!")

