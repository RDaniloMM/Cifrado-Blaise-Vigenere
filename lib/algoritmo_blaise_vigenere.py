# Definimos los alfabetos personalizados
ALFABETOS = {
    "Alfabeto Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú.?¿¡!,+-*/_\"\n\\|@#$%&()=[]{}`^~;:<>",
    "Alfabeto Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;:!?()\"' ",
    "Alfabeto Clásico": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
}

# Funciones del cifrado de Vigenère actualizadas
def cifrar(texto, clave, alfabeto):
    i = 0
    while len(clave) < len(texto):
        clave += clave[i]
        i += 1
    C = ""
    k_index = 0
    for j in range(len(texto)):
        if texto[j] in alfabeto:
            M_i = alfabeto.index(texto[j])
            K_i = alfabeto.index(clave[k_index])

            C_i = (M_i + K_i) % len(alfabeto)

            C += alfabeto[C_i]
            k_index += 1
        else:
            C += texto[j]
    return C

def descifrar(texto_cifrado, clave, alfabeto):
    i = 0
    while len(clave) < len(texto_cifrado):
        clave += clave[i]
        i += 1
    M = ""
    k_index = 0
    for j in range(len(texto_cifrado)):
        if texto_cifrado[j] in alfabeto:
            C_i = alfabeto.index(texto_cifrado[j])
            K_i = alfabeto.index(clave[k_index])

            M_i = (C_i - K_i) % len(alfabeto)

            M += alfabeto[M_i]
            k_index += 1
        else:
            M += texto_cifrado[j]
    return M