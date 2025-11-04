#Modelo perceptron simples 

Características: [Luxo, Capacete, Econômico]

```py
entradas_treinamento = [
    [0, 1, 1],  # 011 - Moto (Não luxo, Tem capacete, Econômico)
    [1, 1, 0],  # 110 - Moto (Luxo, Tem capacete, Não econômico)
    [0, 0, 1],  # 001 - Carro (Não luxo, Sem capacete, Econômico)
    [1, 0, 0]  # 100 - Carro (Luxo, Sem capacete, Não econômico)
]

# Saídas esperadas (0 = Moto, 1 = Carro)
saidas_treinamento = [
    0,  # Moto
    0,  # Moto
    1,  # Carro
    1  # Carro
]
```