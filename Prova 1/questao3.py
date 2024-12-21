import math

MAX_ITERACOES = 10
EPS = 1e-3

# Variáveis da função
pressao = 1.5e-4

def f(x):
    return 25 * (x**2) + math.log(x) - pressao

def metodo_bisseccao(a, b):
    for i in range(MAX_ITERACOES):
        x = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fx = f(x)

        erro_relativo = abs(b - a) / abs(x)  
        print(f"Iteração {i+1}: a = {a:.6f}, b = {b:.6f}, f(a) = {fa:.6f}, f(b) = {fb:.6f}, x = {x:.6f}, f(x) = {fx:.6f}, erro relativo = {erro_relativo}")
        
        # Raiz está no intervalo [a, dm]
        if fa * fx < 0:
            b = x
        # Raiz está no intervalo [dm , b]
        else:
            a = x

        
        # Parar caso o erro desejado seja atingido
        if (erro_relativo < EPS):
            break

    return x, erro_relativo

def main():
    a = 0.2
    b = 0.3

    raiz, erro_relativo = metodo_bisseccao(a, b)

    print(f"\nRaiz aproximada: x = {raiz:.6f}")
    print(f"f(x) = {f(raiz):.6f}")
    print(f"Erro relativo final = {erro_relativo:.6f}")

main()
