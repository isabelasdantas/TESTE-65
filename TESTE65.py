resp = 'S'
cont = media = maior = menor = soma = n = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior número foi o {} e o menor foi {}.'.format(maior, menor))
