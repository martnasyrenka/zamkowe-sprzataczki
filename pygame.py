#okono gry w gui:
from  tkinter import
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("350x300")
okno_gry.mainloop()

#wczytanie obrazu tła
background_image=tk.PhotoImage('lava.jpg')
background_label=tk.Label(parent, image=background_image)
background_label.place=(x=0, y=0, relwidth=1, relheight=1)
