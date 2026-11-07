def quicksort(v, izquierda, derecha):
    i = izquierda
    j = derecha
    pivote = v[(izquierda + derecha) // 2]

    while i <= j:
        while v[i] < pivote:
            i += 1
        while v[j] > pivote:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]   # intercambiar
            i += 1
            j -= 1

    if izquierda < j:
        quicksort(v, izquierda, j)
    if i < derecha:
        quicksort(v, i, derecha)


def main():
    n = int(input("¿Cuántos elementos desea ingresar?: "))
    v = []
    for i in range(n):
        v.append(int(input(f"v[{i + 1}] = ")))

    if n > 0:
        quicksort(v, 0, n - 1)

    print("Números ordenados:")
    for i in range(n):
        print(f"v[{i + 1}] = {v[i]}")


if __name__ == "__main__":
    main()
