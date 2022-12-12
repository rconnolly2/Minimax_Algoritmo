import pygame
import cv2

COLOR_FONDO = (255, 230, 255)
running = True

pantalla = pygame.display.set_mode((500, 500))

pygame.display.set_caption("3 en raya Minimax")

pantalla.fill(COLOR_FONDO)

#Actualizar pantalla seria como SDL Display
pygame.display.flip()


while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

