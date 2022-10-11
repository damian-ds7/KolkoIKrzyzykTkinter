from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title('Kółko i Krzyżyk')
okno.resizable(False, False)


menu = Menu(okno)
okno.config(menu = menu)
czy_x = True
licznik = 0
czy_koniec = False


def gra():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9
    global czy_x, licznik, czy_koniec
    czy_x = True
    czy_koniec = False
    licznik = 0

    p1 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p1))
    p1.grid(row = 0, column = 0)

    p2 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p2))
    p2.grid(row = 0, column = 1)

    p3 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p3))
    p3.grid(row = 0, column = 2)

    p4 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p4))
    p4.grid(row = 1, column = 0)

    p5 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p5))
    p5.grid(row = 1, column = 1)

    p6 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p6))
    p6.grid(row = 1, column = 2)

    p7 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p7))
    p7.grid(row = 2, column = 0)

    p8 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p8))
    p8.grid(row = 2, column = 1)

    p9 = Button(okno, text = ' ', font = ('Calibri', 21), height = 3, width = 8, bg = 'SystemButtonFace',
                command = lambda: nacisniete(p9))
    p9.grid(row = 2, column = 2)


def nacisniete(p):
    global czy_x, licznik

    if p['text'] == ' ' and czy_x is True:
        p['text'] = 'X'
        licznik += 1
        czy_x = False
        czy_wygrana()
    elif p['text'] == ' ' and czy_x is False:
        p['text'] = 'O'
        licznik += 1
        czy_x = True
        czy_wygrana()
    else:
        messagebox.showerror('Kółko i krzyżyk', 'To pole jest już zajęte\nwybierz inne pole')
    if licznik == 9 and czy_koniec is False:
        messagebox.showinfo('Kółko i krzyżyk', 'Remis')
        gra()


def czy_wygrana():
    global czy_koniec
    if p1['text'] == 'X' and p2['text'] == 'X' and p3['text'] == 'X':
        p1.config(bg = 'red')
        p2.config(bg = 'red')
        p3.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p4['text'] == 'X' and p5['text'] == 'X' and p6['text'] == 'X':
        p4.config(bg = 'red')
        p5.config(bg = 'red')
        p6.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p7['text'] == 'X' and p8['text'] == 'X' and p9['text'] == 'X':
        p7.config(bg = 'red')
        p8.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p1['text'] == 'X' and p4['text'] == 'X' and p7['text'] == 'X':
        p1.config(bg = 'red')
        p4.config(bg = 'red')
        p7.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p2['text'] == 'X' and p5['text'] == 'X' and p8['text'] == 'X':
        p2.config(bg = 'red')
        p5.config(bg = 'red')
        p8.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p3['text'] == 'X' and p6['text'] == 'X' and p9['text'] == 'X':
        p3.config(bg = 'red')
        p6.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p1['text'] == 'X' and p5['text'] == 'X' and p9['text'] == 'X':
        p1.config(bg = 'red')
        p5.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p3['text'] == 'X' and p5['text'] == 'X' and p7['text'] == 'X':
        p3.config(bg = 'red')
        p5.config(bg = 'red')
        p7.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
    elif p1['text'] == 'O' and p2['text'] == 'O' and p3['text'] == 'O':
        p1.config(bg = 'red')
        p2.config(bg = 'red')
        p3.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p4['text'] == 'O' and p5['text'] == 'O' and p6['text'] == 'O':
        p4.config(bg = 'red')
        p5.config(bg = 'red')
        p6.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p7['text'] == 'O' and p8['text'] == 'O' and p9['text'] == 'O':
        p7.config(bg = 'red')
        p8.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p1['text'] == 'O' and p4['text'] == 'O' and p7['text'] == 'O':
        p1.config(bg = 'red')
        p4.config(bg = 'red')
        p7.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p2['text'] == 'O' and p5['text'] == 'O' and p8['text'] == 'O':
        p2.config(bg = 'red')
        p5.config(bg = 'red')
        p8.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p3['text'] == 'O' and p6['text'] == 'O' and p9['text'] == 'O':
        p3.config(bg = 'red')
        p6.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p1['text'] == 'O' and p5['text'] == 'O' and p9['text'] == 'O':
        p1.config(bg = 'red')
        p5.config(bg = 'red')
        p9.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()
    elif p3['text'] == 'O' and p5['text'] == 'O' and p7['text'] == 'O':
        p3.config(bg = 'red')
        p5.config(bg = 'red')
        p7.config(bg = 'red')
        czy_koniec = True
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa O!')
        gra()


opcje_menu = Menu(menu, tearoff = False)
menu.add_cascade(label = 'Opcje', menu = opcje_menu, )
opcje_menu.add_command(label = 'Wyczyść planszę', command = gra)
gra()
okno.mainloop()
