MAX_ITERACOES = 3

# Variáveis da função
M = 1250
C = 10000
n = 10

def f(x):
    return (M / x) * (1 - (1 + x) ** (-n)) - C

def metodo_secante(a, b):

    for i in range(MAX_ITERACOES):
        # Pela fórmula, a = x(n-1), b = x(n), x = x(n+1)
        fa = f(a)
        fb = f(b)

        # Calcula o próximo valor de x usando a fórmula da secante
        x = b - fb * (b - a) / (fb - fa)
        fx = f(x)

        # Calcula erro relativo
        erro_relativo = abs(x - b) / abs(x)

        print(f"Iteração {i+1}: a = {a:.6f}, b = {b:.6f}, f(a) = {fa:.6f}, f(b) = {fb:.6f}, x = {x:.6f}, f(x) = {fx:.6f}, erro relativo = {erro_relativo}")

        # Atualiza os valores para a próxima iteração
        a, b = b, x

    return x, erro_relativo

def main():
    a = 0.01
    b = 0.05

    raiz, erro_relativo = metodo_secante(a, b)

    print(f"\nRaiz aproximada: x = {raiz:.6f}")
    print(f"f(x) = {f(raiz):.6f}")
    print(f"Erro relativo final = {erro_relativo:.6f}")

main()
