# Pokémon Team Builder & Battle

Aplicativo em Python + Tkinter para montar uma equipe de 6 Pokémon, filtrar por tipo, visualizar os cards com sprites locais e batalhar contra o computador.

## Funcionalidades

- Seleção de Pokémon em cards
- Filtro por tipo
- Busca por nome
- Montagem de time com 6 Pokémon
- Resumo da equipe antes do duelo
- Batalha por turno
- HP em barras visuais
- Sprites locais da pasta `sprites/`
- Interface em estilo game-like

## Estrutura do projeto

- `main.py` — lógica principal da interface e da batalha
- `sprites/` — imagens dos Pokémon em formato `.png`
- `ash.png` — imagem do treinador Ash

## Requisitos

- Python 3.9+
- Tkinter (vem com a instalação do Python em versões padrão)

## Como executar

Na pasta do projeto:

```bash
python main.py
```

## Observações

- Os sprites são carregados localmente a partir da pasta `sprites/`.
- O nome do arquivo do Pokémon deve seguir o número correspondente na Pokédex (ex.: `25.png` para Pikachu, `1.png` para Bulbasaur, `151.png` para Mew).
- Se a pasta `sprites/` estiver vazia ou faltando algum arquivo, o app usa o emoji do tipo como fallback visual.

## Fluxo do jogo

1. Escolha Pokémon para o time
2. Filtre por tipo ou busque pelo nome
3. Monte 6 Pokémon
4. Veja o resumo da equipe
5. Inicie a batalha
6. Escolha o ataque do Pokémon ativo
7. Continue até vencer ou perder

## Autor

Projeto pessoal de interface e batalha Pokémon em Tkinter.
