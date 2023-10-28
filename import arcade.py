import arcade
# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Mini-Mundo en Arcade"

class Dron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        #Cuerpo del dron
        arcade.draw_ellipse_filled(self.x, self.y, 60, 30, arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(self.x-50,self.x+50,self.y+1,self.y+-1, arcade.color.SILVER_CHALICE)
        arcade.draw_ellipse_filled(self.x, self.y, 30, 15, arcade.color.SILVER_CHALICE)
        arcade.draw_circle_filled(self.x,self.y,5,arcade.color.BLACK_OLIVE)
        #Ala izquierda del dron
        arcade.draw_lrtb_rectangle_filled(self.x-50,self.x-41,self.y-2,self.y-8, arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(self.x-50,self.x-41,self.y+10,self.y+2,arcade.color.IMPERIAL_PURPLE)
        arcade.draw_circle_filled(self.x-46,self.y+10,5,arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(self.x-60,self.x-51,self.y+13,self.y+13,arcade.color.WHITE_SMOKE)
        arcade.draw_lrtb_rectangle_filled(self.x-41,self.x-32,self.y+13,self.y+13,arcade.color.WHITE_SMOKE)
        #Ala derecha del dron
        arcade.draw_lrtb_rectangle_filled(self.x+41,self.x+50,self.y-2,self.y-8, arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(self.x+41,self.x+50,self.y+10,self.y+2,arcade.color.IMPERIAL_PURPLE)
        arcade.draw_circle_filled(self.x+45,self.y+10,5,arcade.color.IMPERIAL_PURPLE)
        arcade.draw_lrtb_rectangle_filled(self.x+50,self.x+59,self.y+13,self.y+13,arcade.color.WHITE_SMOKE)
        arcade.draw_lrtb_rectangle_filled(self.x+32,self.x+41,self.y+13,self.y+13,arcade.color.WHITE_SMOKE)


class Robot_Prey:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
  
        # Cuerpo del robot
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + 50, self.y+50, self.y +1, arcade.color.GRAY_BLUE)
        # Cabezadel robot
        arcade.draw_parabola_filled(self.x,self.y,450,50,arcade.color.AERO_BLUE)
        # Ojos del robot
        arcade.draw_circle_filled(self.x + 30, self.y + 63, 3, arcade.color.RED_DEVIL)
        arcade.draw_circle_filled(self.x + 40, self.y + 63, 3, arcade.color.RED_DEVIL)
        # Brazos del robot
        arcade.draw_lrtb_rectangle_filled(self.x+31, self.x+70,self.y+35,self.y+25, arcade.color.SILVER_LAKE_BLUE)
        arcade.draw_lrtb_rectangle_filled(self.x+51, self.x+90,self.y+50,self.y+40, arcade.color.SILVER_LAKE_BLUE)
        # Piernas del Robot
        arcade.draw_lrtb_rectangle_filled(self.x+10,self.x+20,self.y+0,self.y-10, arcade.color.SILVER_LAKE_BLUE)
        arcade.draw_lrtb_rectangle_filled(self.x+10,self.x+25,self.y-11,self.y-14, arcade.color.SILVER_LAKE_BLUE)
        arcade.draw_lrtb_rectangle_filled(self.x+28,self.x+38,self.y+0,self.y-10, arcade.color.SILVER_LAKE_BLUE)
        arcade.draw_lrtb_rectangle_filled(self.x+28,self.x+43,self.y-11,self.y-14, arcade.color.SILVER_LAKE_BLUE)
        # Dientes del Robot
        arcade.draw_triangle_filled(self.x+30,self.y+55,self.x+34,self.y+55,self.x+32,self.y+52, arcade.color.RED_DEVIL)
        arcade.draw_triangle_filled(self.x+35,self.y+55,self.x+39,self.y+55,self.x+37,self.y+52, arcade.color.RED_DEVIL)
        arcade.draw_triangle_filled(self.x+40,self.y+55,self.x+44,self.y+55,self.x+42,self.y+52, arcade.color.RED_DEVIL)
        

class RobotCazador:
    def __init__(self, x, y):
        #Posición del robot
        self.x = x
        self.y = y
        #Salud del robot
        self.salud = 100

    def dibujar(self):
        # Cuerpo del robot
        arcade.draw_rectangle_filled(self.x, self.y, 40, 50, arcade.color.DEEP_LEMON)


        # Cabeza del Robot
        arcade.draw_rectangle_filled(self.x, self.y + 30, 20, 20, arcade.color.RED_BROWN)
        
        # Antenas del robot
        arcade.draw_rectangle_filled(self.x - 5, self.y + 45,2, 10, arcade.color.SILVER, -30)
        arcade.draw_rectangle_filled(self.x + 5, self.y + 45, 2, 10, arcade.color.SILVER , 30)

        # Ojos del robot
        arcade.draw_circle_filled(self.x - 5, self.y + 30, 3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 5, self.y + 30, 3, arcade.color.BLACK)

        # Boca del robot
        arcade.draw_rectangle_filled(self.x , self.y + 20, 6, 3, arcade.color.WHITE)
        arcade.draw_rectangle_outline(self.x , self.y + 20, 7, 4, arcade.color.BLACK, 1)

        # Brazos del robot
        arcade.draw_rectangle_filled(self.x - 30, self.y + 15, 25, 10, arcade.color.DARK_BROWN, -45)
        arcade.draw_rectangle_filled(self.x + 30, self.y + 15, 25, 10, arcade.color.DARK_BROWN, 45)

        # Piernas del robot
        arcade.draw_rectangle_filled(self.x - 10, self.y - 30, 10, 20, arcade.color.DARK_BROWN)
        arcade.draw_rectangle_filled(self.x + 10, self.y - 30, 10, 20, arcade.color.DARK_BROWN)

    #El robot cazador puede caminar a una velocidad constante
    def caminar(self):
        self.x += 5

    #El robot cazador puede correr a diferentes velocidades
    def correr(self, velocidad):
        self.x += int(velocidad)

    #El robot cazador puede saltar, siempre con el mismo impulso
    def saltar(self):
        self.x += 5

    #El robot tambien puede atacar a los enemigos con 3 diferentes armas, cada una con poder de ataque diferente
    def atacar(self, arma, enemigo):
        if arma == "Pistola normal":
            potencia_ataque = 1
            enemigo.recibir_ataque(potencia_ataque)
        elif arma == "Pistola electromagnetica":
            potencia_ataque = 10
            enemigo.recibir_ataque(potencia_ataque)

    #Cuando se recibe un ataque se invoca el método que resta salud
    def recibir_ataque(self, potencia_ataque):
        self.salud -= potencia_ataque


class MiniMundo(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.PURPLE_HEART)

    def on_draw(self):
        arcade.start_render()

        robot=Robot_Prey(400,100)
        robot.dibujar()

        dron=Dron(400,400)
        dron.dibujar()

        robot1=RobotCazador(100,400)
        robot1.dibujar()

if __name__ == "__main__":
    app = MiniMundo()
    app.setup()
    arcade.run()