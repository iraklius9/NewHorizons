import numpy as np
from colorama import Fore, init

init(autoreset=True)


def main():
    A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    B = np.array([[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]])

    print(Fore.MAGENTA + "Matrix A:")
    print(Fore.BLUE + np.array2string(A, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix B:")
    print(Fore.BLUE + np.array2string(B, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix A Transposed:")
    print(Fore.RED + np.array2string(A.T, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix A Rotated 90 Degrees:")
    print(Fore.GREEN + np.array2string(np.rot90(A), formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix A Rotated 180 Degrees:")
    print(Fore.GREEN + np.array2string(np.rot90(A, 2), formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix A Rotated 270 Degrees:")
    print(Fore.GREEN + np.array2string(np.rot90(A, 3), formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix A Mirrored Horizontally:")
    print(Fore.GREEN + np.array2string(np.fliplr(A), formatter={'all': lambda x: f"{x}"}))

    # -------------------------------------------------------------------------------------

    A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
    B = np.array([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]])

    AB = np.hstack((A, B))
    BA = np.hstack((B, A))
    result = np.vstack((AB, BA))

    print(Fore.MAGENTA + "Matrix A (4x5):")
    print(Fore.YELLOW + np.array2string(A, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix B (4x5):")
    print(Fore.YELLOW + np.array2string(B, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix AB (4x10) - A horizontally stacked with B:")
    print(Fore.YELLOW + np.array2string(AB, formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Matrix AB (8X5) - A vertically stacked with B:")
    print(Fore.YELLOW + np.array2string(np.vstack((A, B)), formatter={'all': lambda x: f"{x}"}))

    print(Fore.MAGENTA + "Final 8x10 Matrix - [A, B] vertically stacked with [B, A]:")
    print(Fore.YELLOW + np.array2string(result, formatter={'all': lambda x: f"{x}"}))

    B = B.T
    result = np.dot(A, B)
    print(Fore.MAGENTA + "Matrix A (4x5) multiplied by Matrix B (4x5):")
    print(Fore.YELLOW + np.array2string(result, formatter={'all': lambda x: f"{x}"}))


main()
