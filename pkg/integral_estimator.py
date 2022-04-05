class IntegralEstimator:

    def __init__(self, rule, a, b, n, fxs):
        self.rule = rule
        self.a = a
        self.b = b
        self.n = n
        self.fxs = fxs

    def trap_estimate(self):
        sum = 0
        for i in range(len(self.fxs)):
            if i == 0 or i == self.n:
                sum += self.fxs[i]
            else:
                sum += 2 * self.fxs[i]
        return (self.b - self.a) / self.n / 2 * sum

    # https://docs.sympy.org/latest/modules/core.html#add
    # this explains why the return value is of a type in classsympy.core.numbers

    def simp_estimate(self):
        sum = 0
        for i in range(len(self.fxs)):
            if i == 0 or i == self.n:
                sum += self.fxs[i]
            elif i % 2 == 0:
                sum += 2 * self.fxs[i]
            else:
                sum += 4 * self.fxs[i]
        return (self.b - self.a) / self.n / 3 * sum
