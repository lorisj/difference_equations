import matplotlib.pyplot as plt
import numpy as np
def myplotter(plt, data1, data2, param_dict):
    out = plt.plot(data1, data2, **param_dict)
    return out
def g(c):
    r=2
    return r*c*(1-c)
def f(n):
    initCond = 0.01
    if(n==1):
        return initCond
    
    else:
        c = f(n-1)
        return g(c)
    
xarr = [f(1)]
yarr = [0]
for i in range(1,100):
    a.append(f(i))
    xarr.append(f(i))
    yarr.append(f(i))
    xarr.append(f(i))
    yarr.append(f(i+1))
    
    
    print(round(f(i), 4), end=', ')
def pt():
    ub=1
    x=np.linspace(0,ub,1000)
    
    plt.plot(x,x, label="y=xn")
    plt.plot(x,g(x), label="y=f(xn)")

    plt.xlabel('xn')
    plt.ylabel("xn+1")
    plt.legend()
    
    myplotter(plt,xarr, yarr, {"marker" : "x"})



plot1 = plt.figure(1)
plot1.set_size_inches(18.5, 10.5, forward=True)
pt()
plot2 = plt.figure(2)
plot2.set_size_inches(18.5, 10.5, forward=True)
pt()



plt2.xlim([0.56, 0.76])
plt2.ylim([0.5,0.8])




