



class Minimax:
    def __init__(self):
        pass

    def minimax(self, cuadro, profundidad, EstaMaximizando):
        return 1

    def MejorJugada(self, cuadro):
        mejor_puntuacion = 0
        jugada = None
        for alto in range(3):
            for ancho in range(3):
                #¿Espacio esta disponible?:
                if (cuadro[alto][ancho] == "0"):
                    cuadro[alto][ancho] = "x"
                    puntuacion = self.minimax(cuadro, 0, True)
                    #Revertimos
                    cuadro[alto][ancho] = "0"
                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        jugada = [alto, ancho]

        cuadro[jugada[0]][jugada[1]] = "x"
        print("maquina mueve")






