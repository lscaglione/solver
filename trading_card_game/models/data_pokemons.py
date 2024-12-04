from .carta import CartaPokemon, CartaItem, CartaApoiador

# Função para criar cartas de Pokémon
def carregar_cartas_pokemon():
    return [
        CartaPokemon(nome="Pikachu", tipo_nivel="Básico", tipo_pokemon="Elétrico", vida_maxima=60,
                     tipo_energia="Elétrico", ataques=[{"nome": "Choque do Trovão", "dano": 20, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=["Raiochu"]),
        CartaPokemon(nome="Charmander", tipo_nivel="Básico", tipo_pokemon="Fogo", vida_maxima=50,
                     tipo_energia="Fogo", ataques=[{"nome": "Brasas", "dano": 30, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=[]),
        CartaPokemon(nome="Bulbasaur", tipo_nivel="Básico", tipo_pokemon="Planta", vida_maxima=50,
                     tipo_energia="Planta", ataques=[{"nome": "Folha Navalha", "dano": 20, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=["Ivysaur"]),
        CartaPokemon(nome="Squirtle", tipo_nivel="Básico", tipo_pokemon="Água", vida_maxima=50,
                     tipo_energia="Água", ataques=[{"nome": "Jato d'Água", "dano": 20, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=["Wartortle"]),
        CartaPokemon(nome="Raichu", tipo_nivel="Estágio 1", tipo_pokemon="Elétrico", vida_maxima=80,
                     tipo_energia="Elétrico", ataques=[{"nome": "Raio", "dano": 40, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=[]),
        CartaPokemon(nome="Charmeleon", tipo_nivel="Estágio 1", tipo_pokemon="Fogo", vida_maxima=70,
                     tipo_energia="Fogo", ataques=[{"nome": "Lança Chamas", "dano": 50, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=["Charizard"]),
        CartaPokemon(nome="Ivysaur", tipo_nivel="Estágio 1", tipo_pokemon="Planta", vida_maxima=70,
                     tipo_energia="Planta", ataques=[{"nome": "Vinha Cortante", "dano": 40, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=["Venusaur"]),
        CartaPokemon(nome="Wartortle", tipo_nivel="Estágio 1", tipo_pokemon="Água", vida_maxima=70,
                     tipo_energia="Água", ataques=[{"nome": "Raio de Água", "dano": 30, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=["Blastoise"]),
        CartaPokemon(nome="Dragonite", tipo_nivel="Estágio 2", tipo_pokemon="Dragão", vida_maxima=150,
                     tipo_energia="Dragão", ataques=[{"nome": "Dragão Destroi", "dano": 90, "custo": 3}],
                     habilidade_recuo=3, evoluivel_para=[]),
        CartaPokemon(nome="Pidgeot", tipo_nivel="Estágio 2", tipo_pokemon="Voador", vida_maxima=120,
                     tipo_energia="Voador", ataques=[{"nome": "Golpe de Asa", "dano": 50, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=[]),
        CartaPokemon(nome="Machamp", tipo_nivel="Estágio 2", tipo_pokemon="Lutador", vida_maxima=130,
                     tipo_energia="Lutador", ataques=[{"nome": "Soco Dinâmico", "dano": 80, "custo": 3}],
                     habilidade_recuo=3, evoluivel_para=[]),
        CartaPokemon(nome="Alakazam", tipo_nivel="Estágio 2", tipo_pokemon="Psíquico", vida_maxima=110,
                     tipo_energia="Psíquico", ataques=[{"nome": "Psíquico", "dano": 60, "custo": 2}],
                     habilidade_recuo=2, evoluivel_para=[]),
        CartaPokemon(nome="Golem", tipo_nivel="Estágio 2", tipo_pokemon="Terrestre", vida_maxima=150,
                     tipo_energia="Terrestre", ataques=[{"nome": "Terremoto", "dano": 100, "custo": 3}],
                     habilidade_recuo=3, evoluivel_para=[]),
        CartaPokemon(nome="Zubat", tipo_nivel="Básico", tipo_pokemon="Venenoso", vida_maxima=40,
                     tipo_energia="Venenoso", ataques=[{"nome": "Ataque Rápido", "dano": 10, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=["Golbat"]),
        CartaPokemon(nome="Jigglypuff", tipo_nivel="Básico", tipo_pokemon="Normal", vida_maxima=60,
                     tipo_energia="Normal", ataques=[{"nome": "Canto", "dano": 20, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=[]),
        CartaPokemon(nome="Psyduck", tipo_nivel="Básico", tipo_pokemon="Psíquico", vida_maxima=50,
                     tipo_energia="Psíquico", ataques=[{"nome": "Confusão", "dano": 15, "custo": 1}],
                     habilidade_recuo=1, evoluivel_para=["Golduck"]),
        CartaPokemon(nome="Electrode", tipo_nivel="Estágio 1", tipo_pokemon="Elétrico", vida_maxima=70,
                     tipo_energia="Elétrico", ataques=[{"nome": "Explosão", "dano": 60, "custo": 3}],
                     habilidade_recuo=2, evoluivel_para=[]),
        CartaPokemon(nome="Nidoking", tipo_nivel="Estágio 2", tipo_pokemon="Venenoso", vida_maxima=130,
                     tipo_energia="Venenoso", ataques=[{"nome": "Colisão", "dano": 70, "custo": 2}],
                     habilidade_recuo=3, evoluivel_para=[]),
        CartaPokemon(nome="Nidoqueen", tipo_nivel="Estágio 2", tipo_pokemon="Venenoso", vida_maxima=120,
                     tipo_energia="Venenoso", ataques=[{"nome": "Pancada", "dano": 60, "custo": 2}],
                     habilidade_recuo=3, evoluivel_para=[]),
    ]


# Função para criar cartas de itens
def carregar_cartas_item():
    return [
        CartaItem(nome="Poção", efeito=lambda alvo: setattr(alvo, "vida_atual", min(alvo.vida_maxima, alvo.vida_atual + 20))),
        CartaItem(nome="Hyper Poção", efeito=lambda alvo: setattr(alvo, "vida_atual", min(alvo.vida_maxima, alvo.vida_atual + 50))),
        CartaItem(nome="Reviver", efeito=lambda alvo: setattr(alvo, "vida_atual", alvo.vida_maxima)),
        CartaItem(nome="Pedra Evolutiva", efeito=lambda alvo: setattr(alvo, "evolucao", True)),
        CartaItem(nome="Escudo", efeito=lambda alvo: setattr(alvo, "defesa", 20)),
        CartaItem(nome="Energia Fogo", efeito=lambda alvo: alvo.adicionar_energia("Fogo")),
        CartaItem(nome="Energia Água", efeito=lambda alvo: alvo.adicionar_energia("Água")),
        CartaItem(nome="Energia Elétrica", efeito=lambda alvo: alvo.adicionar_energia("Elétrico")),
        CartaItem(nome="Energia Planta", efeito=lambda alvo: alvo.adicionar_energia("Planta")),
        CartaItem(nome="Energia Psíquica", efeito=lambda alvo: alvo.adicionar_energia("Psíquico")),
    ]

# Função para criar cartas de apoiadores
def carregar_cartas_apoiador():
    return [
        CartaApoiador(nome="Treinador", efeito=lambda jogador: jogador.comprar_carta()),
        CartaApoiador(nome="Pesquisador", efeito=lambda jogador: jogador.descartar_carta()),
        CartaApoiador(nome="Estratégia", efeito=lambda jogador: jogador.embaralhar_deck()),
        CartaApoiador(nome="Técnico", efeito=lambda jogador: jogador.pesquisar_energia()),
        CartaApoiador(nome="Vendedor", efeito=lambda jogador: jogador.adicionar_energia("Qualquer")),
        CartaApoiador(nome="Veterano", efeito=lambda jogador: jogador.adicionar_energia("Fogo")),
        CartaApoiador(nome="Apoio Estratégico", efeito=lambda jogador: jogador.mudar_turno()),
        CartaApoiador(nome="Mentor", efeito=lambda jogador: jogador.adicionar_energia("Água")),
        CartaApoiador(nome="Botânico", efeito=lambda jogador: jogador.pesquisar_cartas_de_planta()),
        CartaApoiador(nome="Capitão", efeito=lambda jogador: jogador.descartar_energia())
    ]
