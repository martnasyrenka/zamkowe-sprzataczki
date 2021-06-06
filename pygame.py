'''___________________________________________________________________________
Wszystkie importy'''

from  tkinter import *
from tkinter import messagebox

'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry","Gra zamkowe sprzataczki dzieli sie na 3 etapy:\n W pierwszym etapie trzeba ułożyć puzzle w taki sposób aby tworzyły spójną ścieżkę. \n Następnie poruszając się za pomocą strzałek należy przejść postacią po ścieżce\n przez zamek do miejsca docelowego, zanim zapadnie się podłoga.")


'''___________________________________________________________________________
okono gry'''
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("600x600")


#wczytanie obrazu tła
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
puzzle_pionowo_zdj=PhotoImage(file='graphics/path/puzzle_pionowo.png')
puzzle_pionowo=Label(okno_gry, image=puzzle_pionowo_zdj)
#puzzle_prawodol.place(x=200, y=100) 
puzzle.append(Puzzel(puzzle_pionowo, 4, 2))

puzzle_poziomo_zdj=PhotoImage(file='graphics/path/puzzle_poziomo.png')
puzzle_poziomo=Label(okno_gry, image=puzzle_poziomo_zdj)
#puzzle_prawogora.place(x=200, y=150)
puzzle.append(Puzzel(puzzle_poziomo, 4, 3))


#puzzle_lewogora.place(x=200, y=200)
#puzzle.append(Puzzel(puzzle_lewogora, 4, 4))


#puzzle_prosto.place(x=200, y=250)
#puzzle.append(Puzzel(puzzle_prosto, 4, 5))



#puzzle_lewodol.place(x=200, y=300)
#puzzle.append(Puzzel(puzzle_lewodol, 4, 6))


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

def capture(flag):
    global do_capture
    do_capture = flag

def choose_puzzle():
    puzzle_poziomoselected_zdj=PhotoImage(file='graphics/path/puzzle_poziomo_selected.png')
    puzzle_poziomo.configure(image=puzzle_poziomoselected_zdj)
    puzzle_poziomo.image = puzzle_poziomoselected_zdj

def press_puzzle():
    puzzle_poziomopressed_zdj=PhotoImage(file='graphics/path/puzzle_poziomo_pressed.png')
    puzzle_poziomo.configure(image=puzzle_poziomopressed_zdj)
    puzzle_poziomo.image = puzzle_poziomopressed_zdj

capture(False)
okno_gry.bind("<ButtonPress-1>", lambda event: choose_puzzle())
okno_gry.bind("<ButtonRelease-1>", lambda event: capture(False))

#wczytanie grafiki protagonsty
protag_zdj=PhotoImage(file='graphics/protagonist/protag.png')
protag=Label(okno_gry, image=protag_zdj)
protag.place(x=200, y=400)



#wyswietlenie okienka z instrukcje gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
