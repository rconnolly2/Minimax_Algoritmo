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
        self.dimensiones_cuadro = dimensiones_ventana[0]/3
        self.cuadro = [["x", "0", "0"],
                       ["0", "0", "0"],
                       ["0", "0", "0"]]


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
        fila = 0
        columna = 0
        for i in range(3):
            for a in range(3):
                #print(self.cuadro[fila][columna])
                print(int(ancho), int(alto))
                pygame.draw.circle(self.pantalla, (255, 0, 0), (ancho+165, alto+165), 10, 3)
                ancho = ancho+self.dimensiones_cuadro+1


                columna = columna+1
            ancho = 0
            alto = alto+self.dimensiones_cuadro+1

            fila = fila+1
            columna = 0
            


    def Bucle_Juego(self):
        pygame.display.flip()
        # Comprobamos que se de al boton de cerrar ventana si es asi cerramos juego
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False




Tetris = Juego((255, 255, 0), ("Mi juego de tetris"), (500, 500))

Tetris.Inicio_Pygame()

Tetris.Bucle_Juego()