def verifica_se_pertence(numero) -> bool:
    num_proximo = None
    num_anterior = 0
    num_atual = 1
    
    while True:
        if numero == num_atual:
            return True
        
        num_proximo = num_anterior + num_atual
        num_anterior = num_atual
        num_atual = num_proximo
        
        if numero < num_atual:
            return False
        

numero = int(input("Digite um número e verifique saiba se pertence a sequência de Fibonacci: "))
print(
    "Pertence a sequência!" if verifica_se_pertence(numero) else "Não pertence a sequência!"
)