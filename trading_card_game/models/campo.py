# Classe para o campo de batalha
class CampoDeBatalha:
    def __init__(self, tipos_de_energia):
        """
        Inicializa o campo de batalha com um dicionário de energias disponíveis por tipo de energia.
        `tipos_de_energia` é uma lista dos tipos de energia disponíveis no jogo (por exemplo, ["Fogo", "Elétrico"]).
        """
        self.energia_disponivel = {tipo: 0 for tipo in tipos_de_energia}  # Inicializa o banco de energia
        self.energia_alocada = {tipo: 0 for tipo in tipos_de_energia}  # Energia alocada (para controle)

    def gerar_energia(self):
        """
        Gera energia no banco de energia no início de cada turno.
        Gera 1 de energia para cada tipo de energia disponível no campo de batalha.
        """
        for tipo in self.energia_disponivel:
            self.energia_disponivel[tipo] += 1  # Aumenta a energia disponível para cada tipo
            print(f"Banco de energia gerou 1 de energia do tipo {tipo}.")

    def distribuir_energia(self, pokemon, tipo_energia, quantidade):
        """
        Distribui energia gerada para um Pokémon ativo ou no banco.
        Verifica se o tipo de energia está disponível no banco.
        """
        if self.energia_disponivel.get(tipo_energia, 0) >= quantidade:
            pokemon.receber_energia(tipo_energia, quantidade)  # O Pokémon recebe energia
            self.energia_disponivel[tipo_energia] -= quantidade  # Reduz a energia do banco
            self.energia_alocada[tipo_energia] += quantidade  # Marca a energia como alocada
            print(f"{quantidade} de energia do tipo {tipo_energia} foi distribuído para {pokemon.nome}.")
        else:
            print(f"Não há energia suficiente do tipo {tipo_energia}.")

    def finalizar_turno(self):
        """
        Finaliza o turno, verificando se a energia foi alocada.
        Caso a energia não tenha sido alocada, ela é perdida.
        """
        for tipo in self.energia_disponivel:
            if self.energia_alocada[tipo] < self.energia_disponivel[tipo]:
                energia_nao_alocada = self.energia_disponivel[tipo] - self.energia_alocada[tipo]
                self.energia_disponivel[tipo] -= energia_nao_alocada  # Descartar a energia não alocada
                print(f"{energia_nao_alocada} de energia do tipo {tipo} foi perdida por não ter sido alocada.")

        # Resetar a energia alocada para o próximo turno
        self.energia_alocada = {tipo: 0 for tipo in self.energia_alocada}
