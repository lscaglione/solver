from models.jogador import Jogador
from models.campo import CampoDeBatalha
from models.data_pokemons import carregar_cartas_pokemon, carregar_cartas_item, carregar_cartas_apoiador
from models.montar_deck import montar_deck  # Importa a função de montagem do deck

# Função principal do jogo
def jogo(cartas_pokemon, cartas_item, cartas_apoiador):
    # Criar jogadores
    jogador1 = Jogador("Ash", deck=montar_deck(cartas_pokemon, cartas_item, cartas_apoiador, tipos_de_energia=["Fogo", "Elétrico"]))
    jogador2 = Jogador("Gary", deck=montar_deck(cartas_pokemon, cartas_item, cartas_apoiador, tipos_de_energia=["Fogo", "Elétrico"]))

    jogadores = [jogador1, jogador2]
    turno = 0

    # Inicializando o campo de batalha
    campo_batalha = CampoDeBatalha(tipos_de_energia=["Fogo", "Elétrico"])

    # Loop de turnos
    while True:
        jogador_atual = jogadores[turno % 2]
        adversario = jogadores[(turno + 1) % 2]

        print(f"É o turno de {jogador_atual.nome}")

        # Lógica do turno
        jogador_atual.comprar_carta()
        jogador_atual.fazer_acao()

        # Verificar condições de vitória
        if jogador_atual.verificar_vitoria():
            print(f"{jogador_atual.nome} venceu!")
            break

        # Gerar energia e distribuir para o jogador atual
        campo_batalha.gerar_energia()
        campo_batalha.distribuir_energia(jogador_atual.pokemon_ativo, "Fogo", 1)

        # Finalizar o turno
        campo_batalha.finalizar_turno()

        # Alternar turno
        turno += 1
        print("\n")  # Quebra de linha para separar os turnos


# Função principal para iniciar o jogo
def main():
    # Carregar cartas
    cartas_pokemon = carregar_cartas_pokemon()  # Já assume que carrega uma lista de cartas Pokémon
    cartas_item = carregar_cartas_item()  # Similar para itens
    cartas_apoiador = carregar_cartas_apoiador()  # E para os apoiadores

    # Iniciar o jogo
    print("O jogo começou!")
    jogo(cartas_pokemon, cartas_item, cartas_apoiador)


if __name__ == "__main__":
    main()
