numeros = list()
while True:
    try:
        n = int(input('digite um valor: '))
    except ValueError:
        print('Erro! digite apenas números')
        continue
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso!')
    else:
        print('valor duplicado, não posso adicionar...')
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if r not in 'SN':
        print('Erro! digite apenas S ou N')
        continue
    if r in 'N':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

