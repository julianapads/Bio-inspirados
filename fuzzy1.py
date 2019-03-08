

import matplotlib.pyplot as plt
import numpy as np
column1 = {2 : "Bajo",4 : "Medio",5 : "Alto"}
column2 = {7:"Barato",9:"Estandar",0:"Costoso"}
column3 = {9:"bajo",11:"medio",12:"alto",11:"bajo",13:"medio",4:"alto",2:"alto",4:"alto",5:"alto"}
Barato = [0, 0, 30, 70]
Estandar = [25, 60, 85]
Costoso = [55, 80, 100, 100]

#Conjuntos difusos del kilometraje
Bajo = [0, 0, 50, 200]
Medio = [50, 100, 200, 300]
Alto = [200, 300, 300]

#Conjuntos difusos del precio

#Hace las lines de la Grafica, y da la ecuacion de la recta
def Up_or_Down_Ramp(a, b, t, Tipo):

    if a == b:
        b = b + 0.0001
    if Tipo == 0:
        m = 1 / (b - a)
        Slope = 1 - m * b
    elif Tipo == 1:
        m = 0
        Slope = 1
    elif Tipo == 2:
        m = -1 / (b - a)
        Slope = 1 - m * a
    Funcion_recta = t * m + Slope
    return(Funcion_recta)


def triangulo(a, b, c):
    ta = np.arange(a,b, 0.01)
    tb = np.arange(b, c, 0.01)
    Up = Up_or_Down_Ramp(a, b, ta, 0)
    Down = Up_or_Down_Ramp(b, c, tb, 2)
    return Up, Down, ta, tb


def Trapezoidal(a, b, c, d):
    ta = np.arange(a, b, 0.01)
    tb = np.arange(b, c, 0.01)
    tc = np.arange(c, d, 0.01)
    Up = Up_or_Down_Ramp(a, b, ta, 0)
    Down = Up_or_Down_Ramp(c, d, tc, 2)
    Straight = Up_or_Down_Ramp(b, c, tb, 1)
    return Up, Straight, Down, ta, tb, tc


def Graficar(Grafica):
    if Grafica == 'Precio':
        [Up_1, Down_1, ta_1, tb_1] = triangulo(25, 60, 85)
        [Up, Straight, Down, ta, tb, tc] = Trapezoidal(0,0,30,70)
        [Up_2, Straight_2, Down_2, ta_2, tb_2, tc_2] = Trapezoidal(55,80,100,100)

        plt.plot(ta_1, Up_1,'b', tb_1, Down_1, 'b')
        plt.plot(ta, Up,'r', tb, Straight, 'r', tc, Down,'r')
        plt.plot(ta_2, Up_2,'g', tb_2, Straight_2, 'g', tc_2, Down_2,'g')
        plt.xlabel('Precio (M)')
        # plt.title('About as simple as it gets, folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
    elif Grafica == 'Kilometraje':
        [Up_2, Down_2, ta_2, tb_2] = triangulo(200,300,300)
        [Up, Straight, Down, ta, tb, tc] = Trapezoidal(0,0,50,200)
        [Up_1, Straight_1, Down_1, ta_1, tb_1, tc_1] = Trapezoidal(50,100,200,300)

        plt.plot(ta_2, Up_2,'b', tb_2, Down_2, 'b')
        plt.plot(ta, Up,'r', tb, Straight, 'r', tc, Down,'r')
        plt.plot(ta_1, Up_1,'g', tb_1, Straight_1, 'g', tc_1, Down_1,'g')
        plt.xlabel('Kilometraje (Km)')
        # plt.title('About as simple as it gets, folks')
        plt.grid(True)
        plt.savefig("test.png")
        #plt.show()
        print ('Faltan los otros')


def membership_Price():
    [Up_1, Down_1, ta_1, tb_1] = triangulo(25, 60, 85)
    [Up, Straight, Down, ta, tb, tc] = Trapezoidal(0,0,30,70)
    [Up_2, Straight_2, Down_2, ta_2, tb_2, tc_2] = Trapezoidal(55,80,100,100)
    Price = float(input("precio="))
    print(Price)

    if Price >= 0 and Price <= 30:
        print('bajo, pertenece 1 ')

    if Price >= 30 and Price <= 70:
        print('bajodown')
        x=30
        for y in Down:
            x=(x+0.01)

            if round(x) == Price:
                print (y)
                break

    if (Price >= 20 and Price <= 60):
        print('medioup')
        x=20
        for y in Up_1:
            x=(x+0.01)
            if round(x) == Price:
                print (y)
                break
    if Price >= 59 and Price <= 85 :
        print('mediod')
        x=59
        for y in Down_1:
            x=(x+0.01)
            if round(x) == Price:
                print (y)

    if Price >= 55 and Price <= 79:
        print('caro1')
        x=55

        for y in Up_2:
            x=(x+0.01)
            if round(x) == Price:
                print (y)

    if Price >= 80 and Price <= 100:
        print('pertenece en 1 caro')





#    print(len(Up_1)/100)









if __name__== '__main__':
    # Conjuntos difuso de entrada PRECIO
 membership_Price()
 Graficar('Precio')
