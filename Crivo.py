def crivo_eratostenes(limite):
    
    # Inicializa um array para marcar se um numero é primo ou não
    # Incialmente, todos os numeros ssão considerados primos
    
    numeros_primos = [True for _ in range(limite + 1)]
    numeros_primos[0] = numeros_primos[1] = False # 0 e 1 não são primos

    # O processo começa a partir do número 2, o primeiro primo

    p = 2
    
    while p * p <= limite:
        if numeros_primos[p]:

            #Marca todos os multiplos de p como não primos

            for i in range(p * p, limite + 1, p):
                numeros_primos[i] = False

        p += 1

    # Retorna uma lista com os numeros primos até o limite

    primos = [i for i in range(limite + 1) if numeros_primos[i]]
    return primos

# Exemplo: encontrar todos os números primos até 50
limite = 50
primos_ate_limite = crivo_eratostenes(limite)
print(f"Números primos até {limite}:")
print(primos_ate_limite)
