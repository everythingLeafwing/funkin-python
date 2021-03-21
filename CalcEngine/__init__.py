def Add(A, B):
    return A + B
def Subtract(A, B):
    return A - B
def Multiply(A, B):
    return A * B
def Divide(A, B):
    return A / B
def MultiplyAdd(A, multiplier, addend):
    return  (A * multiplier) + addend
def Power(Value, Exponent):
    exponent = Exponent
    value = Value
    while exponent > 1:
        value *= Value
        exponent -= 1

    return value
def Logarithm(Base, Value):
    base = Base
    value = Value

    passes = 0

    while value != base:
        value /= base
        passes += 1
    return passes + 1
def SquareRoot(Value):
    if Value == 0:
        return 0

    g = Value / 2
    g2 = Value + 1
    while (g != g2):
        n = Value / g
        g2 = g
        g = (g + n) / 2
        print(str(g) + ", " + str(g2))

    return g
def Absolute(Value):
    if Value < 0:
        return Value * -1
    return Value
def Exponent(base, exponent):
    return base ** exponent
def Minimum(Value, minimum):
    if Value < minimum:
        return minimum
    else:
        return Value
def Maximum(Value, maximum):
    if Value > maximum:
        return maximum
    else:
        return Value
def Sign(Value):
    if Value < 0:
        return 0
    else:
        return Value
def Round(Value):
    return round(Value)
def Floor(Value):
    rnd = Round(Value)

    if (rnd > Value):
        rnd -= 1
    return rnd
def Ceil(Value):
    rnd = Round(Value)

    if rnd < Value:
        rnd += 1

    return rnd
def Modulo(Value, Dividend):
    value = Value

    while value > Dividend:
        value -= Dividend
    return value
def Snap(A, B):
    a = A / B
    a = Floor(a)
    a = a * B
    return a
