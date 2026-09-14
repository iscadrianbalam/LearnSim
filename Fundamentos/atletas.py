#Ejercicio 2 SimPy + Random + Colorama
#Importando librerias
import simpy, random
from colorama import Fore, Style

#Simulación
def atleta(env, nombre, desgasteProm, entrenos):
    datos = []
    prom = 0
    for i in range (0,entrenos):
        datos.append(random.uniform(desgasteProm-2,10))
        print(f"{env.now}: {nombre} entrenó, su desgaste fue de {datos[i]}")
        yield env.timeout(1)
        prom += datos[i]

    prom /= entrenos

    if(prom > desgasteProm):
        print(Fore.RED + f"{nombre} es propenso a sufrir lesión" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"{nombre} está bien fisicamente" + Style.RESET_ALL)

#Instancia del entorno
env = simpy.Environment()

#Iniciando procesos en el entorno (eventos)
env.process(atleta(env, "Julian", 8.5, 4))

#Iniciando simulación
env.run()