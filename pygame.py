'''___________________________________________________________________________
Wszystkie importy'''
import pygame
from game.digit_sqr import DigitSqr
from  tkinter import *
from tkinter import messagebox
import random


'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry","Gra zamkowe sprzataczki dzieli sie na 3 etapy:\n W pierwszym etapie trzeba ułożyć puzzle w taki sposób aby tworzyły spójną ścieżkę. \n Następnie poruszając się za pomocą strzałek należy przejść postacią po ścieżce\n przez zamek do miejsca docelowego, zanim zapadnie się podłoga.")


'''___________________________________________________________________________
okono gry'''
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("600x600")

'''___________________________________________________________________________
wczytywanie grafiki'''

# wczytanie obrazu tła
tlo_zamek=PhotoImage(file="graphics/background/castle.png")
tlo=Label(okno_gry, image=tlo_zamek)
tlo.place(x=0,y=0)

# wczytanie obrazów puzzli i stworzenie duszkow z poszczegolnymi puzzlami

puzzle_prawodol_zdj=PhotoImage(file='graphics/path/prawo_dol.png')
puzzle_prawodol=Label(okno_gry, image=puzzle_prawodol_zdj)
puzzle_prawodol.place(x=190, y=100)

puzzle_prawogora_zdj=PhotoImage(file='graphics/path/prawo_gora.png')
puzzle_prawogora=Label(okno_gry, image=puzzle_prawogora_zdj)
puzzle_prawogora.place(x=190, y=150)

puzzle_lewogora_zdj=PhotoImage(file='graphics/path/lewo_gora.png')
puzzle_lewogora=Label(okno_gry, image=puzzle_lewogora_zdj)
puzzle_lewogora.place(x=190, y=200)

puzzle_prosto_zdj=PhotoImage(file='graphics/path/prosto.png')
puzzle_prosto=Label(okno_gry, image=puzzle_prosto_zdj)
puzzle_prosto.place(x=190, y=250)

puzzle_lewodol_zdj=PhotoImage(file='graphics/path/lewo_dol.png')
puzzle_lewodol=Label(okno_gry, image=puzzle_lewodol_zdj)
puzzle_lewodol.place(x=190, y=300)

# wczytanie grafiki protagonsty
protag_zdj=PhotoImage(file='graphics/protagonist/protag.png')
protag=Label(okno_gry, image=protag_zdj)
protag.place(x=200, y=400)

'''___________________________________________________________________________
tworzenie klasy puzzle'''


class tworzenie_puzzli:
    def __init__(self, okienko):
        self.okno_gry = okienko
        self.numery_puzzli = []
        self.stworz_puzzle()

    def stworz_puzzle(self):
        del self.numery_puzzli[:]
        while len(self.numery_puzzli) != 12:
            numer = random.randint(1, 12)
            if numer not in self.numery_puzzli:
                self.numery_puzzli.append(numer)
        print self.numery_puzzli

        return self.numery_puzzli

    def wyswietl_puzzle(self,numery_puzzli):
        zmienna_x = 1
        zmienna_y = 1
        puzzle = []
        for numer_puzzla in numery_puzzli:
            puzzle.append(DigitSqr(self.screen, digit, 100 * counter_x, 100 * counter_y))
            counter_x += 1
            if zmienna_x % 4 == 0:
                zmienna_x = 1
                zmienna_y += 1

        return puzzle



wyswietlenie okienka z instrukcje gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
