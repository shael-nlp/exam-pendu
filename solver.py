def generate_valid_words(possible_words:list[str], letters_in_secret:list[tuple[str, int]], letters_not_in_secret:list[str]) -> list[str]:
    """
    Génère une liste de mots qui sont encore valides en fonction des lettres déjà jouées.
    """
    return [word for word in possible_words if all(word[position] == l for l, position in letters_in_secret)
            and not any(l in word for l in letters_not_in_secret)]

def generate_best_letters(possible_words:list[str], letters_not_played:list[str], letters_in_secret:[list[str]], letters_not_in_secret:[list[str]]) -> str:
    """
    Calcule la meilleure lettre à jouer à partir de la
    fréquence moyenne des lettres contenues dans les mots encore en jeu
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





