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

dadosAleatorios = False #feito apra usar dados aleatorios ao invés de input do usuario
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] #usado para 
#imprimir em tela o mês por extenso, não é necessário fazer uma lista mais complexa como [[Janeiro, 1], [Fevereiro, 2] ...] pois pegamos pela posição
qtdMeses = 12 #meses no ano, usado para validar a lista meses, o range é fazer a média

tempMin = -60 #temp mínima aceita
tempMax = 50 #tem máxima aceita
tempEscaladante = 33 #parâmetro para dizer se o meses é escaldante

if len(meses) != qtdMeses: #validação apra ver se não ficou algum mês sem separador, ex: 'Setemnbro' 'Outubro'...
    print('erro quantdade meses!')
    sys.exit()

tempTot = 0 #usado para calcular a temperatura média
qtdEscaldantes = 0 #usado para contar os meses escaldantes

tempMaisQuente = tempMin - 1 #é arriascado deixar como um valor fixo aqui, pq se todos os valores forem menores/mariores vai manter
tempMaisFria = tempMax + 1 #é arriascado deixar como um valor fixo aqui, pq se todos os valores forem menores/mariores vai manter

mesMaisQuente = 1 #mes mais quente, poderia ser 0 para ficar mais claro
mesMaisFrio = 1 #mes mais frio, poderia ser 0 para ficar mais claro

for mes in range(1, qtdMeses + 1): #início do laço, começa em 1 e vai até a qtdMeses + 1 pois o segundoa rgumento do range não é inclusivo ao contrário do primeiro

    if dadosAleatorios:
        #para não precisar o usuário digitar
        tempMes = float(random.randint(tempMin, tempMax)) #poderia pegar o aleatório como float e só cortar alguns decimais para ficar 
        #mais legível
    else:
        #para ser o usuário que digita, confrome pedido
        tempMes = input(f'Digite a temperatura do mês {meses[mes - 1]}: ')

        #teste para passar o decimal para o parâmetro brasileiro, vai aceitar o ponto tambem.e
        tempMes = tempMes.replace(',','.')
        tempMes = float(tempMes)

    if tempMes > tempMax: tempMes = tempMax #teste da temperatura máxima
    if tempMes < tempMin: tempMes = tempMin #teste da temperatua mínima

    print(f'A temperatura de {meses[mes - 1]} é {tempMes}') #mostra na tela a temperatura digitada (já corrigida dos extremos)

    tempTot += tempMes #apoio para a temperatura média

    if tempMes > tempEscaladante: qtdEscaldantes += 1 #apoio para a # de meses mto quentes

    if tempMes > tempMaisQuente: #maior ao invés de maior e igual faz com que o primeiro digitado seja o mais quente em caso de empate
        tempMaisQuente = tempMes #clausura aninhada para preencher as duas variáveis
        mesMaisQuente = mes #clausura aninhada para preencher as duas variáveis

    if tempMes < tempMaisFria: #menor ao invés de menor e igual faz com que o primeiro digitado seja o mais frio em caso de empate
        tempMaisFria = tempMes #clausura aninhada para preencher as duas variáveis
        mesMaisFrio = mes #clausura aninhada para preencher as duas variáveis

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