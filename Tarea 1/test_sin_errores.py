import Metodos_tarea1  # se importa el archivo Metodos_tarea1

# verifica que la funcion string_work intercambie mayusculas a minusculas
# y viceversa


def test_caracteres():
    assert Metodos_tarea1.string_work("abcdeLMNOPQRXYZ") == "ABCDElmnopqrxyz"


# verifica que el dato de entrada de la función string_work sea un string,
# sino da un error
def test_error_numero():
    assert Metodos_tarea1.string_work(54) == 1


# verifica que el dato de entrada de la funcion string_work no tenga
# caracteres especiales ni numeros
def test_error_num_simbolos():
    assert Metodos_tarea1.string_work("asdS4@") == 2


# verifica que la funcion num_to_string retorne el string del numero recibido
def test_prueba_todos_numeros():
    assert Metodos_tarea1.num_to_string(0) == "cero"
    assert Metodos_tarea1.num_to_string(1) == "uno"
    assert Metodos_tarea1.num_to_string(2) == "dos"
    assert Metodos_tarea1.num_to_string(3) == "tres"
    assert Metodos_tarea1.num_to_string(4) == "cuatro"
    assert Metodos_tarea1.num_to_string(5) == "cinco"
    assert Metodos_tarea1.num_to_string(6) == "seis"
    assert Metodos_tarea1.num_to_string(7) == "siete"
    assert Metodos_tarea1.num_to_string(8) == "ocho"
    assert Metodos_tarea1.num_to_string(9) == "nueve"
    assert Metodos_tarea1.num_to_string(10) == "diez"
    assert Metodos_tarea1.num_to_string(11) == "once"
    assert Metodos_tarea1.num_to_string(12) == "doce"
    assert Metodos_tarea1.num_to_string(13) == "trece"
    assert Metodos_tarea1.num_to_string(14) == "catorce"
    assert Metodos_tarea1.num_to_string(15) == "quince"
    assert Metodos_tarea1.num_to_string(16) == "dieciseis"
    assert Metodos_tarea1.num_to_string(17) == "diecisiete"
    assert Metodos_tarea1.num_to_string(18) == "dieciocho"
    assert Metodos_tarea1.num_to_string(19) == "diecinueve"
    assert Metodos_tarea1.num_to_string(20) == "veinticero"
    assert Metodos_tarea1.num_to_string(21) == "veintiuno"
    assert Metodos_tarea1.num_to_string(22) == "veintidos"
    assert Metodos_tarea1.num_to_string(23) == "veintitres"
    assert Metodos_tarea1.num_to_string(24) == "veinticuatro"
    assert Metodos_tarea1.num_to_string(25) == "veinticinco"
    assert Metodos_tarea1.num_to_string(26) == "veintiseis"
    assert Metodos_tarea1.num_to_string(27) == "veintisiete"
    assert Metodos_tarea1.num_to_string(28) == "veintiocho"
    assert Metodos_tarea1.num_to_string(29) == "veintinueve"
    assert Metodos_tarea1.num_to_string(30) == "treinta"
    assert Metodos_tarea1.num_to_string(31) == "treinta_y_uno"
    assert Metodos_tarea1.num_to_string(32) == "treinta_y_dos"
    assert Metodos_tarea1.num_to_string(33) == "treinta_y_tres"
    assert Metodos_tarea1.num_to_string(34) == "treinta_y_cuatro"
    assert Metodos_tarea1.num_to_string(35) == "treinta_y_cinco"
    assert Metodos_tarea1.num_to_string(36) == "treinta_y_seis"
    assert Metodos_tarea1.num_to_string(37) == "treinta_y_siete"
    assert Metodos_tarea1.num_to_string(38) == "treinta_y_ocho"
    assert Metodos_tarea1.num_to_string(39) == "treinta_y_nueve"
    assert Metodos_tarea1.num_to_string(40) == "cuarenta"
    assert Metodos_tarea1.num_to_string(41) == "cuarenta_y_uno"
    assert Metodos_tarea1.num_to_string(42) == "cuarenta_y_dos"
    assert Metodos_tarea1.num_to_string(43) == "cuarenta_y_tres"
    assert Metodos_tarea1.num_to_string(44) == "cuarenta_y_cuatro"
    assert Metodos_tarea1.num_to_string(45) == "cuarenta_y_cinco"
    assert Metodos_tarea1.num_to_string(46) == "cuarenta_y_seis"
    assert Metodos_tarea1.num_to_string(47) == "cuarenta_y_siete"
    assert Metodos_tarea1.num_to_string(48) == "cuarenta_y_ocho"
    assert Metodos_tarea1.num_to_string(49) == "cuarenta_y_nueve"
    assert Metodos_tarea1.num_to_string(50) == "cincuenta"
    assert Metodos_tarea1.num_to_string(51) == "cincuenta_y_uno"
    assert Metodos_tarea1.num_to_string(52) == "cincuenta_y_dos"
    assert Metodos_tarea1.num_to_string(53) == "cincuenta_y_tres"
    assert Metodos_tarea1.num_to_string(54) == "cincuenta_y_cuatro"
    assert Metodos_tarea1.num_to_string(55) == "cincuenta_y_cinco"
    assert Metodos_tarea1.num_to_string(56) == "cincuenta_y_seis"
    assert Metodos_tarea1.num_to_string(57) == "cincuenta_y_siete"
    assert Metodos_tarea1.num_to_string(58) == "cincuenta_y_ocho"
    assert Metodos_tarea1.num_to_string(59) == "cincuenta_y_nueve"
    assert Metodos_tarea1.num_to_string(60) == "sesenta"
    assert Metodos_tarea1.num_to_string(61) == "sesenta_y_uno"
    assert Metodos_tarea1.num_to_string(62) == "sesenta_y_dos"
    assert Metodos_tarea1.num_to_string(63) == "sesenta_y_tres"
    assert Metodos_tarea1.num_to_string(64) == "sesenta_y_cuatro"
    assert Metodos_tarea1.num_to_string(65) == "sesenta_y_cinco"
    assert Metodos_tarea1.num_to_string(66) == "sesenta_y_seis"
    assert Metodos_tarea1.num_to_string(67) == "sesenta_y_siete"
    assert Metodos_tarea1.num_to_string(68) == "sesenta_y_ocho"
    assert Metodos_tarea1.num_to_string(69) == "sesenta_y_nueve"
    assert Metodos_tarea1.num_to_string(70) == "setenta"
    assert Metodos_tarea1.num_to_string(71) == "setenta_y_uno"
    assert Metodos_tarea1.num_to_string(72) == "setenta_y_dos"
    assert Metodos_tarea1.num_to_string(73) == "setenta_y_tres"
    assert Metodos_tarea1.num_to_string(74) == "setenta_y_cuatro"
    assert Metodos_tarea1.num_to_string(75) == "setenta_y_cinco"
    assert Metodos_tarea1.num_to_string(76) == "setenta_y_seis"
    assert Metodos_tarea1.num_to_string(77) == "setenta_y_siete"
    assert Metodos_tarea1.num_to_string(78) == "setenta_y_ocho"
    assert Metodos_tarea1.num_to_string(79) == "setenta_y_nueve"
    assert Metodos_tarea1.num_to_string(80) == "ochenta"
    assert Metodos_tarea1.num_to_string(81) == "ochenta_y_uno"
    assert Metodos_tarea1.num_to_string(82) == "ochenta_y_dos"
    assert Metodos_tarea1.num_to_string(83) == "ochenta_y_tres"
    assert Metodos_tarea1.num_to_string(84) == "ochenta_y_cuatro"
    assert Metodos_tarea1.num_to_string(85) == "ochenta_y_cinco"
    assert Metodos_tarea1.num_to_string(86) == "ochenta_y_seis"
    assert Metodos_tarea1.num_to_string(87) == "ochenta_y_siete"
    assert Metodos_tarea1.num_to_string(88) == "ochenta_y_ocho"
    assert Metodos_tarea1.num_to_string(89) == "ochenta_y_nueve"
    assert Metodos_tarea1.num_to_string(90) == "noventa"
    assert Metodos_tarea1.num_to_string(91) == "noventa_y_uno"
    assert Metodos_tarea1.num_to_string(92) == "noventa_y_dos"
    assert Metodos_tarea1.num_to_string(93) == "noventa_y_tres"
    assert Metodos_tarea1.num_to_string(94) == "noventa_y_cuatro"
    assert Metodos_tarea1.num_to_string(95) == "noventa_y_cinco"
    assert Metodos_tarea1.num_to_string(96) == "noventa_y_seis"
    assert Metodos_tarea1.num_to_string(97) == "noventa_y_siete"
    assert Metodos_tarea1.num_to_string(98) == "noventa_y_ocho"
    assert Metodos_tarea1.num_to_string(99) == "noventa_y_nueve"


# verifica que el dato de entrada de num_to_string sea un numero, si no da
# un error
def test_stringing():
    assert Metodos_tarea1.num_to_string("Hola") == 3


# verifica que si el dato de entrada de num_to_string es un numero
# negativo da un error
def test_negativ_decimal():
    assert Metodos_tarea1.num_to_string(-9) == 4
