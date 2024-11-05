globalvar = 1

def f1():
    global glabalvar
    globalvar3 = globalvar +1

    print (globalvar)
    print (globalvar3)

f1()
print (globalvar)