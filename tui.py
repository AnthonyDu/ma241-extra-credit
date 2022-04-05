from pkg.fx import *
from pkg.integral_estimator import *
from decimal import *

def get_decimal(message):
    while True:
        try:
            return Decimal(input(message))
            break
        except InvalidOperation:
            print("Please enter a decimal number!")
            continue

if __name__ == "__main__":

    # Title
    print("")
    print("Welcome to Integral Estimator!")
    print("")

    # Rule selection
    print("(T - Trapezoidal Rule, S - Simpson's Rule)")
    while True:
        rule = input("Enter the rule you would like to use: ")
        if len(rule) != 0: rule = rule[0].upper()
        if rule == "T":
            print(f"You have chosen the Trapezoidal Rule")
            break
        if rule == "S":
            print(f"You have chosen the Simpson's Rule")
            break

    # Function input
    while True:
        fx = Fx(input("Enter a function of x: "))
        if fx.is_valid_fx():
            print("Expression parsed sucessfully!")
            print(f"You entered: {fx.get_fx()}")
            break

    # Bounds input
    while True:
        a = get_decimal("Enter the lower bound (a): ")
        b = get_decimal("Enter the upper bound (b): ")
        if b >= a: break
        else: print("b must not be equal or less than a!")

    # Subinterval input
    while True:
        n = get_decimal("Enter the number of subintervals (n): ")
        if rule == "S" and (n % 2 != 0 or n <= 0):
            print("n has to be a positive even number!")
        elif n <= 0:
            print("n has to be a positive number!")
        else: break

    # Calculate f(x) at the bounds of each subinterval
    fxs = []
    for i in range(int(n) + 1):
        x = a + (b - a) / n * i
        fxs.append(fx.evaluate_fx(x))

    # Create IntergralEstimator instance
    integration = IntegralEstimator(rule, a, b, n, fxs)

    # Output estimation results
    if rule == "T":
        print(sympy_number_to_str(integration.trap_estimate()))
    elif rule == "S":
        print(sympy_number_to_str(integration.simp_estimate()))
