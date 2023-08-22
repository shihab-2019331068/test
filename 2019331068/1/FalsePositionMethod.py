def fp_method (func, a, b, max_error):

    def f(x):
        f = eval(func)
        return f

    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    error = c - c_before

    while error > max_error:

        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            print("No root or more than one root!")
            quit()
        
        elif f(c_after) * f(a) < 0:
            error = abs (c_after - b)
            b = c_after
            i = i + 1
        
        elif f(c_after) * f(b) < 0:
            error = abs (c_after - a)
            a = c_after
            i = i + 1

        else:
            print("Something went wrong!")
            quit()

    print(f"Error = {error}, after {i} Iterations")
    print(f"The root can be approx. found at {c_after}")


fp_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.05)
