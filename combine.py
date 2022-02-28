from tkinter import *
from tkinter import ttk
import tkinter as tk
import random 
from sorting_algo import *
from tkinter import messagebox as mb
import threading
import heapq
import os

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.arr=[]
        self.title("Visualizing Algorithms")
        self.minsize(600,400)
        #self.wm_iconbitmap("icon.ico")
        #for windos ico format of icon and for Linux xbm format
        if "nt" == os.name:
            self.wm_iconbitmap(bitmap = "icon.ico")
        else:
            self.wm_iconbitmap(bitmap = "@icon.xbm")
        
        bl = "RoyalBlue2" 
        yll = "yellow2"
        
        style = ttk.Style()
        
        style.theme_create( "algo", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                "TNotebook.Tab": {
                    "configure": {"padding": [5, 1], "background": bl},
                    "map":       {"background": [("selected", yll)] } } } )

        style.theme_use("algo")
         
        tabs = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabs)
        tabs.add(self.tab1, text = "SORTING")
 
        self.tab2 = ttk.Frame(tabs)
        tabs.add(self.tab2, text = "BINARY SEARCH")
        
        
        self.tab3 = ttk.Frame(tabs)
        tabs.add(self.tab3,text="A* SEARCHING")
        tabs.pack()
 
        self.sorting_window()
        self.searching_window()
        self.astar_window()
 
 
    def sorting_window(self):
        uif = Frame(self.tab1, width=1000, height=500,bg='lightblue')
        uif.grid(row=0, column=0, padx=10,pady=5)
        choose_alg = StringVar()
        
        canvas = Canvas(self.tab1,width=980, height=600,bg='white')
        canvas.grid(row=1,column=0,padx=10,pady=5)
        Label(uif,text="Algorithm:  ",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky='w')
        
        menu = ttk.Combobox(uif,textvariable = choose_alg,font="arial 10 bold",values=["Bubble Sort","Selection Sort","Merge Sort","Insertion Sort","Quick Sort","Shell Sort","Heap Sort","Radix Sort","Bucket Sort","Cycle Sort"])
        menu.grid(row=0,column=1,padx=1,pady=5)
        menu.current(0)
        
        arr = []

        def draw(arr,col_bars):
            canvas.delete('all')
            c_ht = 600
            c_w = 900
            w = c_w/(len(arr)-1)
            off = 30
            space = 10
            norm = [i/max(arr) for i in arr]
            for i,h in enumerate(norm):
                ax = i*w + off + space
                ay = c_ht - h *360
                bx = (i+1)*w + off
                by = c_ht
                canvas.create_rectangle(ax,ay,bx,by,fill=col_bars[i])
                canvas.create_text(ax+2,ay,anchor=SW,text=str(arr[i]))
                
            self.tab1.update_idletasks()    
    
    
        #Create function
        def Create():
           
            print(choose_alg.get())
            a = int(minval.get())
            b = int(maxval.get())
            s = int(size.get())
            global arr
            arr = [] 
            for i in range(s):
                arr.append(random.randrange(a,b+1))
            colour = ['blue' for i in range(len(arr))]
            draw(arr,colour)
            
        
        #create array button
        Button(uif,text="Create Array",command = Create ,bg="lightgreen",font="arial 10 bold").grid(row=1, column=3, padx=3,pady=0)
        
        def start():
            global arr
            if(menu.get()=="Quick Sort"):
                rec_qsort(arr,0,len(arr)-1,draw,speed.get())
            elif (menu.get()=="Bubble Sort") :    
                bubble_sort(arr,draw,speed.get())
            elif(menu.get()=="Merge Sort"):
                rec_call_merge(arr,draw,speed.get())
            elif(menu.get()=="Insertion Sort"):
                Insertion_rec_sort(arr,draw,speed.get())
            elif(menu.get()=="Selection Sort"):
                SelectionSort(arr,draw,speed.get())
            elif(menu.get()=="Shell Sort"):
                ShellSort(arr,draw,speed.get())
            elif(menu.get()=="Heap Sort"):
                HeapSort(arr,draw,speed.get())
            elif(menu.get()=="Radix Sort"):
                radix_Sort(arr,draw,speed.get())   
            elif(menu.get()=="Bucket Sort"):
                bucketSort(arr,draw,speed.get())
            elif(menu.get()=="Cycle Sort"):
                cycleSort(arr,draw,speed.get())
                    
            draw(arr,['green' for i in range(len(arr))])    

    
    
        #start
        Button(uif,text="Start",command = start ,bg="lightgreen",font="arial 10 bold").grid(row=0, column=3, padx=5,pady=0)           
                
        speed = Scale(uif,from_=0.1, to=2.0, length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label="Select speed delay(s)",font="arial 9 bold",activebackground="lightgreen")
        speed.grid(row=0,column=2,padx=5,pady=5)
        
        #size user input
        size = Scale(uif,from_=3, to=30,resolution=1,orient=HORIZONTAL,label="Array Size",font="arial 10 bold",activebackground="lightgreen",length="105")
        size.grid(row=1,column=0,padx=5,pady=5)
        
        minval = Scale(uif,from_=0, to=10,resolution=1,orient=HORIZONTAL,label="Minimum Value",font="arial 10 bold",activebackground="lightgreen",length="200")
        minval.grid(row=1,column=1,padx=5,pady=5,sticky='w')
        
        maxval = Scale(uif,from_=10, to=100,resolution=1,orient=HORIZONTAL,label="Maximum Value",font="arial 10 bold",activebackground="lightgreen",length="200")
        maxval.grid(row=1,column=2,padx=5,pady=5,sticky='w')
        maxval.set(100)

    def searching_window(self):
        class Column:

            background = "white"
            active = "purple4"
            passive = "gray93"
            middle = "yellow"
            found = "light green"
            not_found = "red"

            def __init__(self, size, col, window):

                self.size = size
                self.but = [tk.Label(window, bg=Column.background, relief="flat", width=4, height=2)
                            for x in range(size)]

                for i in range(size):
                    self.but[i].grid(row=i, column=col, padx=1)

            def color(self, height, clr):

                for i in range(0, height):
                    self.but[self.size - i - 1].config(bg=clr)

        def binary(array, target, low, hi, cols):
            mid = (low + hi) // 2
            cols[mid].color(array[mid], Column.middle)
            time.sleep(0.5)
            if low > hi:
                for i in range(len(cols)):
                    cols[i].color(array[i], Column.not_found)
                mb.showerror("Not found!", "Element not found!")
                return -1
            if target == array[mid]:
                for i in range(low, hi + 1):
                    cols[i].color(array[i], Column.passive)
                cols[mid].color(array[mid], Column.found)
                mb.showinfo("Found!", "Element found at position {}".format(mid + 1))
                return mid
            if target > array[mid]:
                for i in range(low, mid + 1):
                    cols[i].color(array[i], Column.passive)
                time.sleep(0.5)
                return binary(array, target, mid + 1, hi, cols)
            else:
                for i in range(mid, hi + 1):
                    cols[i].color(array[i], Column.passive)
                time.sleep(0.5)
                return binary(array, target, low, mid - 1, cols)

        def find(x, cols):

            foo = int(x.get())
            t = threading.Thread(target=binary, args=(self.arr, foo, 0, len(self.arr) - 1, cols))
            t.start()

        def reset(self):

            global rows, columns
            rows = 15
            columns = 20
            self.arr = [random.randint(0, rows - 1) for i in range(columns)]
            self.arr.sort()

            for i in range(columns):
                cols[i].color(rows, Column.background)

            for i in range(columns):
                cols[i].color(self.arr[i], Column.active)

            for i in range(columns):
                tk.Label(self.tab2, bg=Column.background, relief="flat", width=4, height=2, text=self.arr[i]).grid(row=rows + 1,column=i)


        element = tk.IntVar()
        rows = 15
        columns = 20

        cols = [Column(rows, x, self.tab2) for x in range(columns)]
        self.arr = [random.randint(0, rows - 1) for i in range(columns)]
        self.arr.sort()

        for i in range(columns):
            cols[i].color(self.arr[i], Column.active)

        for i in range(columns):
            tk.Label(self.tab2, bg=Column.background, relief="flat", width=4, height=2, text=self.arr[i]).grid(row=rows + 1, column=i)


        input_box = tk.Entry(self.tab2, relief="flat")
        input_box.grid(row=rows + 2, column=2, columnspan=4, pady=2)
        search = tk.Button(self.tab2, text="Search", command=lambda: find(input_box, cols), relief="flat", bg="white")
        search.grid(row=rows + 2, column=0, columnspan=2, pady=2)

        restart = tk.Button(self.tab2, text="Restart", command=lambda: reset(self), relief="flat", bg="white")
        restart.grid(row=rows + 2, column=6, columnspan=2, pady=2)
 
    def astar_window(self):
        def run():
            import astar_search
        Boardbtn=Button(self.tab3,text="CLICK TO VISUALIZING A* SEARCH",command=run,font="arial 12 bold",bg="lightgreen")
        Boardbtn.pack()
                 
            
app = App()
app.mainloop()

