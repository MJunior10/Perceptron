from random import randint

def somaPonderada(entradas, pesos):
    return sum(entradas[i] * pesos[i] for i in range(len(entradas)))

def ativacao(soma):
    return 1 if soma >= 1 else 0  # Definição do limiar para classificar

def treinamentoPerceptron(entradas, pesos, saidasEsperadas, taxaAprendizado=1, ciclo=0):
    print(f"Ciclo {ciclo+1}")
    erroTotal = 0
    for i in range(len(entradas)):
        saidaFinal = ativacao(somaPonderada(entradas[i], pesos))
        erro = saidasEsperadas[i] - saidaFinal
        erroTotal += abs(erro)
        for j in range(len(pesos)):
            pesos[j] += taxaAprendizado * erro * entradas[i][j]

    print(f"Erro total: {erroTotal}")
    if erroTotal == 0:
        print("\nTreinamento Concluído\n")
        return pesos
    else:
        return treinamentoPerceptron(entradas, pesos, saidasEsperadas, taxaAprendizado, ciclo + 1)

def testarPerceptron(entradas, pesos):
    print("Testando Perceptron:\n")
    for i in range(len(entradas)):
        saida = ativacao(somaPonderada(entradas[i], pesos))
        print(f"Entrada: {entradas[i]}, Saída: {'Quente' if saida == 1 else 'Frio'}")

def main():
    # Temperatura, Umidade, Vento (0 ou 1)
    entradasTreinamento = [
        [30, 70, 0],  # Quente
        [35, 50, 1],  # Quente
        [10, 80, 0],  # Frio
        [15, 60, 1]   # Frio
    ]
    
    saidasEsperadas = [1, 1, 0, 0]  # Quente (1) e Frio (0)

    # Inicializa pesos aleatórios entre -1 e 1
    pesosIniciais = [randint(-1,1) for _ in range(3)]
    
    # Treinamento
    pesosFinais = treinamentoPerceptron(entradasTreinamento, pesosIniciais, saidasEsperadas)

    # Testes com novos dados
    entradasPerceptron = [
        [5, 90, 0],   # Esperado: Frio
        [12, 70, 1],  # Esperado: Frio
        [28, 40, 0],  # Esperado: Quente
        [33, 50, 1]   # Esperado: Quente
    ]
    
    testarPerceptron(entradasPerceptron, pesosFinais)

if __name__ == "__main__":
    main()
