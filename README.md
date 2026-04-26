# Calculadora CLI (Com Inteiros) com Typer

Este é um projeto de calculadora simples implementado como uma aplicação de linha de comando (CLI) usando a biblioteca `typer` em Python.

A calculadora reconstrói operações matemáticas básicas do zero utilizando apenas lógica fundamental. A multiplicação é feita por somas sucessivas e a divisão por subtrações sucessivas, demonstrando como operações complexas podem ser derivadas de conceitos simples.

O projeto tem foco no estudo de lógica de programação, fluxo de execução e construção manual de operações básicas da computação.

## Funcionalidades

- **Soma:** Realiza a soma de dois números inteiros.
- **Subtração:** Realiza a subtração de dois números inteiros.
- **Multiplicação:** Realiza a multiplicação de dois números inteiros através de somas sucessivas.
- **Divisão:** Realiza a divisão inteira de dois números através de subtrações sucessivas, mostrando o resultado (quantas vezes o divisor coube no dividendo) e o resto.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema. Você também precisará instalar a biblioteca `typer`:

```bash
pip install typer
```

### Execução

Para executar as operações, use os seguintes comandos no terminal:

- **Soma:**
  ```bash
  python main.py som 5 3
  ```

- **Subtração:**
  ```bash
  python main.py sub 10 4
  ```

- **Multiplicação:**
  ```bash
  python main.py mul 6 7
  ```

- **Divisão:**
  ```bash
  python main.py div 20 3
  ```


## Exemplo de Saída

```
# Exemplo para soma
Soma:  8

# Exemplo para multiplicação
0 + 6 = 6
6 + 6 = 12
12 + 6 = 18
18 + 6 = 24
24 + 6 = 30
30 + 6 = 36
36 + 6 = 42

# Exemplo para divisão
20 - 3 = 17
17 - 3 = 14
14 - 3 = 11
11 - 3 = 8
8 - 3 = 5
5 - 3 = 2
Resultado: Repetiu 6 Vezes
Resto: 2
```
## Observação sobre a divisão

A operação de divisão implementada neste projeto trabalha apenas com **divisão inteira**.

Isso significa que o algoritmo calcula quantas vezes o divisor cabe completamente no dividendo, utilizando subtrações sucessivas.

O valor que sobra após essas subtrações é chamado de **resto da divisão**.

O algoritmo não calcula números decimais, pois seu objetivo é demonstrar a lógica básica da divisão a partir de subtrações repetidas, semelhante ao funcionamento de uma máquina de cálculo simples.

### Ex:

```
O resto pode ser utilizado para representar a parte decimal da divisão, sendo interpretado como uma fração do divisor. Assim, a divisão completa pode ser escrita como: 

20 ÷ 3 = 6 + (2 ÷ 3) ≈ 6,666...

```
## Autor

Álvaro Carvalho Cabral de Andrade
