
#BISECTION METHOD#

    # specify your bounds xl  and xu

    # to enter no of iteration

    # pass your tol.



def bisection_method(): #a, b,iter, tol
    expr= input("f(x)=")
    a = int(input("Add a:"))
    b = int(input("Add b:"))
    iterations= int(input("Add number of iterations:"))
    tol= float(input("Add tol:"))

def f(x):
    
    return(expr)# allow use to enter any function


    if f(a)*f(b) > 0:

        #end function, no root.

        print("No root found.")

    else:

        while (b - a)/2.0 > tol:

            midpoint = (a + b)/2.0

            if f(midpoint) == 0:

                return(midpoint) #The midpoint is the x-intercept/root.

            elif f(a)*f(midpoint) < 0: # Increasing but below 0 case

                b = midpoint

            else:

                a = midpoint

        

        return(midpoint)



answer = bisection_method() #1, 4, tol=0.001,iter=4

print("answer:",round (answer,3))
