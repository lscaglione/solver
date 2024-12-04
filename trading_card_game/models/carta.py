# Classe base para representar todas as cartas
class Carta:
    def __init__(self, nome, tipo, descricao):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao


# Subclasse para cartas de Pokémon
class CartaPokemon(Carta):
    def __init__(self, nome, tipo_nivel, tipo_pokemon, vida_maxima, ataques, habilidade_recuo, tipo_energia, evoluivel_para=None):
        super().__init__(nome, "Pokemon", f"Tipo: {tipo_pokemon}")
        self.tipo_nivel = tipo_nivel
        self.tipo_pokemon = tipo_pokemon
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.ataques = ataques  # Lista de ataques com custo de energia
        self.habilidade_recuo = habilidade_recuo
        self.tipo_energia = tipo_energia  # Tipo de energia necessário (ex: "Fogo", "Elétrico")
        self.energia = 0  # Energia acumulada do Pokémon
        self.evoluivel_para = evoluivel_para or []  # Lista de possíveis evoluções

    def evoluir(self, carta_evolucao):
        if carta_evolucao not in self.evoluivel_para:
            raise ValueError(f"{self.nome} não pode evoluir para {carta_evolucao.nome}.")
        self.tipo_pokemon = carta_evolucao.tipo_pokemon
        self.vida_maxima = carta_evolucao.vida_maxima
        self.vida_atual = max(0, self.vida_atual - (self.vida_maxima - carta_evolucao.vida_maxima))
        self.ataques = carta_evolucao.ataques
        self.habilidade_recuo = carta_evolucao.habilidade_recuo
        print(f"{self.nome} evoluiu para {carta_evolucao.nome}!")

    def receber_energia(self, tipo_energia, quantidade):
        """
        Método para receber energia de acordo com o tipo.
        Verifica se o tipo de energia recebido é compatível com o Pokémon.
        """
        if tipo_energia == self.tipo_energia:
            self.energia += quantidade
            print(f"{self.nome} recebeu {quantidade} de energia do tipo {tipo_energia}.")
        else:
            print(f"{self.nome} não pode receber energia do tipo {tipo_energia}, pois ele é do tipo {self.tipo_energia}.")

    def atacar(self, pokemon_adversario, ataque_escolhido, campo_batalha):
        """
        Método para atacar um Pokémon adversário, verificando se o Pokémon tem energia suficiente.
        O dano é calculado com base no poder do ataque.
        """
        if self.vida_atual <= 0:
            print(f"{self.nome} não pode atacar porque está sem vida!")
            return

        # Verificar se o Pokémon tem energia suficiente do tipo correto
        if campo_batalha.tem_energia_suficiente(self.tipo_energia, ataque_escolhido['custo_energia']):
            dano = ataque_escolhido['poder']  # Usando o poder do ataque
            print(f"{self.nome} atacou {pokemon_adversario.nome} com o ataque {ataque_escolhido['nome']} causando {dano} de dano!")

            # Reduzindo a vida do Pokémon adversário
            pokemon_adversario.vida_atual -= dano
            pokemon_adversario.vida_atual = max(0, pokemon_adversario.vida_atual)  # Vida não pode ser negativa
            print(f"{pokemon_adversario.nome} agora tem {pokemon_adversario.vida_atual} de vida restante.")
        else:
            print(f"{self.nome} não tem energia suficiente para usar {ataque_escolhido['nome']}!")

    def recuar(self, campo_batalha):
        """
        Método para realizar o recuo, reduzindo a energia conforme o custo do recuo.
        O recuo só ocorre se houver energia suficiente.
        """
        if campo_batalha.tem_energia_suficiente(self.tipo_energia, self.habilidade_recuo):
            campo_batalha.reduzir_energia(self.tipo_energia, self.habilidade_recuo)
            print(f"{self.nome} recuou, gastando {self.habilidade_recuo} de energia.")
        else:
            print(f"{self.nome} não tem energia suficiente para recuar!")

    def esta_vivo(self):
        return self.vida_atual > 0




# Subclasse para cartas de Item
class CartaItem(Carta):
    def __init__(self, nome, efeito):
        super().__init__(nome, "Item", "Carta de item.")
        self.efeito = efeito

    def usar(self, alvo):
        print(f"Usando o item {self.nome} em {alvo.nome}.")
        self.efeito(alvo)


# Subclasse para cartas de Apoiador
class CartaApoiador(Carta):
    def __init__(self, nome, efeito):
        super().__init__(nome, "Apoiador", "Carta de apoiador.")
        self.efeito = efeito

    def usar(self, jogador):
        print(f"{jogador.nome} usou a carta apoiador {self.nome}.")
        self.efeito(jogador)