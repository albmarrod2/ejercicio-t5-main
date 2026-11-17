from collections import Counter, defaultdict


def sustituye_palabras(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    # TODO: Implementar la función
    pass


def indexa_por_iniciales(texto: str) -> dict[str, set[str]]:
    """
    Construye un diccionario que indexa las distintas palabras del texto
    (pasado a minúsculas) por sus iniciales.
    
    Parámetros:
        texto: Texto del que se van a extraer las palabras.
    
    Devuelve:
        Diccionario que asocia a cada inicial el conjunto de palabras
         que comienzan por dicha inicial.
    
    """
    # TODO: Implementar la función
    pass

def construye_frecuencias_bigramas(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    bigramas = []
    texto = texto.lower()
    for c1, c2 in zip(texto, texto[1]):  # para recorrerlas a la vez
        if c1.isalpha() and c2.isalpha():
            bigramas.append(c1 + c2)
    contador = Counter(bigramas)   # cuenta cuantas veces ha salido cada bigrama

    total_bigramas = len(bigramas)
    res = {}
    for bigrama, conteo in contador.items():  # sin el .item() solo devuelve las claves del diccionario es decir los bigramas
        res[bigrama] = conteo / total_bigramas
    return res

    '''otra solucion
        contador = {}
        texto = texto.lower()
        for c1, c2 in zip(texto, texto[1]):  # para recorrerlas a la vez
            if c1.isalpha() and c2.isalpha():
                bigrama = c1 + c2
                contador[bigrama] = contador.get(bigrama, 0) + 1
        contador = Counter(bigramas)   # cuenta cuantas veces ha salido cada bigrama
    
        total_bigramas = sum(contador.values())
        res = {}
        for bigrama, conteo in contador.items():  # sin el .item() solo devuelve las claves del diccionario es decir los bigramas
            res[bigrama] = conteo / total_bigramas
        return res
        '''

    '''otra solucion con defaultdict
            contador = defaultdict(int)
            texto = texto.lower()
            for c1, c2 in zip(texto, texto[1]):  # para recorrerlas a la vez
                if c1.isalpha() and c2.isalpha():
                    bigrama = c1 + c2
                    contador[bigrama] += 1
            contador = Counter(bigramas)   # cuenta cuantas veces ha salido cada bigrama
        
            total_bigramas = sum(contador.values())
            res = {}
            for bigrama, conteo in contador.items():  # sin el .item() solo devuelve las claves del diccionario es decir los bigramas
                res[bigrama] = conteo / total_bigramas
            return res'''


def calcula_distancia_media_frecuencias(freq1: dict[str, float], freq2: dict[str, float]) -> float:
    """
    Calcula la distancia media entre las frecuencias normalizadas
    representadas por dos diccionarios de frecuencias.

    Parámetros:
        freq1: Primer diccionario de frecuencias.
        freq2: Segundo diccionario de frecuencias.

    Devuelve:
        Distancia media entre los dos vectores de frecuencias, o 0.0 si ambos diccionarios están vacíos.
    """
    if len(freq1) == 0 and len(freq2) == 0:
        return 0.0
    
    todos_bigramas = set(freq1)| set(freq2) # set transforma en una connj iterable,,, | significa union
    suma_diferencias = 0
    for bigrama in todos_bigramas:
        suma_bigramas += abs(freq1.get(bigrama, 0) - freq2.get(bigrama, 0))   #get si no encuentra devuelve none, ponemos el 0 para q lo devuelva en vez de none
    return suma_diferencias / len(todos_bigramas)


def identifica_idioma(textos_ejemplo: dict[str, str], texto_a_identificar: str) -> str:
    """
    Identifica el idioma de un texto comparando sus frecuencias de bigramas
    con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

    Parámetros:
        textos_ejemplo: Diccionario que asocia a cada idioma (por ejemplo 'es') un texto de ejemplo en ese idioma.
        texto_a_identificar: Texto cuyo idioma se quiere identificar.

    Devuelve:
        El idioma identificado del texto.
    """
    # PASOS A SEGUIR:
    # 1.- Obtener el diccionario de frecuencias para texto_a_identificar (dic_objetivo)

    dic_objetivo = construye_frecuencias_bigramas(texto_a_identificar)
    distancias_idiomas = []

    # 2.- Recorrer el diccionario textos_ejemplo

    for idioma, texto_idioma in textos_ejemplo.items():

    # 3.- Obtener el diccionario de frecuancias para el ididoma actual (dic_idioma)

        dic_idioma = construye_frecuencias_bigramas(texto_idioma)

    # 4.- Calcula la distancia entre dic_idioma y dic_objetivo

        distancia = calcula_distancia_media_frecuencias(dic_objetivo, dic_idioma)

    # 5.- Guardamos en una lista (distancia, identificador_idioma)

        distancias_idiomas.append((distancia, idioma))

    # 6.- Buscar el minimo de la lista (menor distancia)

        _, idioma = min(distancias_idiomas)
        #distancia_idioma_minimos = min(distancias_idiomas)

    # 7.- Devolver el identificador de idioma

        return idioma
        #return distancia_idioma_minimos[1]



