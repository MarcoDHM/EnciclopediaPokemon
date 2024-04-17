import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Definir la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Memoria de Colores")

# Fuente para el mensaje de victoria
fuente = pygame.font.Font(None, 36)

# Reloj para controlar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Definir clase para cuadrado
class Cuadrado:
    def __init__(self, color, x, y, lado):
        self.color = color
        self.rect = pygame.Rect(x, y, lado, lado)
        self.mostrando = False
        self.encontrado = False

    def dibujar(self):
        if self.encontrado:
            pygame.draw.rect(pantalla, self.color, self.rect)
        elif self.mostrando:
            pygame.draw.rect(pantalla, self.color, self.rect)
        else:
            pygame.draw.rect(pantalla, BLANCO, self.rect)

# Función para crear el tablero de juego
def crear_tablero(filas, columnas):
    num_parejas = (filas * columnas) // 2
    colores_disponibles = [ROJO, VERDE, AZUL, AMARILLO]  # Colores disponibles para elegir

    # Asegurar que haya suficientes colores para el número deseado de parejas
    while len(colores_disponibles) < num_parejas:
        colores_disponibles.extend(colores_disponibles)  # Duplicar los colores disponibles

    random.shuffle(colores_disponibles)
    colores_seleccionados = colores_disponibles[:num_parejas]  # Seleccionar suficientes colores para las parejas
    colores = colores_seleccionados * 2  # Duplicar los colores para formar las parejas
    random.shuffle(colores)

    tablero = []
    tablero_ancho = columnas * 80
    tablero_alto = filas * 80
    inicio_x = (ANCHO - tablero_ancho) // 2
    inicio_y = (ALTO - tablero_alto) // 2

    for i in range(filas):
        fila = []
        for j in range(columnas):
            color = colores.pop()
            cuadrado = Cuadrado(color, inicio_x + j * 80, inicio_y + i * 80, 60)
            fila.append(cuadrado)
        tablero.append(fila)
    return tablero

# Función principal del juego
def main():
    tablero = crear_tablero(4, 4)  # Tablero de 4x4 centrado
    seleccionados = []
    parejas_encontradas = 0
    clics = 0  # Contador de clics
    victoria = False

    while True:
        pantalla.fill(NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and len(seleccionados) < 2 and not victoria:
                pos = pygame.mouse.get_pos()
                for fila in tablero:
                    for cuadrado in fila:
                        if cuadrado.rect.collidepoint(pos) and not cuadrado.mostrando:
                            cuadrado.mostrando = True
                            seleccionados.append(cuadrado)
                            clics += 1
                            if len(seleccionados) == 2:
                                if seleccionados[0].color != seleccionados[1].color:
                                    pygame.time.set_timer(pygame.USEREVENT, 1000)  # Temporizador para ocultar el segundo cuadrado
                                else:
                                    seleccionados = []  # Reiniciar la lista de selección si se encontró una pareja
                                    parejas_encontradas += 1
                                    if parejas_encontradas == (len(tablero) * len(tablero[0])) // 2:
                                        victoria = True
                                        mensaje_victoria = fuente.render("¡Has ganado!", True, BLANCO)
                                        mensaje_rect = mensaje_victoria.get_rect(center=(ANCHO // 2, ALTO // 2))
                            break
            elif event.type == pygame.USEREVENT and len(seleccionados) == 2:
                # Ocultar el segundo cuadrado seleccionado después de un tiempo si no es una pareja
                for cuadrado in seleccionados:
                    cuadrado.mostrando = False
                seleccionados = []

        # Dibujar el tablero
        for fila in tablero:
            for cuadrado in fila:
                cuadrado.dibujar()

        # Si se ha ganado, mostrar mensaje de victoria
        if victoria:
            pantalla.blit(mensaje_victoria, mensaje_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de actualización de la pantalla
        reloj.tick(30)

# Iniciar el juego
if __name__ == "__main__":
    main()
