def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)  # r[i] almacenará la máxima ganancia para longitud i
    s = [0] * (n + 1)  # s[i] almacenará el primer corte óptimo para longitud i

    # Construimos la solución óptima de abajo hacia arriba
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:  # Verificamos si hacer un corte en 'i' es mejor
                q = p[i - 1] + r[j - i]
                s[j] = i  # Guardamos el corte óptimo
        r[j] = q  # Guardamos la mejor ganancia para longitud j

    return r[n], s

# 📌 Función para reconstruir la solución óptima (cómo cortar la varilla)
def print_optimal_cut(s, n):
    while n > 0:
        print(f"Corte de longitud {s[n]}")
        n -= s[n]

# 📌 Ejemplo de uso
p = [1, 5, 8, 9]  # Precio para cada longitud de varilla
n = 4  # Longitud de la varilla

# ✅ Llamamos a la función con programación dinámica
max_profit, s = bottom_up_cut_rod(p, n)

# ✅ Mostramos la ganancia máxima
print(f"Ganancia máxima: {max_profit}")

# ✅ Mostramos los cortes óptimos
print("Cortes óptimos:")
print_optimal_cut(s, n)
