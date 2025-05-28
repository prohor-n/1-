import numpy as np, matplotlib.pyplot as plt

def is_prime(n): return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

def load_matrix():
    A = np.loadtxt("matrix_data.txt", dtype=int)
    if A.shape[0] != A.shape[1]: exit("Матрица должна быть квадратной")
    return A

def build_F(A):
    F, n = A.copy(), A.shape[0] // 2
    E, B, C = A[:n, :n], A[:n, n:], A[n:, n:]
    primes = sum(1 for j in range(1, n, 2) for i in range(n) if is_prime(B[i, j]))
    even_row_sum = np.sum(E[::2])
    print(f"\nПростых в нечётных столбцах B: {primes}\nСумма чисел в чётных строках E: {even_row_sum}")
    if primes > even_row_sum:
        F[:n, :n], F[:n, n:] = np.fliplr(B), np.fliplr(E)
    else:
        F[:n, :n], F[n:, n:] = C.copy(), E.copy()
    return F

def compute_result(A, F, K):
    det_A, diag_F = np.linalg.det(A), np.trace(F)
    print(f"\nОпределитель A: {det_A:.2f}\nСумма диагонали F: {diag_F}")
    if np.linalg.det(F) == 0 or det_A == 0: return "ОШИБКА: матрица необратима"
    if det_A > diag_F:
        return A @ A.T - K * np.linalg.inv(F)
    else:
        G = np.tril(A)
        return (np.linalg.inv(A) + G - np.linalg.inv(F)) * K

def plot_graphs(F):
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    axs[0].plot(F.sum(axis=1)); axs[0].set_title("Сумма строк")
    axs[1].bar(range(F.shape[1]), np.median(F, axis=0)); axs[2].hist(F.flatten(), bins=10)
    for ax in axs: ax.grid(True)
    plt.tight_layout(); plt.show()

def main():
    K = int(input("Введите K: "))
    A = load_matrix(); print("\nA:\n", A)
    F = build_F(A); print("\nF:\n", F)
    R = compute_result(A, F, K); print("\nРезультат:\n", R)
    plot_graphs(F)

main()
