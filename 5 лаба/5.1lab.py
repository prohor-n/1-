import timeit
from itertools import product

def algorithmic_method(K):
    result = [[]]
    for _ in range(K):
        temp = []
        for arr in result:
            for d in (0,1,2,3):
                temp.append(arr + [d])
        result = temp
    return result

def python_method(K):
    return [list(p) for p in product((0,1,2,3), repeat=K)]

def optimized_method(K, max_sum):
    candidates = [list(p) for p in product((0,1,2,3), repeat=K) if sum(p) <= max_sum]
    if not candidates:
        return []
    max_s = max(sum(arr) for arr in candidates)
    return [arr for arr in candidates if sum(arr) == max_s]

if __name__ == '__main__':
    K = 4
    max_sum = 2 * K

    alg = algorithmic_method(K)
    py = python_method(K)

    print("Алг-метод — первые 10 массивов:")
    for arr in alg[:10]:
        print(arr)
    print("\nPython-метод — первые 10 массивов:")
    for arr in py[:10]:
        print(arr)

    print(f"\nВсего массивов: {len(py)}\n")

    t_alg = timeit.timeit(lambda: algorithmic_method(K), number=100)
    t_py  = timeit.timeit(lambda: python_method(K),  number=100)
    print(f"Скорость (100 повторов): algorithmic = {t_alg:.4f}s, python = {t_py:.4f}s\n")

    optimal = optimized_method(K, max_sum)

    print("Оптимальные массивы:")
    for i, arr in enumerate(optimal, start=1):
        end_char = ", " if i % 5 != 0 and i != len(optimal) else "\n"
        print(arr, end=end_char)

    print(f"\nКоличество оптимальных массивов: {len(optimal)}")
    if optimal:
        print("Пример оптимального массива:", optimal[0] , "sum ⩽ 8")
