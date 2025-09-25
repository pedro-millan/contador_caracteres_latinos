import main_contador as cc

def test_eliminar_tildes():
    assert cc.eliminar_tildes("canción") == "cancion"
    assert cc.eliminar_tildes("pingüino") == "pinguino"
    assert cc.eliminar_tildes("Árbol") == "Arbol"

def test_contar_caracteres_simple():
    texto = "Hola Hola"
    resultado = cc.contar_caracteres(texto)

    assert resultado["h"] == 2
    assert resultado["o"] == 2
    assert resultado["l"] == 2
    assert resultado["a"] == 2

def test_contar_caracteres_con_tildes():
    texto = "canción"
    resultado = cc.contar_caracteres(texto)

    # la ó debe convertirse en o gracias a eliminar_tildes
    assert "o" in resultado
    assert resultado["o"] == 1

