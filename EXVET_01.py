vet_int: int = []
soma=0
contador=0
somaimp=0

def coletavalores():
    for i in range(5):
        numero=int(input(f"Digite o {i+1}o número: "))
        vet_int.append(numero)

def verificavalor():
    global soma, contador
    for valor in vet_int:
        if valor>=10 and valor<=200:
            soma = soma + valor
            contador = contador + 1

def calculamedia():
    if contador != 0:
        media = soma/contador
        print (f"Média  dos valores entre 10 e 200: {media}")
    else:
        print (f"Nao existem valores entre 10 e 200!")

def somaimpares():
    global somaimp, contador
    for valor in vet_int:
        if valor % 2 == 1:
            somaimp += valor
            contador += 0
    
    print (f"Soma dos impares: {somaimp}")

def main():
    coletavalores()
    verificavalor()
    calculamedia()
    somaimpares()

if __name__ == "__main__":
    main()