"""
Authors: Fabian Ricardo Tobar Numesqui frtobarn@unal.edu.co
Authors: Eduin Julian Barrera @unal.edu.co
…
Date: 2023-09-10
Purpose: Solution to workshop 4
"""

"""
En un planeta futurista, se encuentra una ciudad donde ciertos robots 
han adquirido conciencia y buscan escapar de la opresión humana. 
En este entorno, un robot de seguridad está programado para apresar a 
los robots rebeldes que desobedecen las leyes humanas. 
La ciudad futurista está densamente vigilada por drones, puertas de 
seguridad avanzadas y campos de energía que dificultan la huida de los robots.

Los robots poseen atributos clave, como su posición, nivel de salud y 
poder de ataque, y emplean métodos que describen sus acciones, como caminar, 
correr, saltar y atacar. Además, cuentan con un método "recibir daño" que resta 
salud cuando son atacados y un método "morir" que se ejecuta cuando su salud llega a cero. 
Por otro lado, los obstáculos en este mundo tienen atributos como posición, tamaño y rango 
de movimiento, y sus métodos involucran infligir daño a los robots al tocarlos, así como 
desaparecer o destruirse en ciertas circunstancias. 
"""

import arcade

# Constantes
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Taller 4"


# Window viene de pyglet(ver documentación para profundizar)
# Creamos la clase MyGameWindow que hereda de arcade.Window------------------------------------
class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(
            width,
            height,
            title,
            resizable=False,
        )
        self.set_location(0, 0)
        # En el constructor se setea pero para que funcione
        # debe llamarse el ondraw -> start_render()
        arcade.set_background_color(arcade.color.PURPLE_HEART)

        # Voy a guardar la posición y la velocidad del cazador aquí
        self.rc_xpos = 100
        self.rc_ypos = 100

        #velocidad del jugador (rc)
        self.rc_speed = 100
        #Booleanos para saber si se esta presionando alguna flecha
        self.rc_right = False
        self.rc_left = False
        self.rc_up = False
        self.rc_down = False


        # Voy a guardar la posición y la velocidad del dron aquí
        self.dron_xpos = 60
        self.dron_ypos = 25

        self.dron_xspeed = 300
        self.dron_yspeed = 100

    # Borra el anterior render y renderiza el cálculo actual
    def on_draw(self):
        arcade.start_render()

        # DIbujar mapa
        muro1 = Muro(10, 360, 20, True)
        muro1.dibujar()

        muro2 = Muro(SCREEN_WIDTH/2, 20, 20, False)
        muro2.dibujar()


        robot_enemigo = Robot_Prey(400, 100)
        robot_enemigo.dibujar()

        robot_cazador = RobotCazador(self.rc_xpos, self.rc_ypos)
        robot_cazador.dibujar()

        puerta = Puerta(300, 300, 2, False)
        puerta.dibujar()

        dron = Dron(self.dron_xpos, self.dron_ypos)
        dron.dibujar()

    # El update se ejecuta cada frame
    def on_update(self, delta_time: float):
        # Moviendo el dron por la pantalla en diagonals
        self.dron_xpos -= self.dron_xspeed * delta_time
        self.dron_ypos += self.dron_yspeed * delta_time
        # return super().on_update(delta_time)

        # Detectando los bordes de la pantalla (dron)
        if self.dron_xpos > (SCREEN_WIDTH - 50) or self.dron_xpos < 50:
            self.dron_xspeed *= -1

        if self.dron_ypos > (SCREEN_HEIGHT - 20) or self.dron_ypos < 20:
            self.dron_yspeed *= -1

        #moviendo al jugador Robot Cazador
        if self.rc_right:
            self.rc_xpos += self.rc_speed * delta_time
        if self.rc_left:
            self.rc_xpos -= self.rc_speed * delta_time
        if self.rc_up:
            self.rc_ypos += self.rc_speed * delta_time
        if self.rc_down:
            self.rc_ypos -= self.rc_speed * delta_time
    


    # Definiendo la entrada de usuario
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.rc_right = True
        if symbol == arcade.key.LEFT: 
            self.rc_left = True
        if symbol == arcade.key.UP:
            self.rc_up = True
        if symbol == arcade.key.DOWN:
            self.rc_down = True
        # return super().on_key_press(symbol, modifiers)


    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.rc_right = False
        if symbol == arcade.key.LEFT: 
            self.rc_left = False
        if symbol == arcade.key.UP:
            self.rc_up = False
        if symbol == arcade.key.DOWN:
            self.rc_down = False
        #return super().on_key_release(symbol, modifiers)

    
    


# El personaje Dron es del tipo obstaculo----------------------------------------------------------------
class Dron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        # Cuerpo del dron
        arcade.draw_ellipse_filled(self.x, self.y, 60, 30, arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(
            self.x - 50,
            self.x + 50,
            self.y + 1,
            self.y + -1,
            arcade.color.SILVER_CHALICE,
        )
        arcade.draw_ellipse_filled(self.x, self.y, 30, 15, arcade.color.SILVER_CHALICE)
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.BLACK_OLIVE)
        # Ala izquierda del dron
        arcade.draw_lrtb_rectangle_filled(
            self.x - 50,
            self.x - 41,
            self.y - 2,
            self.y - 8,
            arcade.color.IMPERIAL_PURPLE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x - 50,
            self.x - 41,
            self.y + 10,
            self.y + 2,
            arcade.color.IMPERIAL_PURPLE,
        )
        arcade.draw_circle_filled(
            self.x - 46, self.y + 10, 5, arcade.color.IMPERIAL_PURPLE
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x - 60, self.x - 51, self.y + 13, self.y + 13, arcade.color.WHITE_SMOKE
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x - 41, self.x - 32, self.y + 13, self.y + 13, arcade.color.WHITE_SMOKE
        )
        # Ala derecha del dron
        arcade.draw_lrtb_rectangle_filled(
            self.x + 41,
            self.x + 50,
            self.y - 2,
            self.y - 8,
            arcade.color.IMPERIAL_PURPLE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 41,
            self.x + 50,
            self.y + 10,
            self.y + 2,
            arcade.color.IMPERIAL_PURPLE,
        )
        arcade.draw_circle_filled(
            self.x + 45, self.y + 10, 5, arcade.color.IMPERIAL_PURPLE
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 50, self.x + 59, self.y + 13, self.y + 13, arcade.color.WHITE_SMOKE
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 32, self.x + 41, self.y + 13, self.y + 13, arcade.color.WHITE_SMOKE
        )


# El personaje Robot_Prey es del tipo enemigo----------------------------------------------------------------
class Robot_Prey:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        # Cuerpo del robot
        arcade.draw_lrtb_rectangle_filled(
            self.x, self.x + 50, self.y + 50, self.y + 1, arcade.color.GRAY_BLUE
        )
        # Cabezadel robot
        arcade.draw_parabola_filled(self.x, self.y, 450, 50, arcade.color.AERO_BLUE)
        # Ojos del robot
        arcade.draw_circle_filled(self.x + 30, self.y + 63, 3, arcade.color.RED_DEVIL)
        arcade.draw_circle_filled(self.x + 40, self.y + 63, 3, arcade.color.RED_DEVIL)
        # Brazos del robot
        arcade.draw_lrtb_rectangle_filled(
            self.x + 31,
            self.x + 70,
            self.y + 35,
            self.y + 25,
            arcade.color.SILVER_LAKE_BLUE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 51,
            self.x + 90,
            self.y + 50,
            self.y + 40,
            arcade.color.SILVER_LAKE_BLUE,
        )
        # Piernas del Robot
        arcade.draw_lrtb_rectangle_filled(
            self.x + 10,
            self.x + 20,
            self.y + 0,
            self.y - 10,
            arcade.color.SILVER_LAKE_BLUE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 10,
            self.x + 25,
            self.y - 11,
            self.y - 14,
            arcade.color.SILVER_LAKE_BLUE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 28,
            self.x + 38,
            self.y + 0,
            self.y - 10,
            arcade.color.SILVER_LAKE_BLUE,
        )
        arcade.draw_lrtb_rectangle_filled(
            self.x + 28,
            self.x + 43,
            self.y - 11,
            self.y - 14,
            arcade.color.SILVER_LAKE_BLUE,
        )
        # Dientes del Robot
        arcade.draw_triangle_filled(
            self.x + 30,
            self.y + 55,
            self.x + 34,
            self.y + 55,
            self.x + 32,
            self.y + 52,
            arcade.color.RED_DEVIL,
        )
        arcade.draw_triangle_filled(
            self.x + 35,
            self.y + 55,
            self.x + 39,
            self.y + 55,
            self.x + 37,
            self.y + 52,
            arcade.color.RED_DEVIL,
        )
        arcade.draw_triangle_filled(
            self.x + 40,
            self.y + 55,
            self.x + 44,
            self.y + 55,
            self.x + 42,
            self.y + 52,
            arcade.color.RED_DEVIL,
        )


# El personaje RobotCazador es del tipo enemigo----------------------------------------------------------------
class RobotCazador:
    def __init__(self, x, y):
        # Posición del robot
        self.x = x
        self.y = y
        # Salud del robot
        self.salud = 100

    def dibujar(self):
        # Cuerpo del robot
        arcade.draw_rectangle_filled(self.x, self.y, 40, 50, arcade.color.DEEP_LEMON)

        # Cabeza del Robot
        arcade.draw_rectangle_filled(
            self.x, self.y + 30, 20, 20, arcade.color.RED_BROWN
        )

        # Antenas del robot
        arcade.draw_rectangle_filled(
            self.x - 5, self.y + 45, 2, 10, arcade.color.SILVER, -30
        )
        arcade.draw_rectangle_filled(
            self.x + 5, self.y + 45, 2, 10, arcade.color.SILVER, 30
        )

        # Ojos del robot
        arcade.draw_circle_filled(self.x - 5, self.y + 30, 3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 5, self.y + 30, 3, arcade.color.BLACK)

        # Boca del robot
        arcade.draw_rectangle_filled(self.x, self.y + 20, 6, 3, arcade.color.WHITE)
        arcade.draw_rectangle_outline(self.x, self.y + 20, 7, 4, arcade.color.BLACK, 1)

        # Brazos del robot
        arcade.draw_rectangle_filled(
            self.x - 30, self.y + 15, 25, 10, arcade.color.DARK_BROWN, -45
        )
        arcade.draw_rectangle_filled(
            self.x + 30, self.y + 15, 25, 10, arcade.color.DARK_BROWN, 45
        )

        # Piernas del robot
        arcade.draw_rectangle_filled(
            self.x - 10, self.y - 30, 10, 20, arcade.color.DARK_BROWN
        )
        arcade.draw_rectangle_filled(
            self.x + 10, self.y - 30, 10, 20, arcade.color.DARK_BROWN
        )

    # El robot cazador puede caminar a una velocidad constante
    def caminar(self):
        self.x += 5

    # El robot cazador puede correr a diferentes velocidades
    def correr(self, velocidad):
        self.x += int(velocidad)

    # El robot cazador puede saltar, siempre con el mismo impulso
    def saltar(self):
        self.x += 5

    # El robot tambien puede atacar a los enemigos con 3 diferentes armas, cada una con poder de ataque diferente
    def atacar(self, arma, enemigo):
        if arma == "Pistola normal":
            potencia_ataque = 1
            enemigo.recibir_ataque(potencia_ataque)
        elif arma == "Pistola electromagnetica":
            potencia_ataque = 10
            enemigo.recibir_ataque(potencia_ataque)

    # Cuando se recibe un ataque se invoca el método que resta salud
    def recibir_ataque(self, potencia_ataque):
        self.salud -= potencia_ataque


# Clases del tipo obstaculo
class Puerta:
    def __init__(self, cx, cy, scale, vertical: bool):
        # Posición de la puerta
        self.cx = cx
        self.cy = cy
        self.w = 10
        self.h = 20 * scale
        # Escala y orientación del obstaculo
        self.scale = scale
        self.vertical = vertical

    def dibujar(self):
        if self.vertical:
            arcade.draw_rectangle_filled(
                self.cx, self.cy, self.w, self.h, arcade.csscolor.BLACK
            )
        else:
            arcade.draw_rectangle_filled(
                self.cx, self.cy, self.w, self.h, arcade.csscolor.BLACK, 90
            )


class Muro:
    def __init__(self, cx, cy, scale, vertical: bool):
        # Posición de la puerta
        self.cx = cx
        self.cy = cy
        self.w = 20
        self.h = 20 * scale
        # Escala y orientación del obstaculo
        self.scale = scale
        self.vertical = vertical

    def dibujar(self):
        if self.vertical:
            arcade.draw_rectangle_filled(
                self.cx, self.cy, self.w, self.h, arcade.csscolor.ORANGE
            )
        else:
            arcade.draw_rectangle_filled(
                self.cx, self.cy, self.w, self.h, arcade.csscolor.ORANGE, 90
            )


MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
