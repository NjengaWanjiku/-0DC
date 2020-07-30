def f(exp, x):

    return(exp)# allow use to enter any function

    # specify your bounds xl  and xu

    # to enter no of iteration

    # pass your tol.



def bisection_method():
    exp= input("f(x)=")
    a=(input("enter a:"))
    b=(input("enter b:"))

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



answer = bisection_method()



print("Answer:", round(answer, 3))