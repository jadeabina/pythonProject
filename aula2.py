a= int(input('incira o primeiro valor:'))
b= int(input('incira o segundo valor:'))
soma= a+b
subtracao= a-b
multiplicacao = a*b
divisao =a/b
resto= a%b
print('Soma: {soma}. \nSubtracao: {subtracao}.'
            '\nMuntplicacao: {multiplicacao} '
            '\nDivisao: {divisao}'
            '\nResto:   {resto} '.format(soma=soma,
                                         subtracao=subtracao,
                                         resto=resto ,
                                         multiplicacao= multiplicacao,
                                         divisao=divisao))
