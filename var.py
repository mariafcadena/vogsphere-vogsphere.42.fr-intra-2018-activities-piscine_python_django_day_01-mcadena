def my_var():
    a=42;
    b="42";
    c="quarante-deux";
    d=float(42.0);
    e=True;
    f=[];
    f.append(42);
    g={42:42};
    h=(42,);
    i=set();
    lista=[a,b,c,d,e,f,g,h,i]
    types=[]
    for element in lista:
        print(str(element) + " est de type <" + str(type(element)) + ">")
    
if __name__ == '__main__':
    my_var()
