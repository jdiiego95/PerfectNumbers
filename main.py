
def PerfectNumbers():
    NP = []

    print("Definir numeros perfectos en un rango dado")
    R1 = int(input("Escriba el numero inicial del rango: "))
    R2 = int(input("Escriba el numero final del rango: "))
    for i in range(R1, R2+1):
        n = 0
        for j in range(1, (i//2)+1):
            if i % j == 0:
                n += j
        if n == i:
            NP.append(i)
    print("los Numeros perfectos que existen entre ",
          R1, " y ", R2, " Son: ", NP)


if __name__ == "__main__":
    PerfectNumbers()
