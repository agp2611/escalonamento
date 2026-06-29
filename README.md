<h1 align="center"> Simulador de Escalonamento de CPU </h1>

Miniprojeto da disciplina de **Sistemas Operacionais**, cujo o objetivo é entender e implementar um código que **simule** os algoritmos de **escalonamento**:

* **First-come, First-served(FCFS)**,
* **Shortest job first(SJF)**, 
* **Round robin(RR)**. 

Com isso, deve-se extrair uma série de **estatísticas** baseadas em cada **algoritmo**.


### Funcionalidades:


* FCFS (First-come, First-served):
   * Algoritmo simples baseado na ordem de chegada de cada job, semelhante ao FIFO.
* SJF (Shortest job first):
   * Priorize jobs com o menor tempo de excução, caso hajam tempos iguais, é ordenado por FCFS, e caso ainda haja empate, o critério é o id do job.
* RR (Round robin):
   * Atribui uma fatia de tempo fixa para cada processo (quantum). Ao expirar o tempo, o processo é movido para o final da fila de prontos e o próximo processo é executado, garantindo um revezamento justo entre as tarefas.


---



### Estrutura do projeto:

```
/projeto-escalonador
├── data/
│   └── entrada.txt             # Arquivos de entrada (.txt)
├── src/
│   ├── algorithms/             # Algoritmos de escalonamento
│   │   ├── fcfs.py
│   │   ├── sjf.py
│   │   └── rr.py
│   └── escalonador.py          # Script principal de execução
└── README.md
```

### Como executar:

1. No terminal bash:
    ```bash
    git clone https://github.com/agp2611/escalonamento.git
    ```

2. Navegue até a raiz do projeto e execute
    ```bash
    python3 src/escalonador.py
    ```

---

### Exemplo de entrada:

```txt
0 20
0 10
4 6
4 8
```

### Exemplo de saída:

```txt
FCFS: 30,5 19,5 19,5
SJF: 21,5 10,5 10,5
RR: 31,5 2,0 20,5
```