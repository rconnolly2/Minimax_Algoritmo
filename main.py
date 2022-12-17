import pygame
import cv2


class Juego:
    def __init__(self, color_fondo: tuple, titulo_ventana: str, dimensiones_ventana: tuple):
        """
        color_fondo => El color que queremos en el tetris en RGB con este formato (255, 255, 255)

        titulo_ventana => El nombre que queremos dar a la ventana

        dimensiones_ventana => Las dimensiones que queremos dar a la ventana en este formato "2 Int": (500, 500)
        """
        self.COLOR_FONDO = color_fondo
        self.titulo_ventana = titulo_ventana
        self.dimensiones = dimensiones_ventana
        self.running = True
        self.turno_jugador = True
        self.dimensiones_cuadro = dimensiones_ventana[0]/3
        self.cuadro = [["x", "0", "0"],
                       ["0", "o", "0"],
                       ["0", "0", "0"]]
        #Lista de coordenadas x, y de cada cuadro
        self.cuadros_lista = []


    def Inicio_Pygame(self):
        # titulo de ventana
        pygame.display.set_caption(self.titulo_ventana)
        try:
            self.pantalla = pygame.display.set_mode(self.dimensiones)
        except:
            print("Error Valores de color_fondo al crear el objeto juego invalido: tiene que ser 2 int (500, 500)")

        try:
            self.pantalla.fill(self.COLOR_FONDO)
        except:
            print(" Error Color de fondo invalido tiene que ser un tupla asi: (255, 0, 0)")

        #Creando Cuadricula
        self.Crear_Cuadricula()
        self.Imprimir_Tabla()
        self.Crear_Cuadros_Lista(self.cuadros_lista)


    def Crear_Cuadros_Lista(self, lista_coordenadas: list):
        """
        lista_cordenadas => La lista que queremos rellenar de coordeandas [x, y] de cada cuadro en nuestro juego tetris
        """
        x = 0
        y = 0
        for alto in range(3):
            for ancho in range(3):
                lista_coordenadas.append([int(x), int(y)]) # Añadimos coordeandas de cada cuadro x y x a nuestra lista
                x = x+self.dimensiones_cuadro # Añadimos en cada ciclo a x dimensiones de cada cuadro
            x = 0 # Al finalizar ir horizontalmente y pasamos a la siguiente linea verticalmente x = 0
            y = y+self.dimensiones_cuadro #Al finalizar ir hotizontalemnte pasamos a la siguiente linea vertical

    def Crear_Cuadricula(self):
        #Crear Cuadro
        ancho = 0
        alto = 0
        for h in range(3):

            for w in range(3):
                pygame.draw.rect(self.pantalla, (255, 0, 0), (ancho, alto, self.dimensiones_cuadro, self.dimensiones_cuadro), 2)
                ancho = ancho+self.dimensiones_cuadro+1
            ancho = 0
            alto = alto+self.dimensiones_cuadro+1

    def Imprimir_Tabla(self):
        ancho = 0
        alto = 0
        suma_up = pygame.Rect(((ancho+82)-15), alto+30, 30, 100)
        suma_down = pygame.Rect(((ancho+82)-50), alto+65, 100, 30)

        for i in range(3):
            for a in range(3):
                print(self.cuadro[a][i])
                #Comprobamos que si en caso que en la lista sea x pintamos x si es circulo circulo :
                if (self.cuadro[a][i] == "x"):
                    pygame.draw.rect(self.pantalla, (255, 0, 0), suma_up)
                    pygame.draw.rect(self.pantalla, (255, 0, 0), suma_down)
                elif (self.cuadro[a][i] == "o"):
                    pygame.draw.circle(self.pantalla, (255, 0, 0), (ancho+82, alto+82), 30, 3)

                ancho = ancho+self.dimensiones_cuadro+1

            ancho = 0
            alto = alto+self.dimensiones_cuadro+1

    def Detectar_Raton(self):
        botones_ratones = pygame.mouse.get_pressed(num_buttons=3)
        #Si el boton izquierdo del raton se presiona devolvemos x, y
        if botones_ratones[0] == True:
            pos_raton = pygame.mouse.get_pos()
            return pos_raton

    def Raton_Dentro(self, cordenadas_cuadros_lista: list):
        """
        Esta funcion se encarga de procesar las cordenadas x, y del raton y de cada cuadro de la lista => cordenadas_cuadros_lista
        y comprobamos si hay colision entre el raton => y cada cuadro utilizando el algo (Bounding Box collision)

        cordenadas_cuadros_lista => La lista de listas con dos int ejemplo (2x2): [[0, 0], [166, 0], [0, 166], [166, 166]]

        """
        x_raton = None
        y_raton = None
        for i in range(9):
            # Si la funcion Detector_raton tiene x, y dentro de su tuple 
            # (solo en caso que se clique el boton izquierdo del raton) => guardamos en 2 variables
            if not (self.Detectar_Raton() == None):
                coordeandas_raton = self.Detectar_Raton()
                print(coordeandas_raton)
                x_raton = coordeandas_raton[0]
                y_raton = coordeandas_raton[1]

            # Comprobamos colision bounding box https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-detection
            x_cuadro, y_cuadro = cordenadas_cuadros_lista[i]
            if (not x_raton == None) and (not y_raton == None):
                #Colision x raton => cuadro
                if (x_raton >= x_cuadro) and (x_cuadro + int(self.dimensiones_cuadro) >= x_raton):
                    #Colision y raton => cuadro
                    if (y_raton >= y_cuadro) and (y_cuadro + int(self.dimensiones_cuadro >= y_raton)):
                        return x_cuadro, y_cuadro # En caso de colison x, y 
                        #La funcion devolvera x, y del cuadro colisionado

        


    def Bucle_Juego(self):
        pygame.display.flip()
        # Comprobamos que se de al boton de cerrar ventana si es asi cerramos juego
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False

            #Aqui debajo va el codigo del bucle del juego:
            self.Raton_Dentro(self.cuadros_lista)




Tetris = Juego((255, 255, 0), ("Mi juego de tetris"), (500, 500))

Tetris.Inicio_Pygame()

Tetris.Bucle_Juego()
