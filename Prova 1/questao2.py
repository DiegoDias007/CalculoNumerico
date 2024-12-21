import math

MAX_ITERACOES = 3
CHUTE_INICIAL = 1

# variaveis da funcao
c = 5

def f(x):
    return 10 - 20 * (math.exp(-0.2*x) - math.exp(-0.75*x)) - c

def derivada(x):
    delta = 1e-5  # Pequeno delta para aproximação da derivada
    return (f(x + delta) - f(x)) / delta

def metodo_newton(chute_inicial, max_iteracoes):
    x = chute_inicial
    for i in range(max_iteracoes):
        fx = f(x)
        dfx = derivada(x)

        proximo_x = x - fx / dfx
        erro_relativo = abs(x - proximo_x) / abs(proximo_x)
        x = proximo_x
        
        print(f"Iteração {i+1}: x = {proximo_x:.6f}, f(x) = {fx:.6f}, erro relativo = {erro_relativo}")

    return x

def main():
    print("Chute inicial = ", CHUTE_INICIAL)
    
    raiz = metodo_newton(CHUTE_INICIAL, MAX_ITERACOES)
    
    print(f"Raiz aproximada: x = {raiz:.6f}")
    print(f"f(x) = {f(raiz):.6f}")

main()