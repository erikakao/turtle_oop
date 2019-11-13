
import random
from turtle import Turtle, Screen
import tkinter

class MyTurtle(Turtle):
    
    speedwert = 0
    
    def __init__(self, bez): #Konstruktormethode
        
        Turtle.__init__(self,bez)
        self.bezeichnung = bez
        
    #def __str__(self):
    #    return Turtle.__str__(self) + ": " + str(self.speedwert)
    #def __str__(self):
    #    return self.bezeichnung + ": " +str(self.speedwert)
    
    def randomspeed(self):
        self.speedwert = self.speedwert + random.randint(1,6)

    def ausgabe(self):
        
        if self.speedwert == 6:
            self.write(self.bezeichnung+": "+str(self.speedwert)+" HURRA!")
        else:
            self.write(self.bezeichnung+": "+str(self.speedwert))


#MyTurtle ist eine abgeleitete Klasse
#speedwert ist eine Eigenschaft, randomspeed und ausgabe sind Methoden


def full_track_crawl(turtle, shortside, longside):
    speed = turtle.speedwert
    turtle.pendown()

    for j in range (2):
        for i in range(0, int(shortside), speed):
            turtle.forward(speed)
            yield(0)
        turtle.left(90)
        for i in range(0, int(longside), speed):
            turtle.forward(speed)
            yield(0)
        turtle.left(90)

    turtle.penup()
    
#das Turtle dreht schneller, wenn es mit der Schrittlänge nicht mehr ausgeht


# set the track

def drawTrack(width,height):
    shortside = .9* width / 3
    longside = .9 * height

    #screen.setup(shortside * 3 + 80, longside + 40)

    turtle1.setposition(-1.5*shortside - 20, -longside / 2)
    turtle1.ausgabe()
    
    turtle2.setposition(-shortside/2, -longside / 2)
    turtle2.ausgabe()
    
    turtle3.setposition(shortside/2 +20, -longside / 2)
    turtle3.ausgabe()

    generator1 = full_track_crawl(turtle1, shortside, longside)
    generator2 = full_track_crawl(turtle2, shortside, longside)
    generator3 = full_track_crawl(turtle3, shortside, longside)

    while (next(generator1, 1) + next(generator2, 1) + next(generator3, 1) < 3):
        pass

#yield ist solange 0, bis das Turtle seine ganze Strecke zu Ende gelaufen hat,
#dann springt die next Wert auf 1,
#wenn jedes Turtle vollendet hat 1+1+1=3 while loop ende

screen = Screen()
screen.title("Run, Turtle, Run!")
screen.bgcolor("lightgreen")
#screen.screensize()
percent = screen.numinput("Window size",
                           "Prozent angeben:",
                           default=75, minval=50, maxval=100)/100
screen.setup(width = percent, height = percent)
#screen Zahlangabe, default ist voreingestellt,
#angegebene Zahl wird mit minval und maxval verglichen,
#wenn ausserhalb den Grenzen, Fehlermeldung, Neuangabe


#Ermittung der Screengröße, Fenster wird nachher destroyed
root = tkinter.Tk()
width_pi = root.winfo_screenwidth() *percent
height_pi = root.winfo_screenheight() *percent
root.destroy()



#definition von Turtle

turtle1 = MyTurtle("Wafa")
turtle1.shape('turtle')
turtle1.color('green')
turtle1.randomspeed()  # = 3
turtle1.penup()

turtle2 = MyTurtle("Erika")
turtle2.shape('turtle')
turtle2.color('blue')
turtle2.randomspeed()  # "slow" (3) < 4 < "normal" (6)
turtle2.penup()

turtle3=MyTurtle("Anna")
turtle3.shape('turtle')
turtle3.color('red')
turtle3.randomspeed()
turtle3.penup()

print(turtle1)
drawTrack(width_pi,height_pi)

screen.exitonclick()
