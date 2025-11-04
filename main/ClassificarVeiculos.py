import random

#entradas (Características: [Luxo, Capacete, Econômico])
entradas_treinamento = [
    [0, 1, 1],  # 011 - Moto (Não luxo, Tem capacete, Econômico)
    [1, 1, 0],  # 110 - Moto (Luxo, Tem capacete, Não econômico)
    [0, 0, 1],  # 001 - Carro (Não luxo, Sem capacete, Econômico)
    [1, 0, 0]  # 100 - Carro (Luxo, Sem capacete, Não econômico)
]

#saídas esperadas (0 = Moto, 1 = Carro)
saidas_treinamento = [
    0,  # Moto
    0,  # Moto
    1,  # Carro
    1  # Carro
]

# peso1 = 0
# peso2 = 0
# peso3 = 0

peso1 = random.choice([-1, 1])
peso2 = random.choice([-1, 1])
peso3 = random.choice([-1, 1])

#para controlar o loop de treinamento
epoca = 0

print("--- Iniciando Treinamento do Perceptron ---")
print(f"Pesos Iniciais: p1={peso1}, p2={peso2}, p3={peso3}\n")

while True:  #loop de épocas
    falha = 0  #contador de falhas nesta época
    epoca += 1

    print(f"--- ÉPOCA {epoca} ---")

    #itera sobre cada dado de treinamento (usando as listas separadas)
    for i in range(len(entradas_treinamento)):

        #receba os dados de entrada (já separados)
        entradas = entradas_treinamento[i]
        esperado = saidas_treinamento[i]

        entrada1 = entradas[0]  #é luxo?
        entrada2 = entradas[1]  #tem capacete?
        entrada3 = entradas[2]  #é econômico?

        soma = (entrada1 * peso1) + (entrada2 * peso2) + (entrada3 * peso3)

        T = 0  #saída calculada (T)
        if soma > 0:
            T = 1
        else:
            T = 0  #se soma for 0 ou negativa, a saída é 0

        #verifica se a saída está errada
        print(f"  Entrada: {entradas} | Esperado: {esperado} | Calculado: {T} | Soma: {soma}")

        if T != esperado:
            falha += 1

            # chama a parte de backward (ajuste de pesos)
            if T == 0 and esperado == 1:
                #se a saída estiver errada e for 0 (calculou 0, mas era 1)
                #adicionar a cada peso os sinais de entrada relativos a elas
                peso1 += entrada1
                peso2 += entrada2
                peso3 += entrada3
                print(f"    -> AJUSTE (+): Novos pesos: p1={peso1}, p2={peso2}, p3={peso3}")

            elif T == 1 and esperado == 0:
                # *se a saída estiver errada e for 1 (calculou 1, mas era 0)
                # Subtrair de cada peso os sinais de entrada relativos a elas
                peso1 -= entrada1
                peso2 -= entrada2
                peso3 -= entrada3
                print(f"    -> AJUSTE (-): Novos pesos: p1={peso1}, p2={peso2}, p3={peso3}")

    print(f"Pesos ao final da Época {epoca}: p1={peso1}, p2={peso2}, p3={peso3}")
    print(f"Total de falhas na Época {epoca}: {falha}\n")

    #condição de parada: nenhuma falha na época
    if falha == 0:
        print(f"Treinamento concluído na Época {epoca} sem falhas!")
        break

    #limite de segurança para evitar loop infinito
    if epoca > 100:
        print("Treinamento interrompido por limite de épocas.")
        break

print("\n=== ANÁLISE DE RELEVÂNCIA DAS VARIÁVEIS ===")

variaveis = ["É luxo?", "Tem capacete?", "É econômico?"]
pesos_finais = [peso1, peso2, peso3]

#soma dos valores absolutos (para calcular porcentagem)
soma_abs = sum(abs(p) for p in pesos_finais)

#gera lista com (nome, peso, relevância)
relevancias = []
for i in range(3):
    if soma_abs != 0:
        rel = abs(pesos_finais[i]) / soma_abs * 100
    else:
        rel = 0
    direcao = "puxa para CARRO (1)" if pesos_finais[i] > 0 else \
               "puxa para MOTO (0)" if pesos_finais[i] < 0 else "neutro"
    relevancias.append((variaveis[i], pesos_finais[i], rel, direcao))

#ordena da mais para a menos relevante
relevancias.sort(key=lambda x: abs(x[1]), reverse=True)

#exibe tabela
for nome, peso, rel, direcao in relevancias:
    print(f"{nome:<20} | Peso = {peso:>5.2f} | Relevância = {rel:>6.2f}% | {direcao}")

print("\n--- Fase de Teste ---")
print("Rede treinada. Pesos finais:")
print(f"p1 (Luxo) = {peso1}")
print(f"p2 (Capacete) = {peso2}")
print(f"p3 (Econômico) = {peso3}")
print("\nDigite 's' para sair.")

while True:
    entrada_teste_str = input("Digite 3 valores de entrada (ex: '101'): ")

    if entrada_teste_str.lower() == 's':
        break

    if len(entrada_teste_str) != 3 or not entrada_teste_str.isdigit():
        print("Entrada inválida. Digite 3 números (0 ou 1).")
        continue

    #processa a entrada de teste
    e1 = int(entrada_teste_str[0])
    e2 = int(entrada_teste_str[1])
    e3 = int(entrada_teste_str[2])

    #calcula a soma e a ativação
    soma_teste = (e1 * peso1) + (e2 * peso2) + (e3 * peso3)

    T_teste = 0
    if soma_teste > 0:
        T_teste = 1
    else:
        T_teste = 0

    #exibe o resultado
    resultado_classe = "Carro (1)" if T_teste == 1 else "Moto (0)"
    print(f"  Entrada: {entrada_teste_str} -> Soma: {soma_teste}")
    print(f"  Resultado: {T_teste} ({resultado_classe})\n")

