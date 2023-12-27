from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, filedialog
from json import load, dump



def cake():
    global s2
    s2 = combo_filter.get()
    def cakem():
        global a
        a = a-1
        if a < 0 :
            btn_cake1.config(text=f"apple cake = {0}")
            btn_cakekharid.config(text=f"soma {0} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
            
        else:
            btn_cake1.config(text=f"apple cake = {a}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")

    def cakem2():
        global b
        b = b-1
        if b < 0 :
            btn_cake2.config(text=f"orange-cake = {0}")
            btn_cakekharid.config(text=f"soma {a} apple va {0} orange cake va {c} banana-cake va {d} gilas cake darid")
        else:
            btn_cake2.config(text=f"orange-cake = {b}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
    def cakem3():
        global c
        c = c-1
        if c < 0 :
            btn_cake3.config(text=f"banana-cake = {0}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {0} banana-cake va {d} gilas cake darid")
        else:
            btn_cake3.config(text=f"banana-cake = {c}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")

    def cakem4():
        global d
        d = d-1
        if d < 0 :
            btn_cake4.config(text=f"gilas-cake = {0}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {0} gilas cake darid")

        else:
            btn_cake4.config(text=f"gilas-cake =  {d}")
            btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
        

# --------------------------------------------------------------------------------------------------
    def cake1():
        global a
        a = a+1
        if a < 0 :
            a=0

            btn_cake1.config(text=f"apple cake = {a}")
        else:
            btn_cake1.config(text=f"apple cake = {a}")        
        btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
    def cake2():
        global b
        b = b+1
        if b < 0 :
            b=0

            btn_cake2.config(text=f"orange-cake = {b}")
        else:
            btn_cake2.config(text=f"orange-cake = {b}")        
        btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
    def cake3():
        global c
        c = c+1
        if c < 0 :
            c=0

            btn_cake3.config(text=f"banana-cake = {c}")
        else:
            btn_cake3.config(text=f"banana-cake = {c}")        
        btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
    def cake4():
        global d
        d = d+1
        if d < 0 :
            d=0

            btn_cake4.config(text=f"gilas-cake = {d}")
        else:
            btn_cake4.config(text=f"gilas-cake = {d}")        
        btn_cakekharid.config(text=f"soma {a} apple va {b} orange cake va {c} banana-cake va {d} gilas cake darid")
# --------------------------------------------------------------------------------------------------
    if combo_filter.get()=="cake":
        
        cake_root = Toplevel(root)
        cake_root.geometry("400x700")
        cake_root.title("Cakes")
        cake_root.config(background='#473E66')
        btn_cake_title = Label(cake_root, text='Cakes Pack', bg="white")


        btn_cake1 = Label(cake_root, text='apple-cake')
        btn_label_cake1 = Button(cake_root, text="+", command=cake1)
        btn_label_cakem = Button(cake_root, text="-", command=cakem)

        btn_cake2 = Label(cake_root, text='orange-cake')
        btn_label_cake2 = Button(cake_root, text="+", command=cake2)
        btn_label_cakem2 = Button(cake_root, text="-", command=cakem2)

        btn_cake3 = Label(cake_root, text='banana-cake')
        btn_label_cake3 = Button(cake_root, text="+", command=cake3)
        btn_label_cakem3 = Button(cake_root, text="-", command=cakem3)


        btn_cake4 = Label(cake_root, text='gilas-cake')
        btn_label_cake4 = Button(cake_root, text="+", command=cake4)
        btn_label_cakem4 = Button(cake_root, text="-", command=cakem4)

        btn_cakekharid = Button(cake_root, text=f"shoma 0 apple va 0 orange cake va 0 banana-cake va 0 gilas cake darid", command=f"shoma {cake1}apple va {cake2} orange cake va {cake3} banana-cake va {cake4} gilas cake darid")

        btn_label_cake1.place (x=10, y=150)
        btn_label_cakem.place (x=60, y=150)
        btn_cake1.place       (x=15, y=100)

        btn_label_cake2.place (x=10, y=450)
        btn_label_cakem2.place(x=60, y=450)
        btn_cake2.place       (x=12, y=400)

        btn_label_cake3.place (x=300, y=150)
        btn_label_cakem3.place(x=350, y=150)
        btn_cake3.place       (x=300, y=100)

        btn_label_cake4.place (x=300, y=450)
        btn_label_cakem4.place(x=350, y=450)
        btn_cake4.place       (x=310, y=400)

        btn_cakekharid.place(x=10, y=600)
        btn_cake_title.place(x=170,y=20)   
        root.withdraw()
        print("nice")
def drink():
    global  s1
    s1 = combo_filter.get()
    def drinkm():
        global e
        e = e-1
        if e < 0 :
            btn_drink1.config(text=f"apple cake = {0}")
            btn_drinkkharid.config(text=f"soma {0} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")
        else:
            btn_drink1.config(text=f"apple cake = {a}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")
    def drinkm2():
        global f
        f = f-1
        if f < 0 :
            btn_drink2.config(text=f"orange-cake = {0}")
            btn_drinkkharid.config(text=f"soma {e} apple va {0} orange cake va {g} banana-cake va {h} gilas cake darid")
        else:
            btn_drink2.config(text=f"orange-cake = {b}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")
    def drinkm3():
        global g
        g = g-1
        if g < 0 :
            btn_drink3.config(text=f"banana-cake = {0}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {0} banana-cake va {h} gilas cake darid")
        else:
            btn_drink3.config(text=f"banana-cake = {c}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")

    def drinkm4():
        global h
        h = h-1
        if h < 0 :
            btn_drink4.config(text=f"gilas-cake = {0}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {0} gilas cake darid")

        else:
            btn_drink4.config(text=f"gilas-cake =  {h}")
            btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")
# --------------------------------------------------------------------------------------------------
    def drink1():
        global e
        e = e+1
        if e < 0 :
            e=0

            btn_drink4.config(text=f"gilas-cake = {e}")
        else:
            btn_drink4.config(text=f"gilas-cake = {e}")        
        btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")

    def drink2():
        global f
        f = f+1
        if f < 0 :
            f=0

            btn_drink4.config(text=f"gilas-cake = {f}")
        else:
            btn_drink4.config(text=f"gilas-cake = {f}")        
        btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")

    def drink3():
        global g
        g = g+1
        if g < 0 :
            g=0

            btn_drink4.config(text=f"gilas-cake = {g}")
        else:
            btn_drink4.config(text=f"gilas-cake = {g}")        
        btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")

    def drink4():
        global h
        h = h+1
        if h < 0 :
            h=0

            btn_drink4.config(text=f"gilas-cake = {h}")
        else:
            btn_drink4.config(text=f"gilas-cake = {h}")        
        btn_drinkkharid.config(text=f"soma {e} apple va {f} orange cake va {g} banana-cake va {h} gilas cake darid")
# --------------------------------------------------------------------------------------------------
    if combo_filter.get()=="drink":
        
        drink_root = Toplevel(root)
        drink_root.geometry("400x700")
        drink_root.title("Drinks")
        drink_root.config(background='#473E66')
        btn_drink_title = Label(drink_root, text='Drink Pack', bg="white")

        btn_drink1 = Label(drink_root, text='apple-juice')
        btn_label_drink1 = Button(drink_root, text="+", command=drink1)
        btn_label_drinkm1 = Button(drink_root, text="-", command=drinkm)

        btn_drink2 = Label(drink_root  , text='orange-juice')
        btn_label_drink2 = Button(drink_root, text="+", command=drink2)
        btn_label_drinkm2 = Button(drink_root, text="-", command=drinkm2)

        btn_drink3 = Label(drink_root, text='banana-juice')
        btn_label_drink3 = Button(drink_root, text="+", command=drink3)
        btn_label_drinkm3 = Button(drink_root, text="-", command=drinkm3)

        btn_drink4 = Label(drink_root, text='cherry-juice')
        btn_label_drink4 = Button(drink_root, text="+", command=drink4)
        btn_label_drinkm4 = Button(drink_root, text="-", command=drinkm4)

        btn_drinkkharid = Button(drink_root, text=f"shoma 0 apple va 0 orange cake va 0 banana va 0 cherry darid", command=f"shoma {drink1}apple va {drink2} orange cake va {drink3} banana-cake va {drink4} gilas cake darid")


        btn_label_drink1.place(x=10, y=150)
        btn_label_drinkm1.place(x=60, y=150)
        btn_drink1.place      (x=15, y=100)

        btn_label_drink2.place(x=10, y=450)
        btn_label_drinkm2.place(x=60, y=450)
        btn_drink2.place      (x=12, y=400)

        btn_label_drink3.place(x=300, y=150)
        btn_label_drinkm3.place(x=350, y=150)
        btn_drink3.place      (x=300, y=100)

        btn_label_drink4.place(x=300, y=450)
        btn_label_drinkm4.place(x=350, y=450)
        btn_drink4.place      (x=310, y=400)

        btn_drinkkharid.place(x=20, y=600)
        btn_drink_title.place(x=170,y=20)   
        root.withdraw()
        print("nice")
def biskiet():
    global s3
    s3 = combo_filter.get()
    def biskietm():
        global i
        i = i-1
        if i < 0 :
            btn_biskiet1.config(text=f"apple-biskiet = {0}")
            btn_biskietkharid.config(text=f"soma {0} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")

        else:
            btn_biskiet1.config(text=f"apple-biskiet =  {i}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
    def biskietm2():
        global j
        j = j-1
        if j < 0 :
            btn_biskiet2.config(text=f"orange-biskiet = {0}")
            btn_biskietkharid.config(text=f"soma {i} apple va {0} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")

        else:
            btn_biskiet2.config(text=f"orange-biskiet =  {j}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
 
    def biskietm3():
        global k
        k = k-1
        if k < 0 :
            btn_biskiet3.config(text=f"banana-biskiet = {0}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {0} banana-biskiet va {0} gilas biskiet darid")

        else:
            btn_biskiet3.config(text=f"banana-cake =  {k}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
    def biskietm4():
        global l
        l = l-1
        if l < 0 :
            btn_biskiet4.config(text=f"gilas-biskiet = {0}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {0} gilas biskiet darid")

        else:
            btn_biskiet4.config(text=f"gilas-biskiet =  {l}")
            btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
   
   
   
    def biskiet1():
        global i
        i = i+1
        if i < 0 :
            i=0

            btn_biskiet1.config(text=f"apple-biskiet = {i}")
        else:
            btn_biskiet1.config(text=f"apple-biskiet = {i}")        
        btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
    def biskiet2():
        global j
        j = j+1
        if j < 0 :
            j=0

            btn_biskiet2.config(text=f"orange-biskiet = {j}")
        else:
            btn_biskiet2.config(text=f"orange-biskiet = {j}")        
        btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
    def biskiet3():
        global k
        k = k+1
        if k < 0 :
            k=0

            btn_biskiet3.config(text=f"banana-biskiet = {k}")
        else:
            btn_biskiet3.config(text=f"banana-biskiet = {k}")        
        btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")

    def biskiet4():
        global l
        l = l+1
        if l < 0 :
            l=0

            btn_biskiet4.config(text=f"gilas-biskiet = {l}")
        else:
            btn_biskiet4.config(text=f"gilas-biskiet = {l}")        
        btn_biskietkharid.config(text=f"soma {i} apple va {j} orange biskiet va {k} banana-biskiet va {l} gilas biskiet darid")
    if combo_filter.get()=="biskiet":
        
        biskiet_root = Toplevel(root)
        biskiet_root.geometry("400x700")
        biskiet_root.title("Biskiet")
        biskiet_root.config(background='#473E66')
        btn_biskiet_title = Label(biskiet_root, text='biskiet Pack', bg="white")
        btn_biskiet1 = Label(biskiet_root, text='apple-biskiet')
        btn_label_biskiet1 = Button(biskiet_root, text="+", command=biskiet1)
        btn_label_biskietm = Button(biskiet_root, text="-", command=biskietm)


        btn_biskiet2 = Label(biskiet_root  , text='orange-biskiet')
        btn_label_biskiet2 = Button(biskiet_root, text="+", command=biskiet2)
        btn_label_biskietm2 = Button(biskiet_root, text="-", command=biskietm2)


        btn_biskiet3 = Label(biskiet_root, text='banana-biskiet')
        btn_label_biskiet3 = Button(biskiet_root, text="+", command=biskiet3)
        btn_label_biskietm3 = Button(biskiet_root, text="-", command=biskietm3)


        btn_biskiet4 = Label(biskiet_root, text='gilas-biskiet')
        btn_label_biskiet4 = Button(biskiet_root, text="+", command=biskiet4)
        btn_label_biskietm4 = Button(biskiet_root, text="-", command=biskietm4)


        btn_biskietkharid = Button(biskiet_root, text=f"shoma 0 apple va 0 orange biskiet va 0 banana va 0 cherry darid", command=f"shoma {biskiet1}apple va {biskiet2} orange cake va {biskiet3} banana-cake va {biskiet4} gilas cake darid")


        btn_label_biskiet1.place(x=10, y=150)
        btn_label_biskietm.place(x=60, y=150)
        btn_biskiet1.place      (x=12, y=100)

        btn_label_biskiet2.place(x=10, y=450)
        btn_label_biskietm2.place(x=60, y=450)
        btn_biskiet2.place      (x=12, y=400)

        btn_label_biskiet3.place(x=300, y=150)
        btn_label_biskietm3.place(x=350, y=150)
        btn_biskiet3.place      (x=300, y=100)

        btn_label_biskiet4.place(x=300, y=450)
        btn_label_biskietm4.place(x=350, y=450)
        btn_biskiet4.place      (x=300, y=400)

        btn_biskietkharid.place(x=30, y=600)
        btn_biskiet_title.place(x=170,y=20)   
        root.withdraw()
        print("nice")
def tanagholat():
    global s4
    s4 = combo_filter.get()
    def tanagholatm():
        global m
        m = m-1
        if m < 0 :
            m = 0
            btn_tanagholat1.config(text=f"anjil = {0}")
            btn_tanagholatkharid.config(text=f"soma {0} anjil va {n} fandogh va {o} peste va {p} badoom darid")
        else:
            btn_tanagholat1.config(text=f"anjil = {m}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")
    def tanagholatm2():
        global n
        n = n-1
        if n < 0 :
            n = 0
            btn_tanagholat2.config(text=f"fandogh = {0}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {0} fandogh va {o} peste va {p} badoom darid")
        else:
            btn_tanagholat2.config(text=f"fandogh = {n}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")
    def tanagholatm3():
        global o
        o = o-1
        if o < 0 :
            o = 0
            btn_tanagholat3.config(text=f"peste = {0}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {0} peste va {p} badoom darid")
        else:
            btn_tanagholat3.config(text=f"peste = {o}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")

    def tanagholatm4():
        global p
        p = p-1
        if p < 0 :
            p = 0
            btn_tanagholat4.config(text=f"badoom = {0}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")

        else:
            btn_tanagholat4.config(text=f"badoom =  {p}")
            btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")

        


    def tanagholat1():
        global m
        m = m+1
        if m < 0 :
            m=0

            btn_tanagholat1.config(text=f"ajil = {m}")
        else:
            btn_tanagholat1.config(text=f"ajil = {m}")        
        btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")
    def tanagholat2():
        global n
        n = n+1
        if n < 0 :
            n=0

            btn_tanagholat2.config(text=f"fandogh  = {n}")
        else:
            btn_tanagholat2.config(text=f"fandogh = {n}")        
        btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh  va {o} peste va {p} badoom darid")
    def tanagholat3():
        global o
        o = o+1
        if o < 0 :
            o=0

            btn_tanagholat3.config(text=f"peste = {o}")
        else:
            btn_tanagholat3.config(text=f"peste = {o}")        
        btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")
    def tanagholat4():
        global p
        p = p+1
        if p < 0 :
            p=0

            btn_tanagholat4.config(text=f"badoom = {p}")
        else:
            btn_tanagholat4.config(text=f"badoom = {p}")        
        btn_tanagholatkharid.config(text=f"soma {m} anjil va {n} fandogh va {o} peste va {p} badoom darid")
    if combo_filter.get()=="tanagholat":
        
        tanagholat_root = Toplevel(root)
        tanagholat_root.geometry("400x700")
        tanagholat_root.title("tanagholat")
        tanagholat_root.config(background='#473E66')
        btn_tanagholat_title = Label(tanagholat_root, text='tanagholat Pack', bg="white")
        btn_tanagholat1 = Label(tanagholat_root, text='anjil = 0')
        btn_label_tanagholat1 = Button(tanagholat_root, text="+", command=tanagholat1)
        btn_label_tanagholatm = Button(tanagholat_root, text="-", command=tanagholatm)

        btn_tanagholat2 = Label(tanagholat_root, text='fandogh = 0')
        btn_label_tanagholat2 = Button(tanagholat_root, text="+", command=tanagholat2)
        btn_label_tanagholatm2 = Button(tanagholat_root, text="-", command=tanagholatm2)

        btn_tanagholat3 = Label(tanagholat_root, text='peste = 0')
        btn_label_tanagholat3 = Button(tanagholat_root, text="+", command=tanagholat3)
        btn_label_tanagholatm3 = Button(tanagholat_root, text="-", command=tanagholatm3)


        btn_tanagholat4 = Label(tanagholat_root, text='badoom = 0')
        btn_label_tanagholat4 = Button(tanagholat_root, text="+", command=tanagholat4)
        btn_label_tanagholatm4 = Button(tanagholat_root, text="-", command=tanagholatm4)

        btn_tanagholatkharid = Button(tanagholat_root, text=f"shoma 0 anjil va 0 fandogh va 0 peste va 0 badoom darid", command=f"shoma {tanagholat1}anjil va {tanagholat2} fandogh va {tanagholat3} peste va {tanagholat4} badoom darid")

        btn_label_tanagholat1.place (x=10, y=150)
        btn_label_tanagholatm.place (x=60, y=150)
        btn_tanagholat1.place       (x=15, y=100)

        btn_label_tanagholat2.place (x=10, y=450)
        btn_label_tanagholatm2.place(x=60, y=450)
        btn_tanagholat2.place       (x=12, y=400)

        btn_label_tanagholat3.place (x=300, y=150)
        btn_label_tanagholatm3.place(x=350, y=150)
        btn_tanagholat3.place       (x=300, y=100)

        btn_label_tanagholat4.place (x=300, y=450)
        btn_label_tanagholatm4.place(x=350, y=450)
        btn_tanagholat4.place       (x=310, y=400)

        btn_tanagholatkharid.place(x=10, y=600)
        btn_tanagholat_title.place(x=170,y=20)   
        root.withdraw()
        print("Nice")
def save():
    global s5
    if combo_filter.get()=="cake":
        combo_filter1.config(command=cake)

    elif combo_filter.get()=="biskiet":
        combo_filter1.config(command=biskiet)

    elif combo_filter.get()=="tanagholat":
        combo_filter1.config(command=tanagholat)

    elif combo_filter.get()=="drink":
        combo_filter1.config(command=drink)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
back = 0
filter = ['cake','drink','biskiet','tanagholat']

cnf_lbl = {
    'bg'   : '#473E66',
    'fg'   : '#F1916D',
    'font' : ('Times', 20),
}


root = Tk()
root.title("MAHNAS SHOP")
root.geometry("400x700")
root.resizable(0,0)
root.config(background='#473E66')

combo_filter = Combobox(root , values=filter , state='readonly')
combo_filter1 = Button(root, text="save", font=("", 10), command = save)

combo_filter.place(x=130,y=20)
combo_filter1.place(x=180,y=80)
mainloop()
