from tkinter import *
from tkinter import ttk
import random 
from sorting_algo import *
win = Tk()
win.title("Sorting Algorithms")
win.maxsize(1000,1100)
win.config(bg='black')

uif = Frame(win, width=1000, height=500,bg='lightblue')#720,200
uif.grid(row=0, column=0, padx=10,pady=5)
choose_alg = StringVar()

canvas = Canvas(win,width=980, height=600,bg='white')#740,400
canvas.grid(row=1,column=0,padx=10,pady=5)
Label(uif,text="Algorithm:  ",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky='w')

menu = ttk.Combobox(uif,textvariable = choose_alg,font="arial 10 bold",values=["Bubble Sort","Selection Sort","Merge Sort","Insertion Sort","Quick Sort","Shell Sort","Heap Sort","Radix Sort","Bucket Sort","Cycle Sort"])
#"Tim Sort"])
menu.grid(row=0,column=1,padx=1,pady=5)
menu.current(0)
arr = []

def draw(arr,col_bars):
    canvas.delete('all')
    c_ht = 600 #400
    c_w = 900   #650
    w = c_w/(len(arr)-1)
    off = 30
    space = 10
    norm = [i/max(arr) for i in arr]
    for i,h in enumerate(norm):
        ax = i*w + off + space
        ay = c_ht - h *460
        bx = (i+1)*w + off
        by = c_ht
        canvas.create_rectangle(ax,ay,bx,by,fill=col_bars[i])
        canvas.create_text(ax+2,ay,anchor=SW,text=str(arr[i]))
        
    win.update_idletasks()    
    
    
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
        
speed = Scale(uif,from_=0.1, to=2.0, length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label="Select speed(s)",font="arial 10 bold",activebackground="lightgreen")
speed.grid(row=0,column=2,padx=5,pady=5)

#size user input
size = Scale(uif,from_=3, to=30,resolution=1,orient=HORIZONTAL,label="Array Size",font="arial 10 bold",activebackground="lightgreen",length="105")
size.grid(row=1,column=0,padx=5,pady=5)

minval = Scale(uif,from_=0, to=10,resolution=1,orient=HORIZONTAL,label="Minimum Value",font="arial 10 bold",activebackground="lightgreen",length="200")
minval.grid(row=1,column=1,padx=5,pady=5,sticky='w')

maxval = Scale(uif,from_=10, to=100,resolution=1,orient=HORIZONTAL,label="Maximum Value",font="arial 10 bold",activebackground="lightgreen",length="200")
maxval.grid(row=1,column=2,padx=5,pady=5,sticky='w')
maxval.set(100)


win.mainloop()