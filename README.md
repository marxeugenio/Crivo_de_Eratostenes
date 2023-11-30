# Crivo de Eratóstenes

O Crivo de Eratóstenes é um algoritmo eficiente para encontrar todos os números primos até um determinado limite. Ele funciona marcando os múltiplos de cada número primo e filtrando os números não marcados como primos.

## Funcionamento

O algoritmo é implementado em Python na função `crivo_eratostenes` presente no arquivo `crivo_eratostenes.py`. A função recebe um limite como entrada e retorna uma lista contendo todos os números primos até esse limite.

### Executando o exemplo

Para executar o exemplo e encontrar os números primos até um determinado limite, você pode modificar o valor da variável `limite` no arquivo `crivo_eratostenes.py` e executá-lo com um interpretador Python.

```python
limite = 50
primos_ate_limite = crivo_eratostenes(limite)
print(f"Números primos até {limite}:")
print(primos_ate_limite)
