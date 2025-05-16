def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    
    num = int(input("digite um número: "))
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """
    import math

    texto = input("Digite alguma frase: ")
    tamanho = len(texto)
    meio = math.ceil(tamanho / 2)
    print(texto[meio:tamanho])

def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    
    num = int(input("digite um número: "))
    for i in range(1, 11): 
        resultado = num * i
        print(resultado, end=" ")


def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    pass

def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    
    lado1 = int(input("digite um lado 1: "))
    lado2 = int(input("digite um lado 2: "))
    lado3 = int(input("digite um lado 3: "))

    if lado1 == lado2 == lado3:
        print("equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("isoceles")
    else: 
        print("escaleno")       

def q6():
    
    ano = int(input("digite o ano da primeira dose: "))
    intervalo = int(input("Digite o intervalo em anos: "))

    for i in range(1, 4):
        print(ano+i*intervalo)


def q7():
    
    while True:
        num =

def q8():
    pass

def q9():
    pass

def q10():
    pass