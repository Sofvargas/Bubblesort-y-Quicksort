def bubblesort(v, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]   # intercambiar l


def main():
    n = int(input("¿Cuántos elementos desea ingresar?: "))
    v = []
    for i in range(n):
        v.append(int(input(f"v[{i + 1}] = ")))

    bubblesort(v, n)

    print("Números ordenados:")
    for i in range(n):
        print(f"v[{i + 1}] = {v[i]}")


if __name__ == "__main__":
    main()