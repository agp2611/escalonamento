#Importando bibliotecas necessárias
import math
import string 

#Inciailizando variáveis de forma limpa
tipo_fila: str = ""
retorno_medio: float = 0.0; resposta_medio: float = 0.0; espera_medio: float = 0.0

#Contém o tempo de chegada e a duração de cada processo
# -=- Ref: https://www.w3schools.com/python/python_file_open.asp
entrada = open("entrada.txt", "r") #Apenas leitura

"""
Estruturando saída: 

[Tipo de Fila] [Tempo de Retorno médio] [Tempo de Resposta médio] [Tempo de Espera médio]

exemplo:
FCFS 30,5 19,5 19,5 
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
"""

print("%s %.1f %.1f %.1f" % (tipo_fila, retorno_medio, resposta_medio, espera_medio))