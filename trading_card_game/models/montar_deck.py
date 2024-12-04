# Função para montar o deck com as restrições
def montar_deck(cartas_pokemon, cartas_item, cartas_apoiador, tipos_de_energia):
    """
    Função que monta um deck de cartas. Agora inclui a escolha do tipo de energia.
    O deck será limitado a 20 cartas.
    """
    deck = []
    for tipo in tipos_de_energia:
        for carta in cartas_pokemon:
            if carta.tipo_energia == tipo:
                deck.append(carta)  # Adiciona apenas Pokémon com o tipo de energia correto

    # Adiciona cartas de item e apoiador
    deck.extend(cartas_item)
    deck.extend(cartas_apoiador)

    # Se o deck passar de 20 cartas, cortamos o excesso
    if len(deck) > 20:
        deck = deck[:20]  # Limita a 20 cartas

    return deck
