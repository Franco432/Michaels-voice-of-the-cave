# PANTALLA DE CARGA -------------------------------------

# Importaciones necesarias para la pantalla de carga
from pygame.display import set_mode
from threading import Thread
from sources.carga import pantalla_carga

# Crear variables para la pantalla de carga
game = {'cargando':True, 'ejecutando':False, 'screen':set_mode((1280, 720))}

# Crear y ejecutar la pantalla de carga
Thread(target=pantalla_carga, args=(game,)).start()

# JUEGO ------------------------------------------------

# Intentar importar e inicializar cosas
try:
	# Importaciones necesarias para el juego
	from pygame import quit, init
	from pygame.time import delay, Clock
	from pygame.display import set_caption

	# Inicializar pygame
	init()

	# Ponerle título a la ventana
	set_caption("Michael's voice of the cave")

	# Importar las escenas del juego
	from sources.menu_inicio import menu_inicio
	from sources.pausa import pausa
	from sources.juego import juego

	# Crear instancias de escenas
	game['escenas'] = {}
	game['escenas']['menu'] = menu_inicio(game)
	game['escenas']['pausa'] = pausa(game)
	game['escenas']['juego'] = juego(game)
	game['escena_actual'] = 'menu'

	# Crear variables que controlen la escena actual
	clock = Clock()

	# Hacer que el juego se esté ejecutando
	game['ejecutando'] = True

	# Simular carga de datos
	delay(1000)

# Si hubo un error, hacer quer el juego no se ejecute
except Exception as e:
	print(f'\nAn error has ocurred loading the game, please report this with the key error:\n{e}\n')

# Parar la pantalla de carga
game['cargando'] = False

# Ejecutar bucle del juego
while game['ejecutando']:
	# Intentar correr un frame del juego
	try:
		# Actualizar el estado del juego respecto a lo que ocurra en la escena actual
		game['escenas'][game['escena_actual']].funciones()
		# Limitar fps y actualizar pantalla
		clock.tick(70)
	# Mostrar que ocurrió un error si eso pasa
	except Exception as e:
		ejecutando = False
		print(f'An error has ocurred during the game, please report this with the key error:\n{e}')

# Cerrar la ventana cuando termine el juego
quit()
input()
