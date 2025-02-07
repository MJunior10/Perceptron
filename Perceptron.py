from random import randint

def somaPonderada(entradas, pesos):
  return sum(entradas[i] * pesos[i] for i in range(len(entradas)))


def ativacao(soma):
  return 1 if soma >= 1 else 0


def treinamentoPerceptron(entradas,pesos,saidasEsperadas,taxaAprendizado=1,ciclo=0):
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
    return treinamentoPerceptron(entradas, pesos, saidasEsperadas,
                                 taxaAprendizado, ciclo + 1)


def testarPerceptron(entradas, pesos):
  print("Testando Perceptron:\n")
  for i in range(len(entradas)):
    saida = ativacao(somaPonderada(entradas[i], pesos))
    print(f"Entrada: {entradas[i]}, Saída: {saida}")


def main():
  entradasTreinamento = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
  saidasEsperadas = [0, 0, 1, 1]
  pesosIniciais = [randint(-1,1) for i in range(3)]
   
  pesosFinais = treinamentoPerceptron(entradasTreinamento, pesosIniciais,
                                      saidasEsperadas)

  entradasPerceptron = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0],
                        [1, 0, 1], [1, 1, 0], [1, 1, 1]]
  testarPerceptron(entradasPerceptron, pesosFinais)


if __name__ == "__main__":
  main()
