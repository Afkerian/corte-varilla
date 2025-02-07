# 📌 Versión Recursiva Pura (Sin Memoización)
def cut_rod(p, n):
    # Caso base: si la longitud es 0, la ganancia es 0
    if n == 0:
        return 0

    q = -float('inf')  # Inicializamos la ganancia máxima en -infinito

    # Probar todos los cortes posibles desde 1 hasta n
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))

    return q

# 📌 Versión Recursiva con Memoización (Optimizada)
def memoized_cut_rod(p, n):
    # Inicializamos los arrays r y s
    r = [-float('inf')] * (n + 1)  # r[i] almacenará la ganancia máxima para longitud i
    s = [0] * (n + 1)  # s[i] almacenará el primer corte óptimo para longitud i
    return memoized_cut_rod_aux(p, n, r, s), s

def memoized_cut_rod_aux(p, n, r, s):
    # Si ya hemos calculado la ganancia para una longitud n, la devolvemos
    if r[n] >= 0:
        return r[n]
    
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1):
            # Calculamos la ganancia posible si cortamos la varilla en i
            temp = p[i - 1] + memoized_cut_rod_aux(p, n - i, r, s)
            # Si la ganancia es mayor, actualizamos q y guardamos el corte
            if temp > q:
                q = temp
                s[n] = i  # Guardamos el primer corte óptimo para n

    # Guardamos la ganancia máxima para longitud n
    r[n] = q
    return q

# 📌 Función para reconstruir la solución óptima (cómo cortar la varilla)
def print_optimal_cut(s, n):
    while n > 0:
        print(f"Corte de longitud {s[n]}")
        n = n - s[n]

# 📌 Ejemplo de uso
p = [1, 5, 8, 9]  # Precio para cada longitud de varilla
n = 4  # Longitud de la varilla

# ✅ Llamada a la versión recursiva pura (ineficiente)
max_profit_recursive = cut_rod(p, n)
print(f"[Recursivo Puro] Ganancia máxima: {max_profit_recursive}")

# ✅ Llamada a la versión con memoización (eficiente)
max_profit_memo, s = memoized_cut_rod(p, n)
print(f"[Memoización] Ganancia máxima: {max_profit_memo}")

# ✅ Mostrar los cortes óptimos
print("Cortes óptimos:")
print_optimal_cut(s, n)
