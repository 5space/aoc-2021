import numpy as np

# solving x^9 - x^2 - 1 = 0
roots = np.roots([1, 0, 0, 0, 0, 0, 0, -1, 0, -1])

# solving for coeffs given initial conditions
a = np.array([[root**(-k) for root in roots] for k in range(9)])
b = np.array([2, 1, 1, 1, 1, 1, 1, 1, 1])

# coefficients of closed form
x = np.linalg.solve(a, b)

# solution
def desc(n):
    return sum(x[i]*roots[i]**n for i in range(9))

with open("input.txt", "r") as file:
    nums = list(map(int, file.read().split(",")))

# these both give the right answer
# much farther and floating point precision
# would start to make it inaccurate though
print(int(sum(desc(79-n) for n in nums)))
print(int(sum(desc(255-n) for n in nums)))