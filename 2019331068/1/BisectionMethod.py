def bisection_method (func, a, b, max_error):

    def f(x):
        f = eval(func)
        return f

    error = abs (b - a)

    while error > max_error:
        c = (a + b) / 2

        if f(a) * f(b) >= 0:
            print("No root or more than one root!")
            quit()
        
        elif f(b) * f(c) < 0:
            a, error = c, abs(c - b)
        
        elif f(a) * f(c) < 0:
            b, error = c, abs(c - a)

        else:
            print("Something went wrong!")
            quit()

    print(f"Error = {error}")

bisection_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.05)

