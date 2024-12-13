def generate_valid_words(possible_words:list[str], letters_in_secret:list[tuple[str, int]], letters_not_in_secret:list[str]) -> list[str]:
    """
    Génère une liste de mots valides en fonction des lettres déjà jouées.

    Entrée:
    ----------
    possible_words : List[str]
        Liste de mots.
    letters_in_secret : List[Tuple[str, int]]
        Liste de tuples (lettre, position) indiquant les lettres et
        leurs positions dans le mot secret.
    letters_not_in_secret : List[str]
        Liste de lettres absentes du mot secret.

    Sortie:
    ----------
    List[str]
        Liste de mots encore valides.
    """
    return [word for word in possible_words if all(word[position] == l for l, position in letters_in_secret)
            and not any(l in word for l in letters_not_in_secret)]

def generate_best_letters(possible_words:list[str], letters_not_played:list[str], letters_not_in_secret:[list[str]]) -> str:
    """
    Calcule la meilleure lettre à jouer à partir de la
    fréquence moyenne des lettres contenues dans les mots encore valides.

    Entrée:
    ----------
    possible_words : List[str]
        Liste des mots encore possibles après filtrage par generate_valid_words
    letters_not_played : List[str]
        Liste des lettres pas encore jouées.
    letters_not_in_secret : List[str]
        Liste de lettres absentes du mot secret.

    Sortie:
    ----------
    str
        Une chaine de caractère contenant une seule lettre.
    """
    letters = [l for l in letters_not_played if l not in letters_not_in_secret]
    nombre_de_mots = len(possible_words)
    best_letter = None
    best_freq = -1
    for l in letters:
        freq = sum(mot.count(l) for mot in possible_words) / nombre_de_mots
        if freq > best_freq:
            best_freq = freq
            best_letter = l
    return f"Essayez de jouer la lettre '{best_letter}' !"





