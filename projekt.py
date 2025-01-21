#from cProfile import label
#from typing import final
#import importlib.resources
#from pkg_resources import non_empty_lines
#from sympy.codegen.ast import continue_, break_
#from sympy.simplify.hyperexpand import try_lerchphi

from math import ceil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

#Wszystkie zmienne dane które podawane będą z klawiatury:
#Temperatura ciała i temperatura wody (początkowe)
Tc = 0
Tw = 0
#masa ciała i objętość wody
m = 0
V = 0
#cieplo wlasciwe ciala
Cc = 0

#stałe wartosci:
#gestosc wody
rho = 1000 #kg/m^3
#cieplo wlasciwe wody
Cw = 4200 #J/kgK

def termometr(temkoncowa):
    if temkoncowa > 273.15 and temkoncowa < 373.15:
        return 0
    elif temkoncowa > 373.15:
        return 1
    else:
        return 2

def CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw):
    if termometr(To) == 1:
        V = ((m * Cc) / (rho * Cw)) * ((Tc - Tw) / (373.15 - Tw) - 1)
        return print("Woda zaczyna wrzec, masz za mala objetosc basenu! Minimalna wielkosc basenu to: ", ceil(V), "m^3")
    elif termometr(To) == 2:
        V = ((m * Cc) / (rho * Cw)) * ((Tc - Tw) / (273.15 - Tw) - 1)
        return print("Woda zaczyna krzepnac, masz za mala objetosc basenu! Minimalna wielkosc basenu to: ", ceil(V), "m^3")
    else:
        return termometr(To)


def CzyLiczbaDobraInator2(Zmienna):
    while True:
        try:
            Zmienna = float(Zmienna)
        except:
            print("Podaj liczbe:")
            break
        else:
            if Zmienna <= 0:
                print("Podaj poprawna wartosc:")
                break
            if Zmienna >0:
                return Zmienna

def CzyDobraTemperatura2(Zmienna):
    Zmienna = CzyLiczbaDobraInator2(Zmienna)
    while True:
        if Zmienna < 273.15 or Zmienna > 373.15:
            print("Woda nie ma odpowiedniej temperatury. Popraw:")
            break
        elif 273.15 <= Zmienna <= 373.15:
            return Zmienna

'''
def CzyLiczbaDobraInator(Zmienna):
    while True:
        try:
            Zmienna = float(Zmienna)
        except:
            print("Podaj liczbe:")
            Zmienna = CzyLiczbaDobraInator(input())
        else:
            Zmienna = float(Zmienna)
            break
    while Zmienna <= 0:
        print("Podaj poprawna wartosc:")
        Zmienna = CzyLiczbaDobraInator(input())
    return float(Zmienna)

def CzyDobraTemperatura(Zmienna):
    Zmienna = CzyLiczbaDobraInator(Zmienna)
    while Zmienna < 273.15 or Zmienna > 373.15:
        print("Woda nie ma odpowiedniej temperatury. Popraw:")
        Zmienna = CzyLiczbaDobraInator(input())
    return Zmienna

print("Podaj dane dla ciala:")
print("temperatura poczatkowa [K]:")
Tc = CzyLiczbaDobraInator(input())
print("masa [kg]:")
m = CzyLiczbaDobraInator(input())
print("cieplo wlasciwe [J/kgK]:")
Cc = CzyLiczbaDobraInator(input())
print("Podaj dane dla basenu:")
print("temperatura poczatkowa [K]:")
Tw = CzyDobraTemperatura(input())
print("objetosc [m^3]:")
V = CzyLiczbaDobraInator(input())
'''
Tc = 100
m = 100
Cc = 100
Tw = 300
V= 100

def Wyniki(Tc, m, Cc, Tw, V):
    if Tw > Tc:
        dQ = (Tw - Tc)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
        To = (-dQ)/(rho*V*Cw)+Tw
        dS = m*Cc*np.log(abs(To/Tc)) + rho*V*Cw*np.log(abs(To/Tw))
        if CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw) == 0:
            print("dQ[J] = ", round(dQ, 2), ",", "To[K] = ", round(To, 2), ",", "dS[J/K] = ", round(dS, 2))
            print(f"Ciepło właściwe: {Cc},Temperatura ciała: {Tc}, Masa: {m}, Temperatura wody: {Tw}, Objętość: {V}\n")
            # Wykresy
            TemCialoX = np.linspace(Tc, To, 100)
            CieploCialoY = m * Cc * (TemCialoX - Tc)

            TemWodaX = np.linspace(Tw, To, 100)
            CieploWodaY = rho * V * Cw * (-TemWodaX + Tw)
            return dQ, To, CieploCialoY, CieploWodaY, TemCialoX, TemWodaX, dS
    if Tw < Tc:
        dQ = (Tc - Tw)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
        To = (dQ)/(rho*V*Cw)+Tw
        dS =  m*Cc*np.log(abs(To/Tc)) + rho*V*Cw*np.log(abs(To/Tw))
        if CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw) == 0:
            print("dQ[J] = ", round(dQ, 2), ",", "To[K] = ", round(To, 2), ",", "dS[J/K] = ", round(dS, 2))
            print(f"Ciepło właściwe: {Cc},Temperatura ciała: {Tc}, Masa: {m}, Temperatura wody: {Tw}, Objętość: {V}\n")
            # Wykresy
            TemCialoX = np.linspace(Tc, To, 100)
            CieploCialoY = m * Cc * (-TemCialoX + Tc)
            TemWodaX = np.linspace(Tw, To, 100)
            CieploWodaY = rho * V * Cw * (TemWodaX - Tw)
            return dQ, To, CieploCialoY, CieploWodaY, TemCialoX, TemWodaX, dS
dQ1, To1, CieploCialoY, CieploWodaY, TemCialoX, TemWodaX, dS1 = Wyniki(Tc, m, Cc, Tw, V)

fig, ax = plt.subplots()
line1, = ax.plot(TemCialoX, CieploCialoY, color='y', lw=1, ls='--', label='Qciala(T)')
line2, = ax.plot(TemWodaX, CieploWodaY, color='b', lw=1, ls='--', label='Qwody(T)')
ax.legend()
ax.set_xlabel('T[K]')
ax.set_ylabel('dQ[J]')
ax.set_title('Wykres funkcji przeplywu ciepla do temperatury Q(T):')
ax.grid(True)

annotation = None
def update(operation, argument):
   global annotation, Tc, m ,Cc, Tw, V
   while True:
       try:
            if operation == 'Cc':
                Cc = CzyLiczbaDobraInator2(argument)
                dQ2, To2, CieploCialoY2, CieploWodaY2, TemCialoX2, TemWodaX2, dS2 = Wyniki(Tc, m, Cc, Tw, V)
            elif operation == 'Tc':
                Tc = CzyLiczbaDobraInator2(argument)
                dQ2, To2, CieploCialoY2, CieploWodaY2, TemCialoX2, TemWodaX2, dS2 = Wyniki(Tc, m, Cc, Tw, V)
            elif operation == 'm':
                m = CzyLiczbaDobraInator2(argument)
                dQ2, To2, CieploCialoY2, CieploWodaY2, TemCialoX2, TemWodaX2, dS2 = Wyniki(Tc, m, Cc, Tw, V)
            elif operation ==  'Tw':
                Tw = CzyDobraTemperatura2(argument)
                dQ2, To2, CieploCialoY2, CieploWodaY2, TemCialoX2, TemWodaX2, dS2 = Wyniki(Tc, m, Cc, Tw, V)
            elif operation == 'V':
                V = CzyLiczbaDobraInator2(argument)
                dQ2, To2, CieploCialoY2, CieploWodaY2, TemCialoX2, TemWodaX2, dS2 = Wyniki(Tc, m, Cc, Tw, V)
            else:
                print("Invalid operation")
            if annotation is not None:
                annotation.remove()
            line1.set_xdata(TemCialoX2)
            line1.set_ydata(CieploCialoY2)
            line2.set_xdata(TemWodaX2)
            line2.set_ydata(CieploWodaY2)
            ax.set_title(f'Wykres funkcji przeplywu ciepla do temperatury Q(T).')
            if Tw < Tc:
                ax.set_xlim([Tw - Tw / 10, Tc + Tc / 10])
            elif Tw > Tc:
                ax.set_xlim([Tc - Tc / 10, Tw + Tw / 10])
            ax.set_ylim([-dQ2 / 10, dQ2 + dQ2 / 8])
            annotation = ax.annotate(f'T[K]{To2:.0f}, dQ: {dQ2:.0f}, dS: {dS2:.0f}', xy=(To2, dQ2), xytext=(To2 - To2/9, dQ2 + dQ2 / 15),
                                     arrowprops=dict(facecolor='black', shrink=0.01),
                                     )
       except:
            break
       finally:
           break
   fig.canvas.draw_idle()
operations = ["Cc", "Tc", "m", "Tw", "V"]
text_boxes = {}
def test(operation, text):
    try:
        number = float(text)
    except ValueError:
        print("Proszę podać liczbę")
        return
    update(operation, number)

for i, operation in enumerate(operations):
    axbox = plt.axes([0.04, 0.9 - i*0.11, 0.04, 0.055])
    text_box = TextBox(axbox, f"{operation.capitalize()}: ")
    text_box.on_submit(lambda text, op=operation: test(op, text))
    text_boxes[operation] = text_box
annotation = ax.annotate(f'T[K]{To1:.0f}, dQ: {dQ1:.0f}, dS: {dS1:.0f}', xy=(To1, dQ1), xytext=(To1- To1/5,dQ1+dQ1/15),
                   arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
