import time
import math
#bubble sort
def bubble_sort(arr,draw,t):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                chngcol = ['green' if k==j or k==j+1 else 'blue' for k in range(len(arr))]
                draw(arr,chngcol)
                time.sleep(t)
    
    aftersort = ['green' for i in range(len(arr))]
    draw(arr,aftersort)
            
#Quick sort
def parts(A,l,r,draw,t):
    yellow = l
    green= A[r]
    draw(A,qcolor(len(A),l,r, yellow,yellow))
    time.sleep(t)
    for j in range(l,r):
        if A[j]<green:
            draw(A,qcolor(len(A),l,r, yellow,j,True))
            time.sleep(t)
            (A[yellow],A[j])=(A[j],A[yellow])
            yellow+=1
            
        draw(A,qcolor(len(A),l,r, yellow,j))
        time.sleep(t)
            
    (A[r],A[yellow]) = (A[yellow],A[r])
    draw(A,qcolor(len(A),l,r, yellow,r,True))
    time.sleep(t)
    return (yellow)

def rec_qsort(A,l,r,draw,t): 
    if l-r<0:
        i = parts(A,l,r,draw,t)
        rec_qsort(A,l,i-1,draw,t)
        rec_qsort(A,i+1,r,draw,t)
                        
def qcolor(dataLen,l, r, yellow, x, swap = False):
    colour = []
    for i in range(dataLen):
        if i >= l and i <= r:
            colour.append('blue')
        else:
            colour.append('red')

        if i == r:
            colour[i] = 'orange'
        elif i == yellow:
            colour[i] = 'yellow'
        elif i == x:
            colour[i] = 'black'

        if swap:
            if i == yellow or i == x:
                colour[i] = 'green'

    return colour


#merge sort
def merge_sort(arr, left, right, draw, t):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, draw, t)
        merge_sort(arr, mid+1, right, draw, t)
        merge(arr, left, mid, right, draw, t)
        
        
def rec_call_merge(arr,draw,t):
    merge_sort(arr,0,len(arr)-1,draw,t)
    

def merge_color(length,left,mid,right):
    colorArr = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= mid:
                colorArr.append("yellow")
            else:
                colorArr.append("red")
        else:
            colorArr.append("blue")

    return colorArr

def merge(arr, left, middle, right, draw, t):
    draw(arr, merge_color(len(arr), left, middle, right))
    time.sleep(t)

    left_side = arr[left:middle+1]
    right_side = arr[middle+1: right+1]
    (i,j)=(0,0)

    for x in range(left, right+1):
        if i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                arr[x] = left_side[i]
                i+= 1
            else:
                arr[x] = right_side[j]
                j+= 1
        
        elif i < len(left_side):
            arr[x] = left_side[i]
            i+= 1
        else:
            arr[x]= right_side[j]
            j+= 1
    
    draw(arr, ["green" if x >= left and x <= right else "blue" for x in range(len(arr))])
    time.sleep(t)
    
#Insertion sort

def Insertion_rec_sort(seq,draw,t):
    isort(seq,len(seq),draw,t)

def isort(seq,k,draw,t): 
    if k>1:
        # ch = ['yellow' if i==k-1 else 'blue' for i in range(len(seq))]
        # draw(seq,ch)
        isort(seq,k-1,draw,t)
        insert(seq,k-1,draw,t)

def insert(seq,k,draw,t):
    pos = k
    while pos>0 and seq[pos]<seq[pos-1]:
        (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
        i_col = ['green' if k==pos-1 else 'blue' for k in range(len(seq))]
        #or k==pos-1
        draw(seq,i_col)
        time.sleep(t)
        pos = pos -1
          
#selection sort
def SelectionSort(l,draw,t):
    for i in range(len(l)):
        minpos = i
        for j in range(i,len(l)):
            if(l[j] < l[minpos]):
                minpos = j
        (l[i] , l[minpos]) = (l[minpos], l[i])
        chngcol = ['green' if k==minpos or k==i else 'blue' for k in range(len(l))]
        # else
        draw(l,chngcol)
        time.sleep(t)

#Shell sort
def ShellSort(arr,draw,t):
    n = len(arr)
    jump = n//2
    while jump > 0:
  
        for i in range(jump,n):
            temp = arr[i]
            j = i
            while  j >= jump and arr[j-jump] >temp:
                arr[j] = arr[j-jump]
                chngcol = ['green' if k==j or k==(j-jump) else 'blue' for k in range(len(arr))]
                draw(arr,chngcol)
                time.sleep(t)
                j -= jump
            arr[j] = temp
            chngcol = ['red' if k==j else 'blue' for k in range(len(arr))]
            draw(arr,chngcol)
            time.sleep(t)
        jump //= 2  
        
#heap sort        
def restore_heap(arr,n,i,draw,t):
    maxi = i  
    l = 2*i + 1     
    r = 2*i + 2
    if l < n and arr[i] < arr[l]:
        maxi = l
    if r < n and arr[maxi] < arr[r]:
        maxi = r
    if maxi != i:
        arr[i],arr[maxi] = arr[maxi],arr[i]
        chngcol = ['red' if k==n else 'blue' for k in range(len(arr))]
        draw(arr,chngcol)
        time.sleep(t)
        restore_heap(arr, n, maxi,draw,t)
       
def HeapSort(arr,draw,t):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        restore_heap(arr, n, i,draw,t)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        chngcol = ['green' if k==i or k==0 else 'blue' for k in range(len(arr))]
        draw(arr,chngcol)
        time.sleep(t)
        restore_heap(arr, i, 0,draw,t)
        
#Radix sort        
def issorted(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True

    return arr[0] <= arr[1] and issorted(arr[1:])        
       
def countingSort(arr,exp,draw,t): 
    n = len(arr) 
    
    res = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        idx = (arr[i]/exp) 
        count[int((idx)%10)] += 1
        if not issorted(arr):
            chngcol = ['green' if k==i else 'blue' for k in range(len(arr))]
            draw(arr,chngcol)
            time.sleep(t)
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0:
        idx = (arr[i]/exp) 
        res[count[int((idx)%10) ] - 1] = arr[i] 
        count[int((idx)%10)] -= 1
        i -= 1
     
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = res[i] 

def radix_Sort(arr,draw,t):
    max1 = max(arr)
    e = 1
    chngcol = ['blue' for k in range(len(arr))]
    draw(arr,chngcol)
    time.sleep(t)
    while max1/e > 0:
        countingSort(arr,e,draw,t)
        
        e *= 10
  
#bucket sort
def inserting(b,draw,t):
    for i in range(1, len(b)):
        u = b[i]
        j = i - 1
        while j >= 0 and b[j] > u:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = u 
    return b    
             

def bucketSort(arr,draw,t):
    buckets=5
    maxi = max(arr)
    mini = min(arr)
    rnge = (maxi - mini) / buckets 
    temp = []
    for i in range(buckets):
        temp.append([])
    for i in range(len(arr)):
        diff = (arr[i] - mini) / rnge - int((arr[i] - mini) / rnge)
 
        if(diff == 0 and arr[i] != mini):
            temp[int((arr[i] - mini) / rnge) - 1].append(arr[i])
 
        else:
            temp[int((arr[i] - mini) / rnge)].append(arr[i])
            
        chngcol = ['green' if k==i else 'blue' for k in range(len(arr))]
        draw(arr,chngcol)
        time.sleep(t)
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()  
    k = 0
    for L in temp:
        if L:
            for i in L:
                arr[k] = i
                k = k+1
                chngcol = ['green' if k==i or k==L else 'blue' for k in range(len(arr))]
                draw(arr,chngcol)
                time.sleep(t)
 
                
 
def cycleSort(arr,draw,t):
  r = 0
  for s in range(0, len(arr) - 1):
    item = arr[s]
    pos = s
    for i in range(s+ 1, len(arr)):
      if arr[i] < item:
        pos += 1
    if pos == s:
      continue
    while item == arr[pos]:
      pos += 1
    arr[pos], item = item, arr[pos]
    r+= 1
    chngcol = ['green'  if k==pos  else 'blue' for k in range(len(arr))]
    draw(arr,chngcol)
    time.sleep(t)
    while pos != s:
      pos = s
      for i in range(s + 1, len(arr)):
        if arr[i] < item:
          pos += 1
      while item == arr[pos]:
        pos += 1
      arr[pos], item = item, arr[pos]
      chngcol = ['red'  if k==pos  else 'blue' for k in range(len(arr))]
      draw(arr,chngcol)
      time.sleep(t)
      r+= 1

        