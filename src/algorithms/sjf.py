"""
Exemplo para entendimento:

Entrada:
0 20
0 10
4 6
4 8

Total = 4 processos e 44 segundos
tempo: 0----5----10----15----20----25----30----35----44
P1:                               [======================]
P2:    [==========]
P3:               [======]
P4:                      [========]
"""


def rodar_sjf(dicionario_de_processos):
    
    #inicializando as variaveis
    retorno: float = 0.0
    resposta: float = 0.0
    espera: float = 0.0
    retorno_medio: float = 0.0
    resposta_media: float = 0.0
    espera_media: float = 0.0
    inicio: float = 0.0
    fim: float = 0.0
    
    tempo_atual: float = 0.0
    processos_restantes = list(dicionario_de_processos.keys()) #Cria uma lista com as chaves do dicionario de processos, que são os IDs dos processos.
    
    #inicializando o loop que vai percorrer todos os processos restantes, sem processo definido ainda.
    while processos_restantes:
        
        #verifica quais processos chegaram e estão prontos para serem executados, ou seja, aqueles cujo tempo de chegada é menor ou igual ao tempo atual.
        processos_disponiveis = [i for i in processos_restantes if dicionario_de_processos[i][0] <= tempo_atual]
        
        #se não existir processo disponivel, então o tempo atual é atualizado para o tempo de chegada do próximo processo que ainda não chegou, e o loop continua.
        if processos_disponiveis:
            tempo_atual = min([dicionario_de_processos[i][0] for i in processos_restantes]) #pega o menor tempo de chegada dos processos restantes
            continue
        
        #define qual processo será executado, de acordo com os critérios do sjf
        #menor duracao > menor tempo de chegada > id
        processo_atual =  min(processos_disponiveis, key=lambda x: (dicionario_de_processos[x][1], dicionario_de_processos[x][0], x))
        
        #define o inicio de acordo com o tempo atual, que pode ser o fim do processo anterior ou o tempo de chegada do processo atual.
        #nessa implementação, a comparação de maximo é redundante, mas mantido para manutenibilidade futura.
        inicio = max(tempo_atual, dicionario_de_processos[processo_atual][0])
        
        #define o fim do processo atual, determinado pelo inicio = a sua duração, que é o segundo elemento da tupla do dicionario de processos.
        fim = inicio + dicionario_de_processos[processo_atual][1]
        
        #realiza os calculos de retorno, resposta e espera, de acordo com as fórmulas do sjf.
        retorno = fim - dicionario_de_processos[processo_atual][0]
        resposta = inicio - dicionario_de_processos[processo_atual][0]
        espera = retorno - dicionario_de_processos[processo_atual][1]
        
        #adiciona os valores de retorno, resposta e espera para calcular a média no final.
        retorno_medio += retorno
        resposta_media += resposta
        espera_media += espera
        
        #atualiza o tempo atual para o fim do processo atual, e remove o processo da lista de processos restantes.
        tempo_atual = fim
        processos_restantes.remove(processo_atual)
        
        
    #caso não haja processos restantes, o loop termina e as médias são calculadas.
    #dividindo os valores totais de retorno, resposta e espera pelo número de processos, que é o tamanho do dicionário de processos.
    retorno_medio /= len(dicionario_de_processos)
    resposta_media /= len(dicionario_de_processos)
    espera_media /= len(dicionario_de_processos)
    
    #retorna as médias de retorno, resposta e espera.
    return retorno_medio, resposta_media, espera_media
