#Ejercicio 1 SimPy + Random + Colorama
#Importando librerias
import simpy, random
from colorama import Fore, Style

#Simulación
def est(env, nombre):
    print(f"{env.now}: {nombre} llegó al Tec")
    retraso = random.randint(0,20)
    yield env.timeout(retraso)
    print(f"{env.now}: {nombre} entró al salón")
    if(retraso > 10):
        print(Fore.RED + f"{nombre} tiene falta" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"{nombre} tiene asistencia" + Style.RESET_ALL)

#Instancia del entorno
env = simpy.Environment()

#Iniciando procesos en el entorno (eventos)
env.process(est(env, "Luis"))
env.process(est(env, "José"))
env.process(est(env, "Maria"))
env.process(est(env, "Angela"))

#Iniciando simulación
env.run(until=20)




