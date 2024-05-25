from openpyxl import *
import random
from points import *
from Buttongeneric import *

class CurrentQuestion:
    def __init__(self):
        self.he = 0
        self.ha = 0
        self.re = 0
        self.mo = 0
        self.score = 0
        self.index = 0
        self.questions = []
        self.init_questions = []
        self.mid_questions = []

    #Pega 3 perguntas da tabela infância
    def questgeninit(self):
        self.init_questions = self.get_random_questions(self.sheetinit,3)
        self.questions.extend(self.init_questions)
    
    #Pega 3 perguntas da tabela adulto
    def questgenmid(self):
        self.mid_questions = self.get_random_questions(self.sheetmid,3)
        self.questions.extend(self.mid_questions)

    #Pegando perguntas aleatórias
    def get_random_questions(self,sheet,num_questions):
        used_lines = set()
        questions = []
        
        while len(questions) <= num_questions:
            line = str(random.randint(2,9))
            #Evitar duplicata
            if line not in used_lines:
                used_lines.add(line)
                cellquest = sheet['A'+line].value
                cellansw1 = sheet['B'+line].value
                cellansw2 = sheet['D'+line].value
                questions.append((line, cellquest, cellansw1, cellansw2))
            return questions
## É NESSAS TRÊS FUNÇÕES ACIMA QUE EU ESTAVA MEXENDO AGORA. É AI QUE TA O PROBLEMA
## ATUALMENTE SE VOCÊ PERCEBER AS PERGUNTAS ESTÃO VINDO FORA DE ORDEM, ADULTO E INFANTIL AO MESMO TEMPO
## E SÓ TA GERANDO 3 PERGUNTAS, NA 3 A TELA NÃO AVANÇA MAIS
## RECOMENDO LER O CÓDIGO E DEBUGAR PARA ENTENER COMO QUE TA O FLUXO DE DADOS NO MOMENTO

    #Pega a próxima pergunta da lista
    def get_next_question(self):
        if  self.index < len(self.questions):
            question = self.questions[self.index]
            self.index += 1
            return question
        return None       

    #Carrega tabela infantil
    def load_init_table(self, filepath):
        self.tableinit = load_workbook(filepath)
        self.sheetinit = self.tableinit.active
        self.questgeninit()
    #Carrega tabela adulto
    def load_mid_table(self, filepath):
        self.tablemid = load_workbook(filepath)
        self.sheetmid = self.tablemid.active 

    
    #Perguntas finais
    def questend(self):
        print('Após mais algum tempo, você envelheceu, e agora já idoso alguns pensamentos vem a sua mente.')
        res1 = input('Como você acha foi sua vida?: ')
        res2 = input('Se arrepende de alguma escolha que foi feita durante sua vida?: ')
        res3 = input('Se pudesse mudar algo durante seu percurso o que seria?: ')
        fim = input('Você ta com 90 anos e sente uma vontade tremenda de andar de skate da forma mais radical possivel.\nSim ou não?: ')
        if fim == 'sim':
            pontos = Points(self.he, self.ha, self.re, self.mo)
            print('Parabés velho burro, você não aguentou se equilibrar em cima do skate por conta dos problemas nas articulações caiu e quebrou a coluna e agora MORREU! mas ganhou 1 ponto por ser pirado')
            print(f'Essa foi sua pontuação ao final da sua vida.: {(pontos.health+pontos.happy+pontos.relation+pontos.money)/4+1}')
        else:
            pontos = Points(self.he, self.ha, self.re, self.mo)
            print('Você teve um final de vida tranquilo, viveu tomando sua cachaçinha com sua aposentadoria ao lado da véia que amou por anos e morreu de forma tranquila enquanto dormia.')
            print(f'Essa foi sua pontuação ao final da sua vida.: {(pontos.health+pontos.happy+pontos.relation+pontos.money)/4}')

    #Inicializa a planilha e denomina ela a uma variavel
   
''' 
   tableinit = load_workbook('perguntasinicio.xlsx')
    sheetinit = tableinit.active
    questgeninit()

    print('Passou-se um tempo e você ficou mais velho.')

    #Inicializa a planilha e denomina ela a uma variavel
    tablemid = load_workbook('perguntasmeio.xlsx')
    sheetmid = tablemid.active
    questgenmid()'''