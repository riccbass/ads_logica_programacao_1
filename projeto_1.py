'''
Enunciado da fase 1

Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e referem-se aos dados de 2021 
(de janeiro a dezembro) registrados em uma cidade. 


Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.

Seu programa deve coletar os seguintes dados:

• Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.   

Para cada mês do ano, informe:  
• Temperatura máxima do mês: devem estar em Celsius, garanta que estejam dentro de um intervalo válido para temperaturas, 
tal como: -60 graus à +50 graus.   

A seguir, seu programa deve calcular e exibir:  
• Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
• Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
• Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela 
por extenso (janeiro a dezembro). 
• Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela 
por extenso (janeiro a dezembro).  

Observações gerais:

Use repetição para ler os dados e calcular as estatísticas solicitadas.
Não é necessário manter os dados lidos na memória após término do programa.    
'''

import sys #importo o sys para sair do código facilmente caso caia alguma validação com erro
import random #random apara testar algus valoes

dadosAleatorios = False 
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
qtdMeses = 12

meses[11]

tempMin = -60
tempMax = 50
tempEscaladante = 33

if len(meses) != qtdMeses:
    print('erro quantdade meses!')
    sys.exit()

tempTot = 0
qtdEscaldantes = 0

tempMaisQuente = tempMin - 1 #é arriascado deixar como um valor fixo aqui, pq se todos os valores forem menores/mariores vai manter
tempMaisFria = tempMax + 1 #é arriascado deixar como um valor fixo aqui, pq se todos os valores forem menores/mariores vai manter

mesMaisQuente = 1
mesMaisFrio = 1

for mes in range(1, qtdMeses + 1):

    if dadosAleatorios:
        tempMes = random.randint(tempMin, tempMax)
    else:
        tempMes = float(input(f'Digite a temperatura do mês {meses[mes - 1]}: ')) 

    if tempMes > tempMax: tempMes = tempMax
    if tempMes < tempMin: tempMes = tempMin

    print(f'A temperatura de {meses[mes - 1]} é {tempMes}')

    tempTot += tempMes

    if tempMes > tempEscaladante: qtdEscaldantes += 1

    if tempMes > tempMaisQuente: #maior ao invés de maior e igual faz com que o primeiro digitado seja o mais quente em caso de empate
        tempMaisQuente = tempMes
        mesMaisQuente = mes

    if tempMes < tempMaisFria: #menor ao invés de menor e igual faz com que o primeiro digitado seja o mais frio em caso de empate
        tempMaisFria = tempMes
        mesMaisFrio = mes

#Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
print(f'A temperatura média é {(tempTot / qtdMeses):.2f}') 
#Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
print(f'A quantidade de meses escaldantes é {qtdEscaldantes}') 
#Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. 
#O mês deve ser escrito na tela por extenso (janeiro a dezembro). 
print(f'Mes mais quente é {meses[mesMaisQuente - 1]} com a temperatura {tempMaisQuente}') 
#Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela 
#por extenso (janeiro a dezembro).  
print(f'Mes mais frio é {meses[mesMaisFrio - 1]} com a temperatura {tempMaisFria}') 

print('fim!')