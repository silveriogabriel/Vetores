'''Faça um programa em python que leia um vetyor de 5 posiçoes para numeros e depois um codigo enteiro. se o codigo for zero finalize o programa se for 1 mostre o vetor na ordem direta, se for 2 mostre o vetor na ordem inversa caso o codigo for diferente de 1 e 2 escreva uma mensagem informando o codigo é invalido'''

vetor = list()
for c in range(5):
    vetor.append(int(input(f'Digite o {c+1} valor:')))
while True:
    print()
    print('''#---------------------------#
 [ 1 ] Mostrar ordem direta
 [ 2 ] Mostrar vetor de inverso
#---------------------------#''')
    codigo = int(input('Digite um valor inteiro[0 para sair]: '))
    if codigo == 0:
        break
    elif codigo == 1:
        print('#---------------------------#')
        for i in vetor:
            print(f'{i}, ',end='')
    elif codigo == 2:
        print('#---------------------------#')
        for c in vetor[::-1]:
            print(F'{c}, ',end='')
    else:
        print('OPÇÃO INVALIDA!!')