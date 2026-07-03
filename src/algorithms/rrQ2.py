"""
Exemplo para entendimento:

Entrada:
0 20
0 10
4 6
4 8

Total = 4 processos e 44 segundos (quantum = 2)
tempo: 0--2--4--6--8-10-12-14-16-18-20-22-24-26-28-30-32-34-36-38-40-42-44

   P1: [==]        [==]        [==]        [==]        [==]  [===========](FIM)    
   P2:    [==]        [==]        [==]        [==]        [==](FIM)
   P3:       [==]        [==]        [==](FIM)   [==]
   P4:          [==]        [==]        [==]        [==](FIM)  
"""

def rodar_rrQ2(dicionario_de_processos):
#A cada execução do processo é tirado 2 segundos até ele acabar (RRq2)

    #Variáveis do RoundRobin:
    quantum = 2
    tempo_atual: float = 0.0 #relogio de tempo atual
    
    #Inciailizando variáveis de forma limpa
    chegada: float = 0.0; duracao: float = 0.0
    retorno_medio: float = 0.0; resposta_media: float = 0.0; espera_media: float = 0.0
    dicionario_guia: dict[int, dict] = {}

    #o sorted pega uma lista e devolve ela ordenada pela key
    #lambda é uma função de uma linha só, ela recebe cada indíce do dicionário (processos) e devolve 
    #[i][0] que é o tempo de chegada do processo, e o indíce original do dicionário, que é o id do processo, para desempatar. (tupla)
    ordem_de_chegada = sorted(dicionario_de_processos.keys(), key=lambda i: (dicionario_de_processos[i][0], i))
                                                                            #{indice: (chegada, duracao)}
                                                                            
    #Fila de processos disputando a CPU
    fila_prontos = []

    for indice, (chegada, duracao) in dicionario_de_processos.items():
        dicionario_guia[indice] = {
            "chegada": chegada,
            "duracao": duracao,    # Quanto tempo leva
            "restante": duracao,   # Vai sendo consumido a cada quantum
            "inicio": None,        # Registra quando executa pela 1ª vez 
            "fim": None,           # Registra quando zera restante
            "retorno": None,       # Calcula depois
            "resposta": None,      # Calcula depois
            "espera": None         # Calcula depois
        }

    #Enquanto existir processo não finalizado (na fila OU esperando chegar), continua rodando
    while len(fila_prontos) > 0 or len(ordem_de_chegada) > 0:

        #Enquanto existir processo e ele estiver no tempo atual
        while len(ordem_de_chegada) > 0 and dicionario_de_processos[ ordem_de_chegada[0] ][0] <= tempo_atual:
                                                                   #o ordem_de_chegada[0] é o primeiro classificado pelo sorted e o indíce 0 dele é o TC

            proximo_indice = ordem_de_chegada.pop(0)  #que vai entrar na fila de prontos agora  (tira e devolve o elemento que está na posição 0 da lista)           
            fila_prontos.append(proximo_indice) #joga no final da fila de prontos

        #Se ninguém chegou ainda, tempo avança para o processo com menor TC
        if len(fila_prontos) == 0:
            tempo_atual = dicionario_de_processos[ ordem_de_chegada[0] ][0]
            continue
        
        #Entra na fila de prontos
        processo_atual = fila_prontos.pop(0)

        #Se é a 1ª vez que ele roda, marca o início
        if dicionario_guia[processo_atual]["inicio"] is None:
            dicionario_guia[processo_atual]["inicio"] = tempo_atual

        #Calcula o que falta tirar do processo atual (não deixar negativo)
        tempo_de_execucao = min(quantum, dicionario_guia[processo_atual]["restante"])

        #Tira o que calculou
        dicionario_guia[processo_atual]["restante"] -= tempo_de_execucao

        #Se tirou segundos adiciona esses segundos gastos no tempo total, avançando ele.
        tempo_atual += tempo_de_execucao

        #Checa se chegou mais alguém durante essa execução, ANTES de decidir o destino do processo_atual
        while len(ordem_de_chegada) > 0 and dicionario_de_processos[ ordem_de_chegada[0] ][0] <= tempo_atual:
            proximo_indice = ordem_de_chegada.pop(0)
            fila_prontos.append(proximo_indice)

        #Se zerou, marca o tempo que zerou e registra as métricas de retorno, resposta e espera
        if dicionario_guia[processo_atual]["restante"] == 0:
            dicionario_guia[processo_atual]["fim"] = tempo_atual

            dicionario_guia[processo_atual]["retorno"] = dicionario_guia[processo_atual]["fim"] - dicionario_guia[processo_atual]["chegada"]
            dicionario_guia[processo_atual]["resposta"] = dicionario_guia[processo_atual]["inicio"] - dicionario_guia[processo_atual]["chegada"]
            dicionario_guia[processo_atual]["espera"] = dicionario_guia[processo_atual]["retorno"] - dicionario_guia[processo_atual]["duracao"]
            
            retorno_medio += dicionario_guia[processo_atual]["retorno"]
            resposta_media += dicionario_guia[processo_atual]["resposta"]
            espera_media += dicionario_guia[processo_atual]["espera"]
        
        #Se não zerou, coloca de volta na fila de prontos para ser executado novamente no final da fila (append)
        elif dicionario_guia[processo_atual]["restante"] != 0:
            fila_prontos.append(processo_atual)

    #Calculando médias com a ajuda do do dicionario de entrada, que contém a quantidade de processos, o len retorna quantos indíces (processos) existem no dicionário
    retorno_medio /= len(dicionario_de_processos)
    resposta_media /= len(dicionario_de_processos)
    espera_media /= len(dicionario_de_processos)

    return retorno_medio, resposta_media, espera_media