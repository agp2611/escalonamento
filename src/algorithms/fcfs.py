"""
Exemplo para entendimento:

Entrada:
0 20
0 10
4 6
4 8

Total = 4 processos e 44 segundos
tempo: 0----5----10----15----20----25----30----35----44
P1:    [======================]
P2:                           [===========]
P3:                                       [======]
P4:                                              [====]
"""

def rodar_fcfs(dicionario_de_processos):

    #Inciailizando variáveis de forma limpa
    chegada: float = 0.0; inicio: float = 0.0; fim: float = 0.0; duracao: float = 0.0
    retorno_medio: float = 0.0; resposta_media: float = 0.0; espera_media: float = 0.0
    dicionario_guia: dict[int, dict] = {}

    #o sorted pega uma lista e devolve ela ordenada pela key
    #lambda é uma função de uma linha só, ela recebe cada indíce do dicionário (processos) e devolve 
    #[i][0] que é o tempo de chegada do processo, e o indíce original do dicionário, que é o id do processo, para desempatar. (tupla)
    ordem_de_execucao = sorted(dicionario_de_processos.keys(), key=lambda i: (dicionario_de_processos[i][0], i))

    #Fix: Loop percorrendo os processos NA ORDEM DE CHEGADA, não na ordem do dicionário
    for posicao, indice in enumerate(ordem_de_execucao):
        chegada, duracao = dicionario_de_processos[indice]

        #Se for o primeiro processo da ordem então ele executa primeiro
        if posicao == 0: 
            inicio = chegada
        #Se não é o primeiro, veio depois, ele só começou quando o anterior terminou
        else:
            inicio = max(fim_anterior, chegada) #Chega antes do CPU ficar livre: então início só vai ser no momento que o anterior terminar
                                                #Chega depois do CPU ficar livre:  então início só vai ser no momento que o processo atual chegar, independente do anterior ter terminado antes

        #O fim de um processo é o momento que ele começou a executar + o tempo que ele demora para executar
        fim = inicio + duracao

        #Calculando variáveis de cada processo
        dicionario_guia[indice] = {
            "chegada": chegada,
            "duracao": duracao,
            "inicio": inicio,      # quando começou a executar pela 1ª vez
            "fim": fim,            # quando terminou
            "retorno": fim-chegada,
            "resposta": inicio-chegada,
            "espera": (fim - chegada) - duracao
        }

        #Adiciona valores de cada processo em variáveis externas para calcular a média no final
        retorno_medio += dicionario_guia[indice]["retorno"]
        resposta_media += dicionario_guia[indice]["resposta"]
        espera_media += dicionario_guia[indice]["espera"]

        #Onde o processo atual terminou pra o próximo saber onde começar
        fim_anterior = fim
    
    #Calculando médias com a ajuda do do dicionario de entrada, que contém a quantidade de processos, o len retorna quantos indíces (processos) existem no dicionário
    retorno_medio /= len(dicionario_de_processos)
    resposta_media /= len(dicionario_de_processos)
    espera_media /= len(dicionario_de_processos)

    return retorno_medio, resposta_media, espera_media