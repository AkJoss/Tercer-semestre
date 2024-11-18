# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:24:06 2024

@author: josea
"""
class Cola:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        #verificar que la cola esta vacia baby
        return len(self.items) == 0
        
    def encolar(self, item):
        #agregar un elemento al rear de la colar
        self.items.append(item)
            
    def desencolar(self):
        #eliminamos el elemento frontal
        if self.is_empty():
            raise IndexError("La cola esta vacia no se puede desencolar.")
        return self.items.pop(0)
        
    def size(self):
        #obtener el tamaño de la cola
        return len(self.items)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("La cola esta vacia no se puede desencolar.")
        return self.items[0]
        
class Paciente:
    
    def __init__(self, nombre, hora):
        self.nombre = nombre
        self.hora = hora

def main():
    queue = Cola()
    
    while True:
        print("1. Agregar paciente")
        print("2. Atender al siguiente paciente")
        print("3. Ver el siguiente paciente")
        print("4. Salir")
        seleccion = input("Elige una opcion: ")
        
        if seleccion == "1":
            nombre = input ("Ingrese el nombre del paciente: ")
            hora = input("Introduce la hora de llegada (ejemplo 10:00am): ")
            paciente = Paciente(nombre, hora)
            queue.encolar(paciente)
            print(f"Paciente {nombre} añadido a la cola\n")
            
        elif seleccion == "2":
            if not queue.is_empty():
                paciente = queue.desencolar()
                print(f"paciente {paciente.nombre} atendido\n")
            else:
                print("La cola esta vacia")
                
        elif seleccion == "3":
            if not queue.is_empty():
                paciente = queue.peek()
                print(f"Siguiente paciente a atender: {paciente.nombre}, Hora de llegada: {paciente.hora}\n")
            else:
                print("Ya no hay pacientes\n")
                
        elif seleccion =="4":
            break
            
        else: print("opcion no valida")
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep 12 16:37:59 2024

    @author: josea
    """
    import pygame
    import random

    # inicializar pygame
    pygame.init()

    #definir constantes
    ANCHO_VENTANA = 600
    ALTO_VENTANA = 700
    MARGEN = 10
    NUM_FILAS = 4
    NUM_COLUMNAS = 4
    TAMAÑO_CARTA = 100

    #Colores RGB (R, G, B)
    Blanco = (255, 255, 255)
    Negro = (0, 0, 0)
    Rojo_loco = (223, 68, 68)
    Azul_oscuro = (30, 77, 148)

    #Cargar imagenes
    imagenes = [
                "sandia.png"
                "platano.png"
                "guayaba.png"
                "tomate.png"
                "manzana.png"
                "uva.png"
                "naranja.png"
                "pera.png"
        ]
    imagenes_cartas = [pygame.image.load(img) for img in imagenes]
    imagen_reverso = pygame.image.load("cerebro.png")

    #Rendimiento imagenes a tamaño de las cartas
    imagenes_cartas = [pygame.transform.scale(img, (TAMAÑO_CARTA, TAMAÑO_CARTA)) for img in imagenes_cartas]
    imagen_reverso = pygame.transform.scale(imagen_reverso, (TAMAÑO_CARTA, TAMAÑO_CARTA))

    #Clase Pila para manejar las acciones del juego
    class Pila:
        def __init__(self):
            self.elementos = []
        
        def push(self, item):
            self.elementos.append(item)
            
        def pop(self):
            if not self.esta_vacia():
                return self.elementos.pop()
            return None
        
        def esta_vacia(self):
            return len(self.elementos) == 0
        
        def vaciar(self):
            self.elementos = []
            
    #Clase Cartas que representa cada parte del juego
    class Carta:
        def __init__(self, id_carta, imagen_frontal, pos):
            self.id_carta = id_carta #identificador unico de la carta
            self.imagen_frontal = imagen_frontal #imagen cuando la carta esta descubierta
            self.imagen_reverso = imagen_reverso #imagen cuando la carta esta oculta
            self.esta_volteada = False
            self.es_par_encontrado = False #indicador de si es parte de un par ya encontrado
            self.pos = pos #posicion en la pantalla
            
        def voltear(self):
            #metodo para voltear la carta
            if not self.es_par_encontrado: #solo permite voltear si no es parte de un par ya encontrado
                self.esta_volteada = not self.esta_volteada
            
        def es_par(self, otra_carta):
            #metodo que verifica si otra carta es el par de esta
            return self.id_carta == otra_carta.id_carta
        
        def dibujar(self, ventana):
            #dibujar la carta en la pantalla con un marco negro
            if self.esta_voteada:
                ventana.blit(self.imagen_frontal, self.pos)
            else:
                ventana.blit(self.imagen_reverso, self.pos)
     #Dibujar un marco negro al rededor de la carta
            pygame.draw.rect(ventana, Negro, (*self.pos, TAMAÑO_CARTA, TAMAÑO_CARTA),2)
        
        #Clase principal del juego
    class JuegoMemoria:
        def __init__(self):
            #inicializar la ventana
            self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
            pygame.display.set_caption("Juego de memoria")
            
            self.cartas_seleccionadas = []
            self.pila_movimientos = Pila() #Crear una pila para guardar movimiento
            self.cartas = []
            self.mensaje = "" #Mensaje que se muestra en pantalla
            self.temporizador = 0 #Temporizador para controlar el volteo de cartas
            self.ganador = False #Variable para indicar si el jugador ha ganado
            
            #Crear los botones de reiniciar y salir
            espacio_entre_botones = 20
            boton_ancho = 120
            boton_alto = 30
            
            self.boton_reiniciar = pygame.Rect(ANCHO_VENTANA // 2 - boton_ancho - espacio_entre_botones, 
                                               ALTO_VENTANA - 60, boton_ancho, boton_alto)
            self.boton_salir = pygame.Rect(ANCHO_VENTANA // 2 + espacio_entre_botones, 
                                           ALTO_VENTANA - 60, boton_ancho, boton_alto)
            #crear el tablero de cartas
            self.crear_tablero()
            
        def crear_tablero(self):
            #metodo para crear el tablero de cartas del juego
            total_cartas = NUM_FILAS * NUM_COLUMNAS
            cartas_ids = list(range(len(imagenes_cartas))) * 2 #Duplicar cartas
            random.suffle(cartas_ids)
            
            #distribuir cartas de froma uniforme en la ventana
            espacio_horizontal = (ANCHO_VENTANA - (NUM_COLUMNAS*TAMAÑO_CARTA) - ((NUM_COLUMNAS - 1)*MARGEN))//2
            espacio_vertical = (ALTO_VENTANA - 100 -(NUM_FILAS*TAMAÑO_CARTA) - ((NUM_FILAS - 1)*MARGEN))//2
            
            for fila in range(NUM_FILAS):
                for columna in range (NUM_COLUMNAS):
                    id_carta = cartas_ids.pop()
                    imagen_frontal = imagenes_cartas[id_carta]
                    pos_x = espacio_horizontal + columna * (TAMAÑO_CARTA + MARGEN)
                    pos_y = espacio_vertical + fila * (TAMAÑO_CARTA + MARGEN)
                    carta = Carta(id_carta, imagen_frontal, (pos_x, pos_y))
                    self.cartas.append(carta)
                    
        def manejar_eventos(self):
            #metodo para manejar los eventos del juego
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = evento.pos
                    
                    #verificar si se ha clikeado el boton de reiniciar
                    if self.boton_reiniciar.collidenpoint(mouse_x, mouse_y):
                        self.reiniciar_juego()
                        
                    #verificar si se ha clikeado el boton salir
                    if self.boton_salir.collidenpoint(mouse_x, mouse_y):
                        return False
                    
                    for carta in self.cartas:
                        if carta.pos[0] <= mouse_x <= carta.pos[0] + TAMAÑO_CARTA and carta.pos[1] <= mouse_y <= carta.pos[1] + TAMAÑO_CARTA:
                            carta.voltear()
                            self.cartas_seleccionadas.append(carta)
                            
            return True
        
        def actualizar(self):
            #Metodo para actualizar el estado del juego
            if len(self.cartas_seleccionadas) == 2:
                carta1, carta2 = self.cartas_seleccionadas
                if carta1.es_par(carta2):
                    self.mensaje = "¡Es par!"
                    carta1.es_par_encontrado = True
                    carta2.es_par_encontrado = True
                    self.cartas_seleccionadas = []#limpiar la seleccion de cartas
                else:
                    self.temporizador += 1
                    if self.temporizador > 60:
                        carta1.voltear()
                        carta2.voltear()
                        self.cartas_seleccionadas = []
                        self.temporizador = 0
                        self.mensaje = ""
            #verificar s el jugador ha ganado
            if all(carta.es_par_encontrado for carta in self.cartas):
                self.ganador = True
                self.mensaje = "Ganaste :D"
                
        def dibujar(self):
            #metodo para dibujar cartas, botones y mensaje en pantalla
            self.ventana.fill(Blanco)
            for carta in self.cartas:
                carta.dibujar(self.ventana)
                
            #Dibujar el boton de reiniciar
            pygame.draw.rect(self.ventana, Rojo_loco, self.boton_reiniciar)
            fuente = pygame.front.SysFont(None, 36)
            texto_reiniciar = fuente.render("Reiniciar", True, Blanco)
            texto_reiniciar_rect = texto_reiniciar.get_rect(center=self.boton_reiniciar.center)
            self.ventana.blit(texto_reiniciar, texto_reiniciar_rect)
            
            #Dibujar el boton de salir
            pygame.draw.rect(self.ventana, Azul_oscuro, self.boton_salir)
            texto_salir = fuente.render("Salir", True, Blanco)
            texto_salir_rect = texto_salir.get_rect(center=self.boton_salir.center)
            self.ventana.blit(texto_salir, texto_salir_rect)
            
            #mostrar el mensaje de resultado
            texto_mensaje = fuente.render(self.mensaje, True, Negro)
            self.ventana.blit(texto_mensaje,(ANCHO_VENTANA//2- 100, 20))
            
            pygame.display.flip()
        
        def reiniciar_juego(self):
            #metodo para reiniciar juego y reorganizar las cartas
            self.cartas = []
            self.mensaje = ""
            self.ganador = False
            self.temporizador = 0
            self.crear_tablero()
    #funcion principal de juego
        def main():
            juego = JuegoMemoria()
            reloj = pygame.time.Clock() 
            corriendo = True
            while corriendo:
                corriendo = juego.manejar_eventos()
                juego.actualizar()
                juego.dibujar()
                reloj.tick(60) #60 FPS para una animacion mas fluida
            pygame.quit()
        if __name__ == "__main__":
            main()               