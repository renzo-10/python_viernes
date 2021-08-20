#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()

mA = Motor(Port.A)
mD = Motor(Port.D)
sencA = ColorSensor(Port.S1)
sencD = ColorSensor(Port.S2)

# Defino mis funciones
def reflexion():
    global reflexA, reflexD
    reflexA = sencA.reflection()
    reflexD = sencD.reflection()
    if reflexA <= 10:
        return "oscuroA" 
    elif reflexA >= 40:
        return "claroA"
    if reflexD <= 10:
        return "oscuroD" 
    elif reflexD >= 40:
        return "claroD"

    """def reflexion():
    global reflexA, reflexD
    reflexA = sencA.reflection()
    reflexD = sencD.reflection()
    if reflexA <= 10 or reflexD <= 10:
        return "oscuro" 
    elif reflexA >= 40 or reflexD >= 40:
        return "claro" """

def intensidadA():
    global intenA
    intenA = sencA.rgb()[1]

    if 5 <= intenA <= 15:
        return "negro"
    elif 17 <= intenA <= 22:
        return "verde"
    elif 23 <= intenA <= 80:
        return "blanco"

def intensidadD():
    global intenD
    intenD = sencD.rgb()[1]
    if 5 <= intenD <= 15:
        return "negro"
    elif 18 <= intenD <= 25:
        return "verde"
    elif 26 <= intenD <= 80:
        return "blanco"


"""def colorA():
    if intensidad() == "blancoA":
        return "BLANCO"
    elif intensidad() == "verdeA":
            return "VERDE"
    elif intensidad() == "nergroA":
        return "NEGRO"


def colorD():
    if intensidad() == "blancoD":
        return "BLANCO"
    elif intensidad() == "verdeD":
        return "VERDE"
    elif intensidad() == "nergroD":
        return "NEGRO"
"""
        
def seguidor_de_linea():
    if intensidadA() == "blanco":
        mA.run(100)
    elif intensidadA() == "negro":
        mA.run(-100)
    if intensidadD() == "blanco":
        mD.run(100)
    elif intensidadD() == "negro":
        mD.run(-100)

"""def seguidor_de_linea():
    if sencA.color() == Color.WHITE:
        mA.run(100)
    elif sencA.color() == Color.BLACK:
        mA.run(-100)  
    if sencD.color() == Color.WHITE:
        mD.run(100)
    elif sencD.color() == Color.BLACK:
        mD.run(-100)"""
#sencA 16 a 18   sencd 18 a 20
"""def VerdeDerecha():
    if intensidadA() == "verde":
        mA.run(10)
        mD.run(30)
        if intensidadA() == "verde":
            mA.stop()
            mD.run(10)
            if intensidadD() == "verde":
                mA.run_time(100, 1800, then=Stop.HOLD,wait=False)
                mD.run_time(-100, 1800, then=Stop.HOLD, wait= True)
                while intensidadA() != "negro":
                    mA.run(100)
                    mD.run(-100)
            else:
                mA.run_time(100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1000, then=Stop.HOLD, wait= True)
                mA.run_time(-100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1000, then=Stop.HOLD, wait= True)
                while intensidadD() != "negro":
                    mA.run(-100)
                    mD.run(100)"""

def VerdeDerecha():
    if sencA.color() == Color.GREEN:
        mA.run(10)
        mD.run(10)
        if intensidadA() == "verde":
            mA.stop()
            mD.run(150)
            if intensidadD() == "verde":
                mA.run_time(100, 1800, then=Stop.HOLD,wait=False)
                mD.run_time(-100, 1800, then=Stop.HOLD, wait= True)
                while sencA.color() != Color.BLACK:
                    mA.run(100)
                    mD.run(-100)
            else:
                mA.run_time(100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1000, then=Stop.HOLD, wait= True)
                mA.run_time(-100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1000, then=Stop.HOLD, wait= True)
                while sencD.color() != Color.BLACK:
                    mA.run(-100)
                    mD.run(100)

def VerdeIzquierda():
    if sencD.color() == Color.GREEN:
        mA.run(10)
        mD.run(10)
        if intensidadD() == "verde":
            mD.stop()
            mA.run(150)
            if intensidadA() == "verde":
                mA.run_time(-100, 1800, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1800, then=Stop.HOLD, wait= True)
                while sencD.color() != Color.BLACK:
                    mA.run(-100)
                    mD.run(100)
            else:
                mA.run_time(100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(100, 1000, then=Stop.HOLD, wait= True)
                mA.run_time(100, 1000, then=Stop.HOLD,wait=False)
                mD.run_time(-100, 1000, then=Stop.HOLD, wait= True)
                while sencA.color() != Color.BLACK:
                    mA.run(100)
                    mD.run(-100)

"""def doble_verde():
    global colorA, colorD
    colorA = sencA.color()
    colorD = sencD.color()
    if colorA == Color.GREEN:
        mA.run(30)
        mD.run(30)
        if intensidadA() == "verde":
            mA.stop()
            mD.run(30)
            if intensidadD() == "verde":
                mA.run_time(150, 1500, then=Stop.HOLD,wait=False)
                mD.run_time(150, 1500, then=Stop.HOLD, wait= True)
                mA.run_time(-150, 2000, then=Stop.HOLD,wait=False)
                mD.run_time(150, 2000, then=Stop.HOLD, wait= True)
                while colorD != Color.BLACK:
                    mA.run(-100)
                    mD.run(100)
                mD.run(-100)
                mA.stop()
                wait(500)
        else:
            mA.run(30)
            mD.run(30)
    elif colorD == Color.GREEN:
        mA.stop()
        mD.stop()
        if intensidadD() == "verde":
            mD.stop()
            mA.run(30)
            if (11 <= sencA.rgb()[1] <= 15):
                mD.run_time(150, 1500, then=Stop.HOLD,wait=False)
                mA.run_time(150, 1500, then=Stop.HOLD, wait= True)
                mD.run_time(-150, 2000, then=Stop.HOLD,wait=False)
                mA.run_time(150, 2000, then=Stop.HOLD, wait= True)
                while sencA.color() != Color.BLACK:
                    mD.run(-100)
                    mA.run(100)
                mA.run(-100)
                mD.stop()
                wait(500)
        else:
            mA.run(30)
            mD.run(30)
"""

def saltear_cruz():
    if (sencA.color() == Color.BLACK):
        mA.run(10)
        mD.run(50)
        if (sencD.color() == Color.BLACK):
            if intensidadA() == "negro" and intensidadD() == "negro":
                mD.run_time(100, 1800, then=Stop.HOLD,wait=False)
                mA.run_time(70, 1800, then=Stop.HOLD, wait= True)
    if (sencD.color() == Color.BLACK):
        mA.run(50)
        mD.run(10)
        if (sencA.color() == Color.BLACK):
            if intensidadA() == "negro" and intensidadD() == "negro":
                mD.run_time(70, 1800, then=Stop.HOLD,wait=False)
                mA.run_time(100, 1800, then=Stop.HOLD, wait= True)
# Write your program here.

#tomo el segundo elemento de la tupla, que devuelve la intensidad del color verde


while True:
    seguidor_de_linea()
    intensidadA()
    intensidadD()
    ev3.screen.print(str(intenA)+" "+str(intenD), sep = '')
    VerdeDerecha()
    VerdeIzquierda()
    saltear_cruz()