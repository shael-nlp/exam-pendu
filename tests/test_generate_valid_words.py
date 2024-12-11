import pytest
from solver import generate_valid_words

def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_generate_valid_words_empty():
    """Test sur une liste vide"""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == []

def test_generate_valid_words_stable():
    """Vérifie que la liste reste inchangée si l'utilisateur ne joue pas."""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_generate_valid_words_lettres_exclues_et_presentes():
    """Test de condition de jeu normal. (Avec lettres exclues et présentes)"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('P', 0)],
        letters_not_in_secret=["A", "N"]
    ) == ["PORTER"]



