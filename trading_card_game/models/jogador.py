class Jogador:
    def __init__(self, nome, deck):
        self.nome = nome
        self.deck = deck
        self.mao = []  # Cartas na mão
        self.vida = 100  # Exemplo de vida do jogador
        self.pokemon_ativo = None

    def comprar_carta(self):
        if self.deck:
            carta_comprada = self.deck.pop(0)
            self.mao.append(carta_comprada)
            print(f"{self.nome} comprou a carta {carta_comprada.nome}.")

    def fazer_acao(self):
        # Aqui pode ser onde você permite que o jogador use cartas ou ataque
        if self.mao:
            carta = self.mao[0]
            print(f"{self.nome} usou a carta {carta.nome}.")
            # Lógica de ataque ou uso de carta
            self.mao.pop(0)

    def verificar_vitoria(self):
        # Verifica se o jogador tem cartas no deck
        if len(self.deck) == 0:
            return True
        return False
