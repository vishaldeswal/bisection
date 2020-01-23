print("****Vishal Deswal****\n****37-IT-18****\n***03820803118***")

def precision(a,b,n):
    a=round(a,n)
    b=round(b,n)
    if a==b:
        print(a)
        exit(0)

def bisection():
    function=lambda x :x**3-2*x-5
    a=3.0
    b=2.0
    prev=0
    new=0
    while True:
        c=(a+b)/2
        new=c
        precision(new,prev,3)
        prev=new
        y=function(c)
        if y<0:
            b=c
        elif y>0:
            a=c
        else:
            print(c)

bisection()
