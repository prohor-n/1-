import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

def F_recursive(n: int) -> float:
    if n <= 5:
        return 10
    if n <= 12:
        return F_recursive(n-2) - F_recursive(n-1)
    sign = 1 if n % 2 == 0 else -1
    return sign*(5*F_recursive(n-1) - 7*F_recursive(n-2) + F_recursive(n//5)) / math.factorial(2*n)

def F_iterative(n):
    F = [0]*(n+1)
    factorial_cache = 1
    for i in range(n+1):
        if i >= 1:
            factorial_cache *= (2*i - 1)*(2*i)
        if i <= 5:
            F[i] = 10
        elif i <= 12:
            F[i] = F[i-2] - F[i-1]
        else:
            sign = 1 if i % 2 == 0 else -1
            F[i] = sign * (5*F[i-1] - 7*F[i-2] + F[i//5]) / factorial_cache
    return F[n]

results = [(n,
            timeit.timeit(lambda n=n: F_recursive(n), number=10),
            timeit.timeit(lambda n=n: F_iterative(n), number=10))
           for n in range(2, 21)]

df = pd.DataFrame(results, columns=['n', 'Recursive Time (s)', 'Iterative Time (s)'])
print(df.to_string(index=False))

plt.figure(figsize=(8,5))
plt.plot(df['n'], df['Recursive Time (s)'], '--o', label='Recursive')
plt.plot(df['n'], df['Iterative Time (s)'], '-o', label='Iterative')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Сравнение времени: рекурсия vs итерация')
plt.legend()
plt.grid(True)
plt.show()
