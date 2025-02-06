# Perceptron Simples

Este é um programa em Python que implementa um Perceptron simples para aprender a função lógica **AND**. O algoritmo utiliza aprendizado supervisionado para ajustar os pesos com base nas entradas e saídas esperadas.

## 📌 Funcionalidades
- Implementação de um Perceptron simples.
- Treinamento da rede com ajuste de pesos.
- Teste do Perceptron após o treinamento.

## 🔧 Requisitos
- Python 3.x

## 🚀 Como executar
1. Clone este repositório ou copie o código para seu ambiente local.
2. Execute o script principal:
   ```bash
   python main.py
   ```

## 🏗 Estrutura do Código
- `somaPonderada(entradas, pesos)`: Calcula a soma ponderada das entradas e pesos.
- `ativacao(soma)`: Função de ativação (degrau unitário).
- `treinamentoPerceptron(entradas, pesos, saidasEsperadas)`: Treina o Perceptron ajustando os pesos.
- `testarPerceptron(entradas, pesos)`: Testa o Perceptron treinado.
- `main()`: Função principal que executa o treinamento e o teste.

## 📊 Exemplo de Saída
```bash
Ciclo 1
Ciclo 2
Ciclo 3
Treinamento Concluído

Testando Perceptron:
Entrada: [0, 0, 0], Saída: 0
Entrada: [0, 0, 1], Saída: 0
Entrada: [0, 1, 0], Saída: 0
Entrada: [0, 1, 1], Saída: 0
Entrada: [1, 0, 0], Saída: 0
Entrada: [1, 0, 1], Saída: 0
Entrada: [1, 1, 0], Saída: 1
Entrada: [1, 1, 1], Saída: 1
```

## 📌 Observação
O código pode ser ajustado para outras funções lógicas alterando os dados de entrada e as saídas esperadas.

## 📜 Licença
Este projeto é de domínio público e pode ser utilizado livremente.

