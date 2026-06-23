#Importando bibliotecas necessárias
import string 
from fcfs import rodar_fcfs
from typing import List
from typing import Dict, List

#Inciailizando variáveis de forma limpa
tipo_fila: str = ""
retorno_FCFS: float = 0.0; resposta_FCFS: float = 0.0; espera_FCFS: float = 0.0
processos: List[str] = []
dicionario_de_processos: dict[str, any] = {}

#Lendo os processos do arquivo de entrada - Contém o tempo de chegada e a duração de cada processo
# -=- Ref: https://www.geeksforgeeks.org/python/python-read-text-file-into-list-or-array/
with open("entrada.txt") as file:
    processos = [line.strip() for line in file] #stip removes spaces at the start and end of the string.

#Convertendo em dicionário python
# -=- Ref: https://medium.com/@atatus/https-www-atatus-com-blog-python-converting-lsts-to-dictionaries-c3f038a8ce30
for indice, elemento in enumerate(processos):
    # elemento.split() transforma '0 20' em ['0', '20']
    chegada, duracao = elemento.split() 
    
    # Guarda como tupla de inteiros: (0, 20)
    dicionario_de_processos[indice] = (int(chegada), int(duracao))

#Testando se o dicionário foi criado corretamente
#print(dicionario_de_processos)

"""
Estruturando saída: 

[Tipo de Fila] [Tempo de Retorno médio] [Tempo de Resposta médio] [Tempo de Espera médio]
                retorno = tempo_fim - tempo_chegada
                                         resposta = tempo_primeira_execucao - tempo_chegada
                                                                   espera = retorno - duracao
                                        
exemplo:
FCFS 30,5 19,5 19,5 
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
"""

#Rodar FCFS
retorno_FCFS, resposta_FCFS, espera_FCFS = rodar_fcfs(dicionario_de_processos)

print("FCFS: %.1f %.1f %.1f" % (retorno_FCFS, resposta_FCFS, espera_FCFS))