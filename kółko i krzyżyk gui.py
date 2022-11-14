from tkinter import *
from tkinter import messagebox

### utworzenie okna, tytuł i zablokowanie zmiany rozmiaru
okno = Tk()
okno.title('Kółko i Krzyżyk')
okno.resizable(False, False)


czy_x = True
licznik = 0
czy_koniec = False


def gra():
    ### global znaczy że te zmienne będą dostępne dla całego programu
    global p1, p2, p3, p4, p5, p6, p7, p8, p9 # zmienne przycisków
    global czy_x, licznik, czy_koniec
    czy_x = True # zmienia jaki znak będzie wyświetlany po naciśnięciu
    czy_koniec = False # sprawdza czy już koniec gry
    licznik = 0 # liczy kliknięcia
    
    ### Utworzenie 9 przycisków na grę
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

### funkcja dodająca X lub O na przycisk po naciśnięciu
def nacisniete(p):
    global czy_x, licznik
    ### jeśli pole jest puste i jest ruch X(czy_x będzie prawda) to doda na pole X
    if p['text'] == ' ' and czy_x is True:
        p['text'] = 'X'
        licznik += 1
        czy_x = False
        czy_wygrana()
    ### jeśli pole jest puste i jest ruch O(czy_x będzie fałsz) to doda na pole O
    elif p['text'] == ' ' and czy_x is False:
        p['text'] = 'O'
        licznik += 1
        czy_x = True
        czy_wygrana()
    else:
        ### jeśli pole nie niest puste wyskoczy błąd
        messagebox.showerror('Kółko i krzyżyk', 'To pole jest już zajęte\nwybierz inne pole')
        
    ### jeśli każde pole jest już zajęte i czy_koniec jest równe fałsz wyskoczy informacja o remisie
    if licznik == 9 and czy_koniec is False:
        messagebox.showinfo('Kółko i krzyżyk', 'Remis')
        gra()


def czy_wygrana():
    ### plansza wygląda tak
    ### p1 p2 p3
    ### p4 p5 p6
    ### p7 p8 p9
    ### w każdym ifie sprawdza różne przycyiski to se do tego porównajcie i ograniecie
    global czy_koniec
    ### sprawdzenie po kolei każdego warunku na wygraną 3 linie poziome, 3 pionowe i 2 po skosie, najpierw dla X później dla O
    if p1['text'] == 'X' and p2['text'] == 'X' and p3['text'] == 'X':
        # jeśli wygrana to zmienia kolor odpowiednich pól na czerwony
        p1.config(bg = 'red')
        p2.config(bg = 'red')
        p3.config(bg = 'red')
        czy_koniec = True
        ### wyskakuje informacja o zwycięzcy
        messagebox.showinfo('Kółko i krzyżyk', 'Wygrywa X!')
        gra()
        ### to samo w każdym elif
        
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

### włączenie gry
gra()
### uruchomienie pętli żeby okno pozostało włączone, sam nie wiem dokładnie co robi z neta wziąłem
okno.mainloop()
