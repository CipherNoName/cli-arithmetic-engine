import typer

app = typer.Typer()

@app.command()
def som(a: int, b: int): # Pega os valores
    print("Soma: ", a + b) # Soma e executa na tela

@app.command()
def sub(a: int, b: int): # Pega os valores
    print("Subtração: ", a - b)  #Subtrai dois números.
@app.command()
def mul(a: int, b: int): # Pega os valores
    resultado = 0
    for x in range(b):
        print(resultado, "+", a, end=" ") # Mostra a operação feita
        resultado += a # Faz a operação
        print("=", resultado) # Mostra o resultado final
@app.command()
def div(a: int, b: int): # Pega os valores
    resultado = 0 
    for _ in range(a):
        if a < b: # Para quando não dá mais para subtrair b de a
            break
        print(a, "-", b, "=", a - b) # Mostra a operação feita
        a -= b # Faz a operação
        resultado +=  1 # Grava quantas vezes se repetiu
    
    print("Resultado: Repetiu", resultado, "Vezes") # Mostra quantas vezes se repetiu
    print("Resto:") # Mostra o resto
        
if __name__ == "__main__":
    app() 
