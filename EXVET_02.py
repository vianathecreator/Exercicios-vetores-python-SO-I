vet_int: int = []

soma=0
contador=0

def coletavalores():
    for i in range(5):
        numero=int(input(f"Digite o {i+1}o número: "))
        vet_int.append(numero)

def mostramaiorvalor():
    maior=max(vet_int)
    menor=min(vet_int)
    print (f"Esse é menor valor: {menor} e esse é o maior: {maior}")

def verificavalor():
    global soma, contador
    for valor in vet_int:
        soma = soma + valor
        contador = contador + 1

def calculamedia():
    if contador != 0:
        media = soma/contador
        print (f"Média  dos valores: {media}")

def main():
    coletavalores()
    mostramaiorvalor()
    verificavalor()
    calculamedia()

if __name__ == "__main__":
    main()