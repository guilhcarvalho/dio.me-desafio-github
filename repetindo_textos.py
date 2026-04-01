'''
Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

O que aprenderemos?

Manipulação de Strings (string)
Números Inteiros (int)
Múltiplas repetições
Entrada de dados
Aproveitar as sugestões do Github Copilot
'''

string_1 = input('string: ')
integer_1 = int(input('int: '))

for i in range(integer_1):
    if i != integer_1:
        print(string_1)