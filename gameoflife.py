import pygame
import numpy as np
# Detalles de la ventana
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("The Game Of Life (Just a Visualization)")


# Inicializa pygame y fija los parámetros de la ventana
pygame.init()
size = X, Y = 640, 640
screen = pygame.display.set_mode(size)


# Color de fondo, celdas vivas y grid
bg = 25, 25, 25
cv=40,240,240
grid=40,140,240


# Numero de celdas (xd) en el eje x y numero de celdas (yd) en el eje y
# Admite dimensiones aún si no son cuadradas pero no se recomiendan valores
# mayores a 200 por cuestiones de visualización
yd=71
xd=71


# Dimensiones de las celdas
cellw  = X // xd
cellh  = Y // yd


# Se genera una matríz aleatoria de ceros y unos
gs=np.random.randint(0, 2, (xd,yd) )


while 1:
# Controlamos a cuantos frames por segundo correra la visualización 
    time = pygame.time.Clock().tick(20)
    
# Respuesta a eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()


    screen.fill(bg)
# Genera una copia de la matriz que empieza el loop
    ngs=np.copy(gs)

    for y in range(yd):
        for x in range(xd):
            pygame.draw.rect(screen, (cv), (x*cellw,y*cellh,cellw,cellh)  , 1-gs[x,y] )
            pygame.draw.rect(screen, (grid), (x*cellw,y*cellh,cellw,cellh)  ,1 )


# Cuenta el numero de vecinos vivos (es un arreglo toroidal, bordes conectados)
            vecinos= gs[(x-1)%xd,(y-1)%yd]  \
                    +gs[x       ,(y-1)%yd]  \
                    +gs[(x+1)%xd,(y-1)%yd]  \
                    +gs[(x-1)%xd,y       ]  \
                    +gs[(x+1)%xd,y       ]  \
                    +gs[(x-1)%xd,(y+1)%xd]  \
                    +gs[x       ,(y+1)%yd]  \
                    +gs[(x+1)%xd,(y+1)%yd]

            # Condiciones    
            # una celda muerta con 3 celdas vecinas vivas nace
            if gs[x,y]==0 and vecinos==3:
                ngs[x,y]=1
            # unq celda viva muere si no tiene 2 o 3 vecinas vivas
            elif gs[x,y]==1 and (vecinos<2 or vecinos >3):
                ngs[x,y]=0



    # Hacemos que el nuevo loop se genere con la nueva matriz
    gs=ngs   
    pygame.display.flip()