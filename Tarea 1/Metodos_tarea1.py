global numero

#   Inicio de la funcion string_work


def string_work(input1):
    #   Asegura que el dato recibido es un string
    if (isinstance(input1, str)):
        #       Verifica que no hayan caracteres especiales ni números
        for x in input1:
            if (65 <= ord(x) <= 90 or 97 <= ord(x) <= 122):
                1 == 1
            else:
                # Error que indica si alguno de los caracteres no es una letra
                return 2
        return input1.swapcase()
    else:
        #       Error que indica que el dato recibido no es de tipo string
        return 1

#   Inicio de la funcion num_to_string


def num_to_string(numero):  # verifica numero en rango [0:99]

    if isinstance(numero, int):

        if 0 <= numero <= 99:
            # si la entrada es menor a 10, se retorna lo que esté en la
            # posición (según el número digitado) del la tupla de unidades
            if numero < 10:
                return UNIDADES[numero]
            decena, unidad = divmod(numero, 10)
            if numero <= 19:
                resultado = DECENAS[unidad]
            elif numero <= 29:
                # para los números entre 20 y 29 concatena veinti con su
                # respectiva unidad
                resultado = 'veinti%s' % UNIDADES[unidad]
            else:
                resultado = DIEZ_DIEZ[decena]
                if unidad > 0:
                    # para números de 30 en adelante concatena las decenas con
                    # su respectiva unidad
                    resultado = '%s_y_%s' % (resultado, UNIDADES[unidad])
            return resultado
        else:
            return 4  # Error que indica que un dato es mayor a 99 o menor a 0

    else:
        return 3  # Error que indica que un dato no es un número entero


# se crean tuplas según unidades, decenas o saltos de diez en diez
UNIDADES = (
    'cero',
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve'
)

DECENAS = (
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    'quince',
    'dieciseis',
    'diecisiete',
    'dieciocho',
    'diecinueve'
)

DIEZ_DIEZ = (
    'cero',
    'diez',
    'veinte',
    'treinta',
    'cuarenta',
    'cincuenta',
    'sesenta',
    'setenta',
    'ochenta',
    'noventa'
)
