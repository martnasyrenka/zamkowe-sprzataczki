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


class Puzzel:
    def __init__(self,puzzel, x, y):
        self.puzzel=puzzel
        self.place(x,y)

    def place(self, x, y):
        self.x=x
        self.y=y
        self.puzzel.place(x=x*50, y=y*50)
    def move(self, x, y):
        self.x+=x
        self.y+=y
        self.puzzel.place(x=self.x*50, y=self.y*50)

    

class Puzzle:
    def __init__(self):
        self.p=[]
        self.selected=1

    def append(self, puzzel):
        self.p.append(puzzel)

    def zaznacz(self, numer):
        self.selected=numer

    def przesun_w_prawo(self):
        if self.selected!=-1:
            print('przesun_w_prawo()')
            self.p[self.selected].move(1,0)

    def przesun_w_lewo(self):
        if self.selected!=-1:
            print('przesun_w_lewo()')
            self.p[self.selected].move(-1,0)

    def przesun_w_dol(self):
        if self.selected!=-1:
            print('przesun_w_dol()')
            self.p[self.selected].move(0,-1)

    def przesun_w_gore(self):
        if self.selected!=-1:
            print('przesun_w_gore()')
            self.p[self.selected].move(0,1)
    
def keypress(event):
    if event.char == 'd':
        print('keypress()')
        puzzle.przesun_w_prawo()
    elif event.char == 'a':
        puzzle.przesun_w_lewo()
    elif event.char=='w':
        puzzle.przesun_w_gore()
    elif event.char=='s':
        puzzle.przesun_w_dol()
    else:
        pass

puzzle=Puzzle()
puzzle.zaznacz(2)

#wczytanie obrazów puzzli
puzzle_prawodol_zdj=PhotoImage(file='graphics/path/prawodol.png')
puzzle_prawodol=Label(okno_gry, image=puzzle_prawodol_zdj)
puzzle_prawodol.place(x=200, y=100)
puzzle.append(Puzzel(puzzle_prawodol, 4, 2))

puzzle_prawogora_zdj=PhotoImage(file='graphics/path/prawogora.png')
puzzle_prawogora=Label(okno_gry, image=puzzle_prawogora_zdj)
puzzle_prawogora.place(x=200, y=150)
puzzle.append(Puzzel(puzzle_prawogora, 4, 3))

puzzle_lewogora_zdj=PhotoImage(file='graphics/path/lewogora.png')
puzzle_lewogora=Label(okno_gry, image=puzzle_lewogora_zdj)
puzzle_lewogora.place(x=200, y=200)
puzzle.append(Puzzel(puzzle_lewogora, 4, 4))

puzzle_prosto_zdj=PhotoImage(file='graphics/path/prosto.png')
puzzle_prosto=Label(okno_gry, image=puzzle_prosto_zdj)
puzzle_prosto.place(x=200, y=250)
puzzle.append(Puzzel(puzzle_prosto, 4, 5))


puzzle_lewodol_zdj=PhotoImage(file='graphics/path/lewodol.png')
puzzle_lewodol=Label(okno_gry, image=puzzle_lewodol_zdj)
puzzle_lewodol.place(x=200, y=300)
puzzle.append(Puzzel(puzzle_lewodol, 4, 6))


#pobieranie współrzędnych kursora myszy
def motion(event):
    if do_capture:
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
okno_gry.bind('<Motion>', motion)

okno_gry.bind('d',keypress)
okno_gry.bind('a', keypress)
okno_gry.bind('w', keypress)
okno_gry.bind('s', keypress)
# wczytanie obrazów puzzli i stworzenie duszkow z poszczegolnymi puzzlami

puzzle_prawodol_zdj=PhotoImage(file='graphics/path/prawo_dol.png')
puzzle_prawodol=Label(okno_gry, image=puzzle_prawodol_zdj)
puzzle_prawodol.place(x=190, y=100)


def capture(flag):
    global do_capture
    do_capture = flag

def choose_puzzle():
    puzzle_prostoselected_zdj=PhotoImage(file='graphics/path/prosto_selected.png')
    puzzle_prosto.configure(image=puzzle_prostoselected_zdj)
    puzzle_prosto.image = puzzle_prostoselected_zdj

    puzzle_prawodolselected_zdj=PhotoImage(file='graphics/path/prawodol_selected.png')
    puzzle_prawodol.configure(image=puzzle_prawodolselected_zdj)
    puzzle_prawodol.image = puzzle_prawodolselected_zdj

    puzzle_prawogoraselected_zdj=PhotoImage(file='graphics/path/prawogora_selected.png')
    puzzle_prawogora.configure(image=puzzle_prawogoraselected_zdj)
    puzzle_prawogora.image = puzzle_prawogoraselected_zdj

    puzzle_lewodolselected_zdj=PhotoImage(file='graphics/path/lewodol_selected.png')
    puzzle_lewodol.configure(image=puzzle_lewodolselected_zdj)
    puzzle_lewodol.image = puzzle_lewodolselected_zdj

    puzzle_lewogoraselected_zdj=PhotoImage(file='graphics/path/lewogora_selected.png')
    puzzle_lewogora.configure(image=puzzle_lewogoraselected_zdj)
    puzzle_lewogora.image = puzzle_lewogoraselected_zdj


def press_puzzle():
    puzzle_prostopressed_zdj=PhotoImage(file='graphics/path/prosto_pressed.png')
    puzzle_prosto.configure(image=puzzle_prostopressed_zdj)
    puzzle_prosto.image = puzzle_prostopressed_zdj

    puzzle_prawogorapressed_zdj=PhotoImage(file='graphics/path/prawogora_pressed.png')
    puzzle_prawogora.configure(image=puzzle_prawogorapressed_zdj)
    puzzle_prawogora.image = puzzle_prawogorapressed_zdj

    puzzle_prawodolpressed_zdj=PhotoImage(file='graphics/path/prawodol_pressed.png')
    puzzle_prawodol.configure(image=puzzle_prawodolpressed_zdj)
    puzzle_prawodol.image = puzzle_prawodolpressed_zdj

    puzzle_lewogorapressed_zdj=PhotoImage(file='graphics/path/lewogora_pressed.png')
    puzzle_lewogora.configure(image=puzzle_lewogorapressed_zdj)
    puzzle_lewogora.image = puzzle_lewogorapressed_zdj

    puzzle_lewodolpressed_zdj=PhotoImage(file='graphics/path/lewodol_pressed.png')
    puzzle_lewodol.configure(image=puzzle_lewodolpressed_zdj)
    puzzle_lewodol.image = puzzle_lewodolpressed_zdj

capture(False)
okno_gry.bind("<ButtonPress-1>", lambda event: choose_puzzle())
okno_gry.bind("<ButtonRelease-1>", lambda event: capture(False))

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
        print (self.numery_puzzli)

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



#wyswietlenie okienka z instrukcje gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
