#Importacion de librerias
import simpy, random
from colorama import Fore, Style

#Entidad principal de la simulación
def cliente(env, nombre, cajas):
    llegada = env.now
    print(f"{env.now:.2f} - {nombre} llega a la cafetería")

    with cajas.request() as solicitud:
        yield solicitud

        espera = env.now - llegada

        print(Fore.GREEN + f"{env.now:.2f} - {nombre} empieza a pagar "
              f"(esperó {espera:.2f} min)" + Style.RESET_ALL)

        # Tiempo que tarda en pagar
        tiempo_pago = random.randint(2, 5)
        yield env.timeout(tiempo_pago)

        print(f"{env.now:.2f} - {nombre} termina de pagar")

# Creando el entorno
env = simpy.Environment()

# Definiendo recursos: 2 Cajas de atención disponibles
cajas = simpy.Resource(env, capacity = 3)

# Generar eventos (atención a cada cliente)
env.process(cliente(env, "Juanito", cajas))
env.process(cliente(env, "Perlita", cajas))
env.process(cliente(env, "Pedrito", cajas))
env.process(cliente(env, "Jaimito", cajas))

# Ejecutar simulación durante 30 minutos
env.run(until=30)