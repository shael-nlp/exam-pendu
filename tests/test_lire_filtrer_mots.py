import pytest
from generate_dicts import lire_filtrer_mots

def test_lire_filtrer_mots_empty():
    """Teste la fonction avec un fichier vide"""
    with pytest.raises(ValueError):
        lire_filtrer_mots(
            chemin_lexique="data_test/filetest_empty.txt",
            longueur=6
        )

def test_lire_filtrer_mots_longueur():
    """Vérifie que la longueur des mots."""
    for word in range(len(lire_filtrer_mots(
            chemin_lexique="data_test/filetest1.txt",
            longueur=6))):
        assert len(lire_filtrer_mots(
            chemin_lexique="data_test/filetest1.txt",
            longueur=6
        )[word]) == 6

def test_lire_filtrer_mots_special():
    """Vérifie que les mots ne contiennent pas de caractères spéciaux tels que des accents, espaces ou tirets."""
    assert lire_filtrer_mots(
        chemin_lexique="data_test/filetest1.txt",
        longueur=4,
    )[0] == "EPEE"
