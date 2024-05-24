from openpyxl import *
import random
from points import *

#Função para gerar as perguntas da infancia
def questgeninit():
    global ha, he, re, mo
    he, ha, re, mo = 0, 0, 0, 0
    rep = []
    x = 3
    #Busca 3 perguntas aleatorias na planilha
    for i in range(x):
        line = str(random.randint(2,9))
        cellquest = sheetinit['A'+line].value
        cellansw1 = sheetinit['B'+line].value
        cellansw2 = sheetinit['D'+line].value
        rep.append(cellquest)
        #Evitar duplicatas
        if cellquest in rep[i] == True:
            x += 1
            pass
        else:
            print(f'{cellquest}\n{cellansw1}\n{cellansw2}')
            ans = input(': ')
            if ans == '1':
                points1 = str(sheetinit['C'+line].value).split(' ')
                he += int(points1[0])*10
                ha += int(points1[1])*10
                re += int(points1[2])*10
                mo += int(points1[3])*10
                Points(he, ha, re, mo)
            else:
                points1 = str(sheetinit['E'+line].value).split(' ')
                he += int(points1[0])*10
                ha += int(points1[1])*10
                re += int(points1[2])*10
                mo += int(points1[3])*10
                Points(he, ha, re, mo) 

#Função para gerar as perguntas da fase adulta
def questgenmid():
    global ha, he, re, mo
    rep = []
    x = 3
    #Busca 3 perguntas aleatorias na planilha
    for i in range(x):
        line = str(random.randint(2,9))
        cellquest = sheetmid['A'+line].value
        cellansw1 = sheetmid['B'+line].value
        cellansw2 = sheetmid['D'+line].value
        rep.append(cellquest)
        #Evitar duplicatas
        if cellquest in rep[i] == True:
            x += 1
            pass
        else:
            print(f'{cellquest}\n{cellansw1}\n{cellansw2}')
            ans = input(': ')
            if ans == '1':
                #Sistema para contagem da pontuação pela celula a partir da escolha do jogador
                points1 = str(sheetmid['C'+line].value).split(' ')
                he += int(points1[0])*10
                ha += int(points1[1])*10
                re += int(points1[2])*10
                mo += int(points1[3])*10
                Points(he, ha, re, mo)
            else:
                #Sistema para contagem da pontuação pela celula a partir da escolha do jogador
                points1 = str(sheetmid['E'+line].value).split(' ')
                he += int(points1[0])*10
                ha += int(points1[1])*10
                re += int(points1[2])*10
                mo += int(points1[3])*10
                Points(he, ha, re, mo)

#Inicializa a planilha e denomina ela a uma variavel
tableinit = load_workbook('perguntasinicio.xlsx')
sheetinit = tableinit.active
questgeninit()

print('Passou-se um tempo e você ficou mais velho.')

#Inicializa a planilha e denomina ela a uma variavel
tablemid = load_workbook('perguntasmeio.xlsx')
sheetmid = tablemid.active
questgenmid()

#Perguntas finais
print('Após mais algum tempo, você envelheceu, e agora já idoso alguns pensamentos vem a sua mente.')
res1 = input('Como você acha foi sua vida?: ')
res2 = input('Se arrepende de alguma escolha que foi feita durante sua vida?: ')
res3 = input('Se pudesse mudar algo durante seu percurso o que seria?: ')
fim = input('Você ta com 90 anos e sente uma vontade tremenda de andar de skate da forma mais radical possivel.\nSim ou não?: ')
if fim == 'sim':
    pontos = Points(he, ha, re, mo)
    print('Parabés velho burro, você não aguentou se equilibrar em cima do skate por conta dos problemas nas articulações caiu e quebrou a coluna e agora MORREU! mas ganhou 1 ponto por ser pirado')
    print(f'Essa foi sua pontuação ao final da sua vida.: {(pontos.health+pontos.happy+pontos.relation+pontos.money)/4+1}')
else:
    pontos = Points(he, ha, re, mo)
    print('Você teve um final de vida tranquilo, viveu tomando sua cachaçinha com sua aposentadoria ao lado da véia que amou por anos e morreu de forma tranquila enquanto dormia.')
    print(f'Essa foi sua pontuação ao final da sua vida.: {(pontos.health+pontos.happy+pontos.relation+pontos.money)/4}')