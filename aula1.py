'''Peça para o usuário inserir via input os seguintes dados.nome , sobrenome , idade (em inteiro) , Escola e numero de telefone. 
preciso de uma condição de que se o usuário for menor de idade ele print que e de menor e precisa do documento da mae ai 
entra mais um input para saber o nome da mae : nome e sobre nome. caso não seja menor de idade 
ele mostre para o usuário :print(nome sobrenome escola telefone)'''

nome = input('Nome ')
sobrenome = input('Sobrenome ')
idade = int(input('Idade '))
if idade < 18:
    print('Vc é menor de idade, precisa do documento da mae')
    nome_mae = input('Nome da mãe')
    sobrenome_mae = input('Sobrenome ')
escola = input('Escola ')
numero = input('Numero tel ')



print(nome,'\n',sobrenome,'\n',escola,'\n',numero)