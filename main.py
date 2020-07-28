def f(x):

    return(x**3 - 20)# allow use to enter any function

    # specify your bounds xl  and xu

    # to enter no of iteration

    # pass your tol.



def bisection_method(a, b,iter, tol):

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



answer = bisection_method(1, 4, tol=0.001,iter=4)



print("Answer:", round(answer, 3))