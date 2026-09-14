#Simulación en Simpy con generador propio
import simpy
from colorama import Fore, Style

#Generador por método de congruencia lineal
def generador(semilla, a, c, mod):
    valor = ((a*semilla)+c) % mod
    return valor

#Evento definición
def definicion(env, nombre, porterias):
    llegada = env.now
    print(f"{llegada} - {nombre} ingresa a la cola para el ejercicio")
    with porterias.request() as solicitud:
        yield solicitud
        espera = env.now - llegada
        print(Fore.GREEN + f"{nombre} inicia ejercicio. Esperó {espera}" + Style.RESET_ALL)
        for i in range(10):
            semilla = 7
            valGen = generador(semilla,5,3,16)
            yield env.timeout(valGen)
            print(f"{env.now} - {nombre} realiza su remate {i+1}")
            semilla = valGen
        print(Fore.RED + f"{nombre} finalizó ejercicio a las {env.now}"+ Style.RESET_ALL)  

#Elementos de la simulación
entorno = simpy.Environment()
porterias = simpy.Resource(entorno, capacity=2)

#Eventos
entorno.process(definicion(entorno,"Ronaldo",porterias))
entorno.process(definicion(entorno,"Messi",porterias))
entorno.process(definicion(entorno,"Raúl",porterias))
entorno.process(definicion(entorno,"Guardado",porterias))

#Inicio de la simulación
entorno.run()