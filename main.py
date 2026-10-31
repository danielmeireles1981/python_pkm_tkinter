import os
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Banco de Dados Completo com os 151 Pokémon da 1ª Geração (Kanto)
POKEDEX = {
    "Bulbasaur": {"tipo": "Planta", "hp": 45, "atk": 49, "def": 49, "vel": 45, "movimentos": [("Chicote de Cipó", 15), ("Investida", 10)]},
    "Ivysaur": {"tipo": "Planta", "hp": 60, "atk": 62, "def": 63, "vel": 60, "movimentos": [("Razor Leaf", 25), ("Investida", 10)]},
    "Venusaur": {"tipo": "Planta", "hp": 80, "atk": 82, "def": 83, "vel": 80, "movimentos": [("SolarBeam", 35), ("Chicote de Cipó", 15)]},
    "Charmander": {"tipo": "Fogo", "hp": 39, "atk": 52, "def": 43, "vel": 65, "movimentos": [("Brasa", 15), ("Arranhão", 10)]},
    "Charmeleon": {"tipo": "Fogo", "hp": 58, "atk": 64, "def": 58, "vel": 80, "movimentos": [("Lança-Chamas", 25), ("Brasa", 15)]},
    "Charizard": {"tipo": "Fogo", "hp": 78, "atk": 84, "def": 78, "vel": 100, "movimentos": [("Flamethrower", 35), ("Dragon Claw", 30)]},
    "Squirtle": {"tipo": "Água", "hp": 44, "atk": 48, "def": 65, "vel": 43, "movimentos": [("Jato de Água", 15), ("Investida", 10)]},
    "Wartortle": {"tipo": "Água", "hp": 59, "atk": 63, "def": 80, "vel": 58, "movimentos": [("Water Pulse", 25), ("Jato de Água", 15)]},
    "Blastoise": {"tipo": "Água", "hp": 79, "atk": 83, "def": 100, "vel": 78, "movimentos": [("Hidrobomba", 35), ("Surf", 30)]},
    "Caterpie": {"tipo": "Inseto", "hp": 45, "atk": 30, "def": 35, "vel": 45, "movimentos": [("Investida", 8), ("Pancada", 10)]},
    "Metapod": {"tipo": "Inseto", "hp": 50, "atk": 20, "def": 55, "vel": 30, "movimentos": [("Investida", 5), ("Esfera", 8)]},
    "Butterfree": {"tipo": "Inseto", "hp": 60, "atk": 45, "def": 50, "vel": 70, "movimentos": [("Confusão", 20), ("Rajada de Vento", 18)]},
    "Weedle": {"tipo": "Inseto", "hp": 40, "atk": 35, "def": 30, "vel": 50, "movimentos": [("Picada Venenosa", 12), ("Investida", 8)]},
    "Kakuna": {"tipo": "Inseto", "hp": 45, "atk": 25, "def": 50, "vel": 35, "movimentos": [("Investida", 5), ("Ferroada", 8)]},
    "Beedrill": {"tipo": "Inseto", "hp": 65, "atk": 90, "def": 40, "vel": 75, "movimentos": [("Míssil de Agulhas", 25), ("Picada Venenosa", 15)]},
    "Pidgey": {"tipo": "Normal", "hp": 40, "atk": 45, "def": 40, "vel": 56, "movimentos": [("Investida", 10), ("Ataque Rápido", 12)]},
    "Pidgeotto": {"tipo": "Normal", "hp": 63, "atk": 60, "def": 55, "vel": 71, "movimentos": [("Investida", 10), ("Asa de Aço", 20)]},
    "Pidgeot": {"tipo": "Normal", "hp": 83, "atk": 80, "def": 75, "vel": 101, "movimentos": [("Ataque Rápido", 12), ("Furacão", 30)]},
    "Rattata": {"tipo": "Normal", "hp": 30, "atk": 56, "def": 35, "vel": 72, "movimentos": [("Investida", 10),("Mordida", 12)]},
    "Raticate": {"tipo": "Normal", "hp": 55, "atk": 81, "def": 60, "vel": 97, "movimentos": [("Hyper Fang", 25), ("Mordida", 15)]},
    "Spearow": {"tipo": "Normal", "hp": 40, "atk": 60, "def": 30, "vel": 70, "movimentos": [("Bicada", 12), ("Investida", 10)]},
    "Fearow": {"tipo": "Normal", "hp": 65, "atk": 90, "def": 65, "vel": 100, "movimentos": [("Perfurar", 25), ("Bicada", 15)]},
    "Ekans": {"tipo": "Veneno", "hp": 35, "atk": 60, "def": 44, "vel": 55, "movimentos": [("Picada Venenosa", 12), ("Mordida", 12)]},
    "Arbok": {"tipo": "Veneno", "hp": 60, "atk": 85, "def": 69, "vel": 80, "movimentos": [("Mordida", 15), ("Aperto", 22)]},
    "Pikachu": {"tipo": "Elétrico", "hp": 35, "atk": 55, "def": 40, "vel": 90, "movimentos": [("Choque do Trovão", 15), ("Ataque Rápido", 12)]},
    "Raichu": {"tipo": "Elétrico", "hp": 60, "atk": 90, "def": 55, "vel": 110, "movimentos": [("Relâmpago", 25), ("Investida Trovão", 30)]},
    "Sandshrew": {"tipo": "Terra", "hp": 50, "atk": 75, "def": 85, "vel": 40, "movimentos": [("Arranhão", 10), ("Investida", 10)]},
    "Sandslash": {"tipo": "Terra", "hp": 75, "atk": 100, "def": 110, "vel": 65, "movimentos": [("Cortar", 20), ("Terremoto", 35)]},
    "Nidoran (F)": {"tipo": "Veneno", "hp": 55, "atk": 47, "def": 52, "vel": 41, "movimentos": [("Arranhão", 10), ("Picada Venenosa", 12)]},
    "Nidorina": {"tipo": "Veneno", "hp": 70, "atk": 62, "def": 67, "vel": 56, "movimentos": [("Mordida", 12), ("Picada Venenosa", 15)]},
    "Nidoqueen": {"tipo": "Veneno", "hp": 90, "atk": 92, "def": 87, "vel": 76, "movimentos": [("Body Slam", 25), ("Terremoto", 35)]},
    "Nidoran (M)": {"tipo": "Veneno", "hp": 46, "atk": 57, "def": 40, "vel": 50, "movimentos": [("Bicada", 10), ("Investida", 10)]},
    "Nidorino": {"tipo": "Veneno", "hp": 61, "atk": 72, "def": 57, "vel": 65, "movimentos": [("Chifrada", 18), ("Picada Venenosa", 15)]},
    "Nidoking": {"tipo": "Veneno", "hp": 81, "atk": 102, "def": 77, "vel": 85, "movimentos": [("Megahorn", 30), ("Terremoto", 35)]},
    "Clefairy": {"tipo": "Fada", "hp": 70, "atk": 45, "def": 48, "vel": 35, "movimentos": [("Pancada", 10), ("Tapa", 12)]},
    "Clefable": {"tipo": "Fada", "hp": 95, "atk": 70, "def": 73, "vel": 60, "movimentos": [("Metrônomo", 25), ("Força Lunar", 30)]},
    "Vulpix": {"tipo": "Fogo", "hp": 38, "atk": 41, "def": 40, "vel": 65, "movimentos": [("Brasa", 15), ("Ataque Rápido", 12)]},
    "Ninetales": {"tipo": "Fogo", "hp": 73, "atk": 76, "def": 75, "vel": 100, "movimentos": [("Lança-Chamas", 25), ("Brasa", 15)]},
    "Jigglypuff": {"tipo": "Normal", "hp": 115, "atk": 45, "def": 20, "vel": 20, "movimentos": [("Tapa", 10), ("Investida", 10)]},
    "Wigglytuff": {"tipo": "Normal", "hp": 140, "atk": 70, "def": 45, "vel": 45, "movimentos": [("Body Slam", 25), ("Hyper Beam", 40)]},
    "Zubat": {"tipo": "Veneno", "hp": 40, "atk": 45, "def": 35, "vel": 55, "movimentos": [("Bicada", 12), ("Mordida", 12)]},
    "Golbat": {"tipo": "Veneno", "hp": 75, "atk": 80, "def": 70, "vel": 90, "movimentos": [("Mordida", 15), ("Asa Cortante", 25)]},
    "Oddish": {"tipo": "Planta", "hp": 45, "atk": 50, "def": 55, "vel": 30, "movimentos": [("Absorver", 15), ("Investida", 10)]},
    "Gloom": {"tipo": "Planta", "hp": 60, "atk": 65, "def": 70, "vel": 40, "movimentos": [("Mega Dreno", 22), ("Absorver", 15)]},
    "Vileplume": {"tipo": "Planta", "hp": 75, "atk": 80, "def": 85, "vel": 50, "movimentos": [("SolarBeam", 35), ("Mega Dreno", 22)]},
    "Paras": {"tipo": "Inseto", "hp": 35, "atk": 70, "def": 55, "vel": 25, "movimentos": [("Arranhão", 10), ("Picada", 12)]},
    "Parasect": {"tipo": "Inseto", "hp": 60, "atk": 95, "def": 80, "vel": 30, "movimentos": [("Cortar", 20), ("X-Scissor", 28)]},
    "Venonat": {"tipo": "Inseto", "hp": 60, "atk": 55, "def": 50, "vel": 45, "movimentos": [("Investida", 10), ("Confusão", 20)]},
    "Venomoth": {"tipo": "Inseto", "hp": 70, "atk": 65, "def": 60, "vel": 90, "movimentos": [("Psiquismo", 30), ("Picada Venenosa", 15)]},
    "Diglett": {"tipo": "Terra", "hp": 10, "atk": 55, "def": 25, "vel": 95, "movimentos": [("Arranhão", 10), ("Investida", 10)]},
    "Dugtrio": {"tipo": "Terra", "hp": 35, "atk": 80, "def": 50, "vel": 120, "movimentos": [("Terremoto", 35), ("Investida", 10)]},
    "Meowth": {"tipo": "Normal", "hp": 40, "atk": 45, "def": 35, "vel": 90, "movimentos": [("Arranhão", 10), ("Mordida", 12)]},
    "Persian": {"tipo": "Normal", "hp": 65, "atk": 70, "def": 60, "vel": 115, "movimentos": [("Cortar", 20), ("Ataque Rápido", 12)]},
    "Psyduck": {"tipo": "Água", "hp": 50, "atk": 52, "def": 48, "vel": 55, "movimentos": [("Jato de Água", 15), ("Arranhão", 10)]},
    "Golduck": {"tipo": "Água", "hp": 80, "atk": 82, "def": 78, "vel": 85, "movimentos": [("Hidrobomba", 35), ("Surf", 30)]},
    "Mankey": {"tipo": "Lutador", "hp": 40, "atk": 80, "def": 35, "vel": 70, "movimentos": [("Soco", 12), ("Chute", 12)]},
    "Primeape": {"tipo": "Lutador", "hp": 65, "atk": 105, "def": 60, "vel": 95, "movimentos": [("Mega Soco", 25), ("Soco Cruzado", 28)]},
    "Growlithe": {"tipo": "Fogo", "hp": 55, "atk": 70, "def": 45, "vel": 60, "movimentos": [("Brasa", 15), ("Mordida", 12)]},
    "Arcanine": {"tipo": "Fogo", "hp": 90, "atk": 110, "def": 80, "vel": 95, "movimentos": [("Lança-Chamas", 25), ("Extremspeed", 32)]},
    "Poliwag": {"tipo": "Água", "hp": 40, "atk": 50, "def": 40, "vel": 90, "movimentos": [("Jato de Água", 15), ("Investida", 10)]},
    "Poliwhirl": {"tipo": "Água", "hp": 65, "atk": 65, "def": 65, "vel": 90, "movimentos": [("Water Pulse", 25), ("Jato de Água", 15)]},
    "Poliwrath": {"tipo": "Água", "hp": 90, "atk": 95, "def": 95, "vel": 70, "movimentos": [("Hidrobomba", 35), ("Soco Dinâmico", 30)]},
    "Abra": {"tipo": "Psíquico", "hp": 25, "atk": 20, "def": 15, "vel": 90, "movimentos": [("Confusão", 15), ("Investida", 5)]},
    "Kadabra": {"tipo": "Psíquico", "hp": 40, "atk": 35, "def": 30, "vel": 105, "movimentos": [("Psiquismo", 30), ("Confusão", 15)]},
    "Alakazam": {"tipo": "Psíquico", "hp": 55, "atk": 50, "def": 45, "vel": 120, "movimentos": [("Psiquismo", 35), ("Psybeam", 25)]},
    "Machop": {"tipo": "Lutador", "hp": 70, "atk": 80, "def": 50, "vel": 35, "movimentos": [("Soco", 12), ("Investida", 10)]},
    "Machoke": {"tipo": "Lutador", "hp": 80, "atk": 100, "def": 70, "vel": 45, "movimentos": [("Mega Soco", 25), ("Soco", 15)]},
    "Machamp": {"tipo": "Lutador", "hp": 90, "atk": 130, "def": 80, "vel": 55, "movimentos": [("Soco Dinâmico", 35), ("Mega Soco", 25)]},
    "Bellsprout": {"tipo": "Planta", "hp": 50, "atk": 75, "def": 35, "vel": 40, "movimentos": [("Chicote de Cipó", 15), ("Absorver", 15)]},
    "Weepinbell": {"tipo": "Planta", "hp": 65, "atk": 90, "def": 50, "vel": 55, "movimentos": [("Razor Leaf", 25), ("Chicote de Cipó", 15)]},
    "Victreebel": {"tipo": "Planta", "hp": 80, "atk": 105, "def": 65, "vel": 70, "movimentos": [("SolarBeam", 35), ("Razor Leaf", 25)]},
    "Tentacool": {"tipo": "Água", "hp": 40, "atk": 40, "def": 35, "vel": 70, "movimentos": [("Jato de Água", 15), ("Picada Venenosa", 12)]},
    "Tentacruel": {"tipo": "Água", "hp": 80, "atk": 70, "def": 65, "vel": 100, "movimentos": [("Surf", 30), ("Hidrobomba", 35)]},
    "Geodude": {"tipo": "Pedra", "hp": 40, "atk": 80, "def": 100, "vel": 20, "movimentos": [("Investida", 10), ("Lançamento de Rocha", 20)]},
    "Graveler": {"tipo": "Pedra", "hp": 55, "atk": 95, "def": 115, "vel": 35, "movimentos": [("Rock Slide", 25), ("Terremoto", 35)]},
    "Golem": {"tipo": "Pedra", "hp": 80, "atk": 120, "def": 130, "vel": 45, "movimentos": [("Terremoto", 35), ("Rock Slide", 25)]},
    "Ponyta": {"tipo": "Fogo", "hp": 50, "atk": 85, "def": 55, "vel": 90, "movimentos": [("Investida", 10), ("Brasa", 15)]},
    "Rapidash": {"tipo": "Fogo", "hp": 65, "atk": 100, "def": 70, "vel": 105, "movimentos": [("Flame Charge", 25), ("Lança-Chamas", 25)]},
    "Slowpoke": {"tipo": "Água", "hp": 90, "atk": 65, "def": 65, "vel": 15, "movimentos": [("Confusão", 15), ("Jato de Água", 15)]},
    "Slowbro": {"tipo": "Água", "hp": 95, "atk": 75, "def": 110, "vel": 30, "movimentos": [("Surf", 30), ("Psiquismo", 30)]},
    "Magnemite": {"tipo": "Elétrico", "hp": 25, "atk": 35, "def": 70, "vel": 45, "movimentos": [("Choque do Trovão", 15), ("Investida", 10)]},
    "Magneton": {"tipo": "Elétrico", "hp": 50, "atk": 60, "def": 95, "vel": 70, "movimentos": [("Relâmpago", 25), ("Choque do Trovão", 15)]},
    "Farfetch'd": {"tipo": "Normal", "hp": 52, "atk": 90, "def": 55, "vel": 60, "movimentos": [("Cortar", 20), ("Investida", 10)]},
    "Doduo": {"tipo": "Normal", "hp": 35, "atk": 85, "def": 45, "vel": 75, "movimentos": [("Bicada", 12), ("Investida", 10)]},
    "Dodrio": {"tipo": "Normal", "hp": 60, "atk": 110, "def": 70, "vel": 100, "movimentos": [("Perfurar", 25), ("Bicada", 15)]},
    "Seel": {"tipo": "Água", "hp": 65, "atk": 45, "def": 55, "vel": 45, "movimentos": [("Investida", 10), ("Jato de Água", 15)]},
    "Dewgong": {"tipo": "Água", "hp": 90, "atk": 70, "def": 80, "vel": 70, "movimentos": [("Surf", 30), ("Ice Beam", 30)]},
    "Grimer": {"tipo": "Veneno", "hp": 80, "atk": 80, "def": 50, "vel": 25, "movimentos": [("Investida", 10), ("Lama", 15)]},
    "Muk": {"tipo": "Veneno", "hp": 105, "atk": 105, "def": 75, "vel": 50, "movimentos": [("Lama", 20), ("Gunk Shot", 35)]},
    "Shellder": {"tipo": "Água", "hp": 30, "atk": 65, "def": 100, "vel": 40, "movimentos": [("Investida", 10), ("Water Pulse", 22)]},
    "Cloyster": {"tipo": "Água", "hp": 50, "atk": 95, "def": 180, "vel": 70, "movimentos": [("Hidrobomba", 35), ("Ice Beam", 30)]},
    "Gastly": {"tipo": "Fantasma", "hp": 30, "atk": 35, "def": 30, "vel": 80, "movimentos": [("Língua", 10), ("Bola Sombria", 20)]},
    "Haunter": {"tipo": "Fantasma", "hp": 45, "atk": 50, "def": 45, "vel": 95, "movimentos": [("Bola Sombria", 25), ("Língua", 12)]},
    "Gengar": {"tipo": "Fantasma", "hp": 60, "atk": 65, "def": 60, "vel": 110, "movimentos": [("Bola Sombria", 30), ("Língua", 15)]},
    "Onix": {"tipo": "Pedra", "hp": 35, "atk": 45, "def": 160, "vel": 70, "movimentos": [("Investida", 10), ("Lançamento de Rocha", 20)]},
    "Drowzee": {"tipo": "Psíquico", "hp": 60, "atk": 48, "def": 45, "vel": 42, "movimentos": [("Confusão", 15), ("Investida", 10)]},
    "Hypno": {"tipo": "Psíquico", "hp": 85, "atk": 73, "def": 70, "vel": 67, "movimentos": [("Psiquismo", 30), ("Confusão", 15)]},
    "Krabby": {"tipo": "Água", "hp": 30, "atk": 105, "def": 90, "vel": 50, "movimentos": [("Arranhão", 10), ("Jato de Água", 15)]},
    "Kingler": {"tipo": "Água", "hp": 55, "atk": 130, "def": 115, "vel": 75, "movimentos": [("Surf", 30), ("Crabhammer", 35)]},
    "Voltorb": {"tipo": "Elétrico", "hp": 40, "atk": 30, "def": 50, "vel": 100, "movimentos": [("Investida", 10), ("Choque do Trovão", 15)]},
    "Electrode": {"tipo": "Elétrico", "hp": 60, "atk": 50, "def": 70, "vel": 140, "movimentos": [("Relâmpago", 25), ("Explosão", 45)]},
    "Exeggcute": {"tipo": "Planta", "hp": 60, "atk": 40, "def": 80, "vel": 40, "movimentos": [("Absorver", 15), ("Confusão", 15)]},
    "Exeggutor": {"tipo": "Planta", "hp": 95, "atk": 95, "def": 85, "vel": 55, "movimentos": [("SolarBeam", 35), ("Psiquismo", 30)]},
    "Cubone": {"tipo": "Terra", "hp": 50, "atk": 50, "def": 95, "vel": 35, "movimentos": [("Investida", 10), ("Bone Club", 20)]},
    "Marowak": {"tipo": "Terra", "hp": 60, "atk": 80, "def": 110, "vel": 45, "movimentos": [("Terremoto", 35), ("Bone Club", 20)]},
    "Hitmonlee": {"tipo": "Lutador", "hp": 50, "atk": 120, "def": 53, "vel": 87, "movimentos": [("Chute", 15), ("Mega Chute", 28)]},
    "Hitmonchan": {"tipo": "Lutador", "hp": 50, "atk": 105, "def": 79, "vel": 76, "movimentos": [("Soco", 15), ("Mega Soco", 25)]},
    "Lickitung": {"tipo": "Normal", "hp": 90, "atk": 55, "def": 75, "vel": 30, "movimentos": [("Língua", 15), ("Body Slam", 25)]},
    "Koffing": {"tipo": "Veneno", "hp": 40, "atk": 65, "def": 95, "vel": 35, "movimentos": [("Lama", 15), ("Investida", 10)]},
    "Weezing": {"tipo": "Veneno", "hp": 65, "atk": 90, "def": 120, "vel": 60, "movimentos": [("Gunk Shot", 35), ("Lama", 20)]},
    "Rhyhorn": {"tipo": "Terra", "hp": 80, "atk": 85, "def": 95, "vel": 25, "movimentos": [("Investida", 10), ("Chifrada", 18)]},
    "Rhydon": {"tipo": "Terra", "hp": 105, "atk": 130, "def": 120, "vel": 40, "movimentos": [("Terremoto", 35), ("Rock Slide", 25)]},
    "Chansey": {"tipo": "Normal", "hp": 250, "atk": 5, "def": 5, "vel": 50, "movimentos": [("Tapa", 10), ("Hyper Beam", 30)]},
    "Tangela": {"tipo": "Planta", "hp": 65, "atk": 55, "def": 115, "vel": 60, "movimentos": [("Chicote de Cipó", 15), ("Mega Dreno", 22)]},
    "Kangaskhan": {"tipo": "Normal", "hp": 105, "atk": 95, "def": 80, "vel": 90, "movimentos": [("Body Slam", 25), ("Mega Soco", 25)]},
    "Horsea": {"tipo": "Água", "hp": 30, "atk": 40, "def": 70, "vel": 60, "movimentos": [("Jato de Água", 15), ("Investida", 10)]},
    "Seadra": {"tipo": "Água", "hp": 55, "atk": 65, "def": 95, "vel": 85, "movimentos": [("Surf", 30), ("Water Pulse", 22)]},
    "Goldeen": {"tipo": "Água", "hp": 45, "atk": 67, "def": 60, "vel": 63, "movimentos": [("Bicada", 12), ("Jato de Água", 15)]},
    "Seaking": {"tipo": "Água", "hp": 80, "atk": 92, "def": 65, "vel": 68, "movimentos": [("Waterfall", 28), ("Surf", 30)]},
    "Staryu": {"tipo": "Água", "hp": 30, "atk": 45, "def": 55, "vel": 85, "movimentos": [("Jato de Água", 15), ("Investida", 10)]},
    "Starmie": {"tipo": "Água", "hp": 60, "atk": 75, "def": 85, "vel": 115, "movimentos": [("Surf", 30), ("Psiquismo", 30)]},
    "Mr. Mime": {"tipo": "Psíquico", "hp": 40, "atk": 45, "def": 65, "vel": 90, "movimentos": [("Psiquismo", 30), ("Tapa", 12)]},
    "Scyther": {"tipo": "Inseto", "hp": 70, "atk": 110, "def": 80, "vel": 105, "movimentos": [("Cortar", 20), ("Asa Cortante", 25)]},
    "Jynx": {"tipo": "Gelo", "hp": 65, "atk": 50, "def": 35, "vel": 95, "movimentos": [("Ice Beam", 30), ("Confusão", 15)]},
    "Electabuzz": {"tipo": "Elétrico", "hp": 65, "atk": 83, "def": 57, "vel": 105, "movimentos": [("Relâmpago", 25), ("Soco do Trovão", 28)]},
    "Magmar": {"tipo": "Fogo", "hp": 65, "atk": 95, "def": 57, "vel": 93, "movimentos": [("Lança-Chamas", 25), ("Soco de Fogo", 28)]},
    "Pinsir": {"tipo": "Inseto", "hp": 65, "atk": 125, "def": 100, "vel": 85, "movimentos": [("Cortar", 20), ("X-Scissor", 28)]},
    "Tauros": {"tipo": "Normal", "hp": 75, "atk": 100, "def": 95, "vel": 110, "movimentos": [("Body Slam", 25), ("Investida", 15)]},
    "Magikarp": {"tipo": "Água", "hp": 20, "atk": 10, "def": 55, "vel": 80, "movimentos": [("Splash", 1), ("Investida", 5)]},
    "Gyarados": {"tipo": "Água", "hp": 95, "atk": 125, "def": 79, "vel": 81, "movimentos": [("Hidrobomba", 35), ("Hyper Beam", 40)]},
    "Lapras": {"tipo": "Água", "hp": 130, "atk": 85, "def": 80, "vel": 60, "movimentos": [("Surf", 30), ("Ice Beam", 30)]},
    "Ditto": {"tipo": "Normal", "hp": 48, "atk": 48, "def": 48, "vel": 48, "movimentos": [("Transformação", 10), ("Investida", 10)]},
    "Eevee": {"tipo": "Normal", "hp": 55, "atk": 55, "def": 50, "vel": 55, "movimentos": [("Investida", 10), ("Arranhão", 10)]},
    "Vaporeon": {"tipo": "Água", "hp": 130, "atk": 65, "def": 60, "vel": 65, "movimentos": [("Surf", 30), ("Water Pulse", 22)]},
    "Jolteon": {"tipo": "Elétrico", "hp": 65, "atk": 65, "def": 60, "vel": 130, "movimentos": [("Relâmpago", 25), ("Choque do Trovão", 15)]},
    "Flareon": {"tipo": "Fogo", "hp": 65, "atk": 130, "def": 60, "vel": 65, "movimentos": [("Lança-Chamas", 25), ("Brasa", 15)]},
    "Porygon": {"tipo": "Normal", "hp": 65, "atk": 60, "def": 70, "vel": 40, "movimentos": [("Investida", 10), ("Psybeam", 20)]},
    "Omanyte": {"tipo": "Água", "hp": 35, "atk": 40, "def": 100, "vel": 35, "movimentos": [("Jato de Água", 15), ("Lançamento de Rocha", 20)]},
    "Omastar": {"tipo": "Água", "hp": 70, "atk": 60, "def": 125, "vel": 55, "movimentos": [("Hidrobomba", 35), ("Rock Slide", 25)]},
    "Kabuto": {"tipo": "Água", "hp": 30, "atk": 80, "def": 90, "vel": 55, "movimentos": [("Jato de Água", 15), ("Arranhão", 10)]},
    "Kabutops": {"tipo": "Água", "hp": 60, "atk": 115, "def": 105, "vel": 80, "movimentos": [("Surf", 30), ("Cortar", 20)]},
    "Aerodactyl": {"tipo": "Pedra", "hp": 80, "atk": 105, "def": 65, "vel": 130, "movimentos": [("Rock Slide", 25), ("Perfurar", 25)]},
    "Snorlax": {"tipo": "Normal", "hp": 160, "atk": 110, "def": 65, "vel": 30, "movimentos": [("Body Slam", 30), ("Hyper Beam", 40)]},
    "Articuno": {"tipo": "Gelo", "hp": 90, "atk": 85, "def": 100, "vel": 85, "movimentos": [("Ice Beam", 35), ("Blizzard", 40)]},
    "Zapdos": {"tipo": "Elétrico", "hp": 90, "atk": 90, "def": 85, "vel": 100, "movimentos": [("Relâmpago", 35), ("Thunder", 40)]},
    "Moltres": {"tipo": "Fogo", "hp": 90, "atk": 100, "def": 90, "vel": 90, "movimentos": [("Lança-Chamas", 35), ("Fire Blast", 40)]},
    "Dratini": {"tipo": "Dragão", "hp": 41, "atk": 64, "def": 45, "vel": 50, "movimentos": [("Investida", 10), ("Fúria do Dragão", 25)]},
    "Dragonair": {"tipo": "Dragão", "hp": 61, "atk": 84, "def": 65, "vel": 70, "movimentos": [("Fúria do Dragão", 28), ("Water Pulse", 22)]},
    "Dragonite": {"tipo": "Dragão", "hp": 91, "atk": 134, "def": 95, "vel": 80, "movimentos": [("Fúria do Dragão", 30), ("Hyper Beam", 40)]},
    "Mewtwo": {"tipo": "Psíquico", "hp": 106, "atk": 110, "def": 90, "vel": 130, "movimentos": [("Psiquismo", 35), ("Hyper Beam", 40)]},
    "Mew": {"tipo": "Psíquico", "hp": 100, "atk": 100, "def": 100, "vel": 100, "movimentos": [("Psiquismo", 30), ("Transformação", 20)]}
}

VANTAGENS = {
    "Fogo": {"Planta": 1.5, "Água": 0.5, "Gelo": 1.5, "Inseto": 1.5},
    "Água": {"Fogo": 1.5, "Planta": 0.5, "Terra": 1.5, "Pedra": 1.5},
    "Planta": {"Água": 1.5, "Fogo": 0.5, "Terra": 1.5, "Pedra": 1.5},
    "Elétrico": {"Água": 1.5, "Planta": 0.5, "Terra": 0.1},
    "Gelo": {"Planta": 1.5, "Terra": 1.5, "Fogo": 0.5, "Água": 0.5},
    "Pedra": {"Fogo": 1.5, "Gelo": 1.5, "Inseto": 1.5},
    "Terra": {"Fogo": 1.5, "Elétrico": 1.5, "Pedra": 1.5, "Planta": 0.5},
}

class PokemonBatalha:
    def __init__(self, nome, dados):
        self.nome = nome
        self.tipo = dados["tipo"]
        self.max_hp = dados["hp"] * 1.8 
        self.hp = self.max_hp
        self.atk = dados["atk"]
        self.defesa = dados["def"]
        self.vel = dados["vel"]
        self.movimentos = dados["movimentos"]

    def esta_vivo(self):
        return self.hp > 0

class JogoPokemonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Terminal & GUI Battle")
        self.root.geometry("650x550")
        self.root.config(bg="#f0f0f0")
        
        self.equipe_jogador_nomes = []
        self.time_jogador = []
        self.time_cpu = []
        self.idx_jogador = 0
        self.idx_cpu = 0
        self.cache_sprites = {}
        self.carregando_sprites = set()
        self._numero_por_nome = {nome: indice + 1 for indice, nome in enumerate(POKEDEX.keys())}
        
        self.criar_tela_selecao()

    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_selecao(self):
        self.limpar_janela()
        self.root.geometry("980x700")
        self.root.config(bg="#edf5ff")

        titulo = tk.Label(self.root, text="🔥 MONTE SUA EQUIPE DE 6 POKÉMON 🔥", font=("Arial", 20, "bold"), bg="#edf5ff", fg="#233a5c")
        titulo.pack(pady=(18, 10))

        self.lbl_status_equipe = tk.Label(self.root, text="Selecionados: 0/6", font=("Arial", 12, "bold"), bg="#edf5ff", fg="#1565C0")
        self.lbl_status_equipe.pack(pady=5)

        frame_busca = tk.Frame(self.root, bg="#edf5ff")
        frame_busca.pack(pady=(5, 10))

        tk.Label(frame_busca, text="Buscar Pokémon:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 5))
        self.txt_busca = tk.Entry(frame_busca, font=("Arial", 11), width=28)
        self.txt_busca.pack(side=tk.LEFT, padx=5)
        self.txt_busca.bind("<Return>", lambda event: self.buscar_pokemon())

        tk.Label(frame_busca, text="Tipo:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(side=tk.LEFT, padx=(10, 5))
        self.tipo_filtro = tk.StringVar(value="Todos")
        tipos = ["Todos"] + sorted({dados["tipo"] for dados in POKEDEX.values()})
        self.menu_tipo = tk.OptionMenu(frame_busca, self.tipo_filtro, *tipos, command=lambda *_: self.buscar_pokemon())
        self.menu_tipo.config(font=("Arial", 10, "bold"), width=12, bg="#E3F2FD")
        self.menu_tipo.pack(side=tk.LEFT, padx=5)

        btn_buscar = tk.Button(frame_busca, text="Pesquisar", command=self.buscar_pokemon, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=14, pady=6, width=12)
        self._configurar_hover(btn_buscar, "#4CAF50", "#3d8b40")
        btn_buscar.pack(side=tk.LEFT, padx=5)

        btn_limpar = tk.Button(frame_busca, text="Limpar", command=self.limpar_equipe, bg="#E0E0E0", font=("Arial", 10, "bold"), padx=12, pady=6, width=10)
        self._configurar_hover(btn_limpar, "#E0E0E0", "#CFCFCF")
        btn_limpar.pack(side=tk.LEFT, padx=5)

        self.lbl_detalhes = tk.Label(self.root, text="Selecione um Pokémon para ver o card e adicioná-lo ao time.", font=("Arial", 10), bg="#edf5ff", fg="#444", justify=tk.LEFT)
        self.lbl_detalhes.pack(pady=(0, 8))

        self.canvas = tk.Canvas(self.root, height=370, bg="#edf5ff", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0))

        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 20))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.cards_frame = tk.Frame(self.canvas, bg="#edf5ff")
        self.canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")
        self.cards_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)

        frame_botoes = tk.Frame(self.root, bg="#edf5ff")
        frame_botoes.pack(pady=(10, 5))

        btn_adicionar = tk.Button(frame_botoes, text="Adicionar Pokémon Selecionado", command=self.adicionar_pokemon, bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=28, height=2)
        self._configurar_hover(btn_adicionar, "#2196F3", "#1976D2")
        btn_adicionar.pack(side=tk.LEFT, padx=8)

        btn_remover = tk.Button(frame_botoes, text="Remover Último", command=self.remover_ultimo_pokemon, bg="#F44336", fg="white", font=("Arial", 11, "bold"), width=18, height=2)
        self._configurar_hover(btn_remover, "#F44336", "#D32F2F")
        btn_remover.pack(side=tk.LEFT, padx=8)

        btn_aleatorio = tk.Button(frame_botoes, text="Gerar Time Aleatório", command=self.gerar_time_aleatorio, bg="#FF9800", fg="white", font=("Arial", 11, "bold"), width=22, height=2)
        self._configurar_hover(btn_aleatorio, "#FF9800", "#F57C00")
        btn_aleatorio.pack(side=tk.LEFT, padx=8)

        caminho_ash = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ash.png")
        caminho_ash_fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ash_fixed.png")

        try:
            self.ash_image = tk.PhotoImage(file=caminho_ash)
        except tk.TclError:
            self.ash_image = None
            if os.path.exists(caminho_ash_fallback):
                self.ash_image = tk.PhotoImage(file=caminho_ash_fallback)

        frame_ash = tk.Frame(self.root, bg="#f5f5f5")
        frame_ash.pack(pady=(8, 2))

        if self.ash_image is not None:
            self.ash_image = self.ash_image.subsample(1, 1)
            self.lbl_ash = tk.Label(frame_ash, image=self.ash_image, bg="#f5f5f5")
            self.lbl_ash.pack(anchor=tk.CENTER)
            tk.Label(frame_ash, text="Treinador Ash", font=("Arial", 11, "bold"), bg="#f5f5f5", fg="#2E7D32").pack(anchor=tk.CENTER)
        else:
            self.lbl_ash = tk.Label(frame_ash, text="ASH", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#2E7D32")
            self.lbl_ash.pack(anchor=tk.CENTER)

        self.lbl_lista_escolhidos = tk.Label(self.root, text="Time: Nenhum", font=("Arial", 10, "italic"), bg="#edf5ff", fg="#555")
        self.lbl_lista_escolhidos.pack(pady=10)

        self.pokemon_selecionado = None
        self.atualizar_lista_opcoes(sorted(POKEDEX.keys()))

    def _configurar_hover(self, botao, cor_base, cor_hover):
        botao.bind("<Enter>", lambda event, b=botao, cor=cor_hover: b.config(bg=cor))
        botao.bind("<Leave>", lambda event, b=botao, cor=cor_base: b.config(bg=cor))

    def _on_mousewheel(self, event):
        if hasattr(event, "delta") and event.delta:
            self.canvas.yview_scroll(int(-event.delta / 120), "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        return "break"

    def _emoji_por_tipo(self, tipo):
        emojis = {
            "Fogo": "🔥",
            "Água": "💧",
            "Planta": "🌿",
            "Elétrico": "⚡",
            "Gelo": "❄️",
            "Pedra": "🪨",
            "Terra": "🌍",
            "Inseto": "🐛",
            "Veneno": "☠️",
            "Normal": "✨",
            "Lutador": "🥊",
            "Psíquico": "🧠",
            "Fada": "🧚",
            "Dragão": "🐉",
            "Voador": "🪽",
            "Fantasma": "👻",
            "Sombrio": "🌑",
            "Metal": "⚙️",
        }
        return emojis.get(tipo, "🎴")

    def _cor_por_tipo(self, tipo):
        cores = {
            "Fogo": "#ffb3a7",
            "Água": "#99d6ff",
            "Planta": "#9ae69a",
            "Elétrico": "#ffe082",
            "Gelo": "#bfeaff",
            "Pedra": "#d7c9a7",
            "Terra": "#d9b38c",
            "Inseto": "#cfe8a9",
            "Veneno": "#d7a7e8",
            "Normal": "#d9d9d9",
            "Lutador": "#f4a261",
            "Psíquico": "#f4a1ff",
            "Fada": "#f8c8dc",
            "Dragão": "#8fa7ff",
            "Voador": "#cfe3ff",
            "Fantasma": "#bca6d8",
            "Sombrio": "#5a5a5a",
            "Metal": "#d5d9dd",
        }
        return cores.get(tipo, "#eaeaea")

    def _obter_sprite_pokemon(self, nome):
        if nome in self.cache_sprites:
            return self.cache_sprites[nome]

        numero = self._numero_por_nome.get(nome)
        if numero is None:
            return None

        caminho_sprite = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sprites", f"{numero}.png")
        if not os.path.exists(caminho_sprite):
            self.cache_sprites[nome] = None
            return None

        try:
            imagem = tk.PhotoImage(file=caminho_sprite)
            self.cache_sprites[nome] = imagem
            return imagem
        except tk.TclError:
            self.cache_sprites[nome] = None
            return None

    def _carregar_sprite_assincrono(self, nome, label_ref=None):
        if nome in self.cache_sprites:
            imagem = self.cache_sprites[nome]
            if imagem is not None and label_ref is not None and label_ref.winfo_exists():
                label_ref.config(image=imagem, text="")
                label_ref.image = imagem
            return

        if nome in self.carregando_sprites:
            return

        self.carregando_sprites.add(nome)
        imagem = self._obter_sprite_pokemon(nome)
        self.carregando_sprites.discard(nome)

        if imagem is not None and label_ref is not None and label_ref.winfo_exists():
            label_ref.config(image=imagem, text="")
            label_ref.image = imagem
        elif label_ref is not None and label_ref.winfo_exists():
            label_ref.config(text=self._emoji_por_tipo(POKEDEX[nome]["tipo"]))

    def atualizar_lista_opcoes(self, lista):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        self.candidatos_atuais = lista
        colunas = 3
        for indice, nome in enumerate(lista):
            dados = POKEDEX[nome]
            tipo = dados["tipo"]
            cor = self._cor_por_tipo(tipo)
            card_wrapper = tk.Frame(self.cards_frame, bg="#dfe3ea", padx=8, pady=8)
            card_wrapper.grid(row=indice // colunas, column=indice % colunas, padx=12, pady=10, sticky="nsew")

            card = tk.Frame(card_wrapper, bg=cor, bd=2, relief=tk.RIDGE, padx=8, pady=8, highlightthickness=0)
            card.pack(fill=tk.BOTH, expand=True)

            frame_conteudo = tk.Frame(card, bg=cor, bd=0)
            frame_conteudo.pack(fill=tk.BOTH, expand=True)

            sprite_frame = tk.Frame(frame_conteudo, bg="#ffffff", bd=2, relief=tk.SOLID, padx=8, pady=8)
            sprite_frame.pack(pady=(0, 6), anchor=tk.CENTER)

            lbl_sprite = tk.Label(sprite_frame, text=self._emoji_por_tipo(tipo), font=("Arial", 22), bg="#ffffff", fg="#1a1a1a")
            lbl_sprite.pack(ipadx=18, ipady=12)
            self._carregar_sprite_assincrono(nome, lbl_sprite)

            btn = tk.Button(
                frame_conteudo,
                text=f"{self._emoji_por_tipo(tipo)} {nome}\n{tipo}\nHP {dados['hp']}  ATK {dados['atk']}\nDEF {dados['def']}  VEL {dados['vel']}",
                justify=tk.LEFT,
                bg=cor,
                fg="#1a1a1a",
                font=("Arial", 10, "bold"),
                relief=tk.FLAT,
                padx=12,
                pady=12,
                width=20,
                height=6,
                command=lambda nome_pokemon=nome: self.selecionar_pokemon_card(nome_pokemon)
            )
            btn.pack(fill=tk.BOTH, expand=True)

        self.cards_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def selecionar_pokemon_card(self, nome):
        self.pokemon_selecionado = nome
        dados = POKEDEX[nome]
        ataques = ", ".join(f"{ataque} ({poder})" for ataque, poder in dados["movimentos"][:3])
        self.lbl_detalhes.config(text=f"{nome} — {dados['tipo']} | HP {dados['hp']} | ATK {dados['atk']} | DEF {dados['def']} | VEL {dados['vel']} | Ataques: {ataques}")

    def mostrar_detalhes_pokemon(self, event=None):
        if not hasattr(self, 'candidatos_atuais'):
            return
        if self.pokemon_selecionado is None:
            self.lbl_detalhes.config(text="Selecione um Pokémon para ver detalhes.")
            return
        nome = self.pokemon_selecionado
        dados = POKEDEX[nome]
        ataques = ", ".join(f"{ataque} ({poder})" for ataque, poder in dados["movimentos"][:3])
        self.lbl_detalhes.config(text=f"{nome} — {dados['tipo']} | HP {dados['hp']} | ATK {dados['atk']} | DEF {dados['def']} | VEL {dados['vel']} | Ataques: {ataques}")

    def buscar_pokemon(self):
        termo = self.txt_busca.get().strip().lower()
        tipo = self.tipo_filtro.get()
        todos = sorted(POKEDEX.keys())

        filtrados = [n for n in todos if termo in n.lower()] if termo else todos
        if tipo != "Todos":
            filtrados = [n for n in filtrados if POKEDEX[n]["tipo"] == tipo]

        if not filtrados:
            for widget in self.cards_frame.winfo_children():
                widget.destroy()
            self.candidatos_atuais = []
            self.pokemon_selecionado = None
            self.lbl_detalhes.config(text="Nenhum Pokémon encontrado para esse filtro.")
            return

        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        self.atualizar_lista_opcoes(filtrados)

    def limpar_equipe(self):
        self.equipe_jogador_nomes = []
        self.lbl_status_equipe.config(text="Selecionados: 0/6")
        self.lbl_lista_escolhidos.config(text="Time: Nenhum")

    def remover_ultimo_pokemon(self):
        if not self.equipe_jogador_nomes:
            messagebox.showwarning("Aviso", "Seu time já está vazio!")
            return

        self.equipe_jogador_nomes.pop()
        self.lbl_status_equipe.config(text=f"Selecionados: {len(self.equipe_jogador_nomes)}/6")
        self.lbl_lista_escolhidos.config(text="Time: " + ", ".join(self.equipe_jogador_nomes) if self.equipe_jogador_nomes else "Time: Nenhum")

    def gerar_time_aleatorio(self):
        nomes = list(POKEDEX.keys())
        time_aleatorio = random.sample(nomes, 6)
        self.equipe_jogador_nomes = time_aleatorio
        self.lbl_status_equipe.config(text=f"Selecionados: {len(self.equipe_jogador_nomes)}/6")
        self.lbl_lista_escolhidos.config(text="Time: " + ", ".join(self.equipe_jogador_nomes))
        self.criar_tela_resumo_time()

    def criar_tela_resumo_time(self):
        self.limpar_janela()
        self.root.geometry("980x700")
        self.root.config(bg="#f5f5f5")

        tk.Label(self.root, text="📋 RESUMO DA EQUIPE", font=("Arial", 20, "bold"), bg="#edf5ff", fg="#233a5c").pack(pady=(20, 10))
        tk.Label(self.root, text=f"Time final: {len(self.equipe_jogador_nomes)}/6", font=("Arial", 12, "bold"), bg="#edf5ff", fg="#1565C0").pack()

        frame_cards = tk.Frame(self.root, bg="#edf5ff")
        frame_cards.pack(pady=15)

        for index, nome in enumerate(self.equipe_jogador_nomes):
            dados = POKEDEX[nome]
            cor = self._cor_por_tipo(dados["tipo"])
            card_wrapper = tk.Frame(frame_cards, bg="#dfe3ea", padx=8, pady=8)
            card_wrapper.grid(row=index // 3, column=index % 3, padx=12, pady=10, sticky="nsew")

            card = tk.Frame(card_wrapper, bg=cor, bd=2, relief=tk.RIDGE, padx=10, pady=10, highlightthickness=0)
            card.pack(fill=tk.BOTH, expand=True)

            sprite = self._obter_sprite_pokemon(nome)
            sprite_frame = tk.Frame(card, bg="#ffffff", bd=2, relief=tk.SOLID, padx=8, pady=8)
            sprite_frame.pack(anchor=tk.CENTER, pady=(0, 6))

            if sprite is not None:
                lbl_sprite = tk.Label(sprite_frame, image=sprite, bg="#ffffff")
                lbl_sprite.pack()
                lbl_sprite.image = sprite
            else:
                lbl_sprite = tk.Label(sprite_frame, text=self._emoji_por_tipo(dados['tipo']), font=("Arial", 22), bg="#ffffff", fg="#111")
                lbl_sprite.pack(ipadx=18, ipady=12)

            tk.Label(card, text=f"{self._emoji_por_tipo(dados['tipo'])} {nome}", font=("Arial", 11, "bold"), bg=cor, fg="#111").pack(anchor=tk.W)
            tk.Label(card, text=f"Tipo: {dados['tipo']}", font=("Arial", 9), bg=cor, fg="#111").pack(anchor=tk.W)
            tk.Label(card, text=f"HP: {dados['hp']}", font=("Arial", 9), bg=cor, fg="#111").pack(anchor=tk.W)
            tk.Label(card, text=f"ATK: {dados['atk']}", font=("Arial", 9), bg=cor, fg="#111").pack(anchor=tk.W)

        frame_acoes = tk.Frame(self.root, bg="#edf5ff")
        frame_acoes.pack(pady=10)

        btn_iniciar = tk.Button(frame_acoes, text="Iniciar Batalha", command=self.iniciar_batalha, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=18, height=2)
        self._configurar_hover(btn_iniciar, "#4CAF50", "#3d8b40")
        btn_iniciar.pack(side=tk.LEFT, padx=10)

        btn_voltar = tk.Button(frame_acoes, text="Voltar", command=self.criar_tela_selecao, bg="#E0E0E0", fg="#111", font=("Arial", 12, "bold"), width=12, height=2)
        self._configurar_hover(btn_voltar, "#E0E0E0", "#CFCFCF")
        btn_voltar.pack(side=tk.LEFT, padx=10)

    def adicionar_pokemon(self):
        if self.pokemon_selecionado is None:
            messagebox.showwarning("Aviso", "Selecione um Pokémon antes de adicionar ao time!")
            return

        if len(self.equipe_jogador_nomes) >= 6:
            messagebox.showwarning("Aviso", "Seu time já está completo! Você precisa remover algum Pokémon antes de adicionar outro.")
            return

        nome = self.pokemon_selecionado
        if nome in self.equipe_jogador_nomes:
            messagebox.showwarning("Aviso", "Você já escolheu este Pokémon!")
            return

        self.equipe_jogador_nomes.append(nome)
        self.lbl_status_equipe.config(text=f"Selecionados: {len(self.equipe_jogador_nomes)}/6")
        self.lbl_lista_escolhidos.config(text="Time: " + ", ".join(self.equipe_jogador_nomes))

        if len(self.equipe_jogador_nomes) == 6:
            self.criar_tela_resumo_time()

    def iniciar_batalha(self):
        todos_nomes = list(POKEDEX.keys())
        equipe_cpu_nomes = random.sample(todos_nomes, 6)
        
        self.time_jogador = [PokemonBatalha(nome, POKEDEX[nome]) for nome in self.equipe_jogador_nomes]
        self.time_cpu = [PokemonBatalha(nome, POKEDEX[nome]) for nome in equipe_cpu_nomes]
        
        self.idx_jogador = 0
        self.idx_cpu = 0
        
        self.criar_tela_batalha()

    def criar_tela_batalha(self):
        self.limpar_janela()
        self.root.geometry("1150x900")
        self.root.config(bg="#f4f4f4")
        self.batalha_em_andamento = False

        self.frame_topo = tk.Frame(self.root, bg="#ffe1dd", bd=2, relief=tk.RIDGE)
        self.frame_topo.pack(fill=tk.X, padx=10, pady=10)

        self.lbl_cpu_info = tk.Label(self.frame_topo, text="", font=("Arial", 11, "bold"), bg="#ffe1dd")
        self.lbl_cpu_info.pack(anchor=tk.W, padx=10, pady=5)

        self.lbl_cpu_hp = tk.Label(self.frame_topo, text="", font=("Arial", 10), bg="#ffe1dd")
        self.lbl_cpu_hp.pack(anchor=tk.W, padx=10, pady=5)

        self.lbl_resultado = tk.Label(self.frame_topo, text="⚔️ Batalha em andamento", font=("Arial", 11, "bold"), bg="#ffe1dd", fg="#2f2f2f")
        self.lbl_resultado.pack(anchor=tk.W, padx=10, pady=(0, 8))

        self.frame_luta = tk.Frame(self.root, bg="#123d38", bd=3, relief=tk.SUNKEN)
        self.frame_luta.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.lbl_arena = tk.Label(self.frame_luta, text="🏟️ ARENA DE BATALHA", font=("Arial", 16, "bold"), bg="#123d38", fg="#f7f7f7")
        self.lbl_arena.pack(pady=(8, 4))

        self.frame_batalha_visual = tk.Frame(self.frame_luta, bg="#123d38")
        self.frame_batalha_visual.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

        self.panel_cpu = tk.Frame(self.frame_batalha_visual, bg="#294d45", bd=2, relief=tk.RIDGE)
        self.panel_cpu.pack(fill=tk.X, padx=15, pady=(0, 10))

        self.lbl_cpu_sprite = tk.Label(self.panel_cpu, bg="#2d4d3f", bd=2, relief=tk.SOLID, padx=12, pady=12)
        self.lbl_cpu_sprite.pack(anchor=tk.W, padx=12, pady=(8, 2))

        self.lbl_cpu_nome = tk.Label(self.panel_cpu, text="", font=("Arial", 15, "bold"), bg="#2d4d3f", fg="#ffffff")
        self.lbl_cpu_nome.pack(anchor=tk.W, padx=12, pady=(0, 2))

        self.lbl_cpu_tipo = tk.Label(self.panel_cpu, text="", font=("Arial", 10), bg="#2d4d3f", fg="#dfefff")
        self.lbl_cpu_tipo.pack(anchor=tk.W, padx=12)

        self.canvas_cpu_hp = tk.Canvas(self.panel_cpu, width=500, height=28, bg="#2d4d3f", highlightthickness=0)
        self.canvas_cpu_hp.pack(fill=tk.X, padx=12, pady=(6, 12))

        self.panel_jogador = tk.Frame(self.frame_batalha_visual, bg="#294d45", bd=2, relief=tk.RIDGE)
        self.panel_jogador.pack(fill=tk.X, padx=15, pady=(0, 10))

        self.lbl_jogador_sprite = tk.Label(self.panel_jogador, bg="#2d4d3f", bd=2, relief=tk.SOLID, padx=12, pady=12)
        self.lbl_jogador_sprite.pack(anchor=tk.W, padx=12, pady=(8, 2))

        self.lbl_jogador_nome = tk.Label(self.panel_jogador, text="", font=("Arial", 15, "bold"), bg="#2d4d3f", fg="#ffffff")
        self.lbl_jogador_nome.pack(anchor=tk.W, padx=12, pady=(0, 2))

        self.lbl_jogador_tipo = tk.Label(self.panel_jogador, text="", font=("Arial", 10), bg="#2d4d3f", fg="#dfefff")
        self.lbl_jogador_tipo.pack(anchor=tk.W, padx=12)

        self.canvas_jogador_hp = tk.Canvas(self.panel_jogador, width=500, height=28, bg="#2d4d3f", highlightthickness=0)
        self.canvas_jogador_hp.pack(fill=tk.X, padx=12, pady=(6, 12))

        self.txt_log = tk.Text(self.frame_luta, height=9, width=100, font=("Courier", 10), state=tk.DISABLED, wrap=tk.WORD)
        self.txt_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.frame_baixo = tk.Frame(self.root, bg="#ccffcc", bd=2, relief=tk.RIDGE)
        self.frame_baixo.pack(fill=tk.X, padx=10, pady=10)

        self.lbl_jogador_info = tk.Label(self.frame_baixo, text="", font=("Arial", 11, "bold"), bg="#ccffcc")
        self.lbl_jogador_info.pack(anchor=tk.W, padx=10, pady=5)

        self.lbl_jogador_hp = tk.Label(self.frame_baixo, text="", font=("Arial", 10), bg="#ccffcc")
        self.lbl_jogador_hp.pack(anchor=tk.W, padx=10, pady=5)

        self.frame_botoes = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_botoes.pack(pady=5)

        self.btn_mov1 = tk.Button(self.frame_botoes, text="", font=("Arial", 11, "bold"), width=26, bg="#FF9800", fg="white", command=lambda: self.executar_turno(0))
        self._configurar_hover(self.btn_mov1, "#FF9800", "#F57C00")
        self.btn_mov1.pack(side=tk.LEFT, padx=10)

        self.btn_mov2 = tk.Button(self.frame_botoes, text="", font=("Arial", 11, "bold"), width=26, bg="#FF9800", fg="white", command=lambda: self.executar_turno(1))
        self._configurar_hover(self.btn_mov2, "#FF9800", "#F57C00")
        self.btn_mov2.pack(side=tk.LEFT, padx=10)

        self.atualizar_interface_batalha()
        self.log_msg("⚔️ Batalha iniciada! Escolha o seu próximo movimento.")

    def log_msg(self, texto):
        self.txt_log.config(state=tk.NORMAL)
        self.txt_log.insert(tk.END, texto + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state=tk.DISABLED)

    def habilitar_botoes_ataque(self, habilitar):
        estado = tk.NORMAL if habilitar else tk.DISABLED
        self.btn_mov1.config(state=estado)
        self.btn_mov2.config(state=estado)

    def _atualizar_barra_hp(self, canvas, hp_atual, hp_maximo, cor="#4CAF50"):
        canvas.delete("all")
        largura = 500
        altura = 26
        margem = 3
        proporcao = max(0, min(1, hp_atual / max(1, hp_maximo)))
        fundo = canvas.create_rectangle(margem, margem, largura - margem, altura - margem, fill="#1d2d2a", outline="#d0d0d0")
        valor = int((largura - 2 * margem) * proporcao)
        barra = canvas.create_rectangle(margem, margem, margem + valor, altura - margem, fill=cor, outline="")
        canvas.tag_raise(barra)
        texto = f"HP {int(hp_atual)} / {int(hp_maximo)}"
        canvas.create_text(largura / 2, altura / 2, text=texto, fill="#ffffff", font=("Arial", 9, "bold"))
        return fundo, barra

    def atualizar_interface_batalha(self):
        ativo_jogador = self.time_jogador[self.idx_jogador]
        ativo_cpu = self.time_cpu[self.idx_cpu]

        sprite_cpu = self._obter_sprite_pokemon(ativo_cpu.nome)
        if sprite_cpu is not None:
            self.lbl_cpu_sprite.config(image=sprite_cpu, text="", bg="#2d4d3f")
            self.lbl_cpu_sprite.image = sprite_cpu
        else:
            self.lbl_cpu_sprite.config(text=self._emoji_por_tipo(ativo_cpu.tipo), font=("Arial", 28), fg="white", bg="#2d4d3f")
            self.lbl_cpu_sprite.image = None

        sprite_jogador = self._obter_sprite_pokemon(ativo_jogador.nome)
        if sprite_jogador is not None:
            self.lbl_jogador_sprite.config(image=sprite_jogador, text="", bg="#2d4d3f")
            self.lbl_jogador_sprite.image = sprite_jogador
        else:
            self.lbl_jogador_sprite.config(text=self._emoji_por_tipo(ativo_jogador.tipo), font=("Arial", 28), fg="white", bg="#2d4d3f")
            self.lbl_jogador_sprite.image = None

        self.lbl_cpu_info.config(text=f"🤖 CPU | Inimigo: {ativo_cpu.nome} ({ativo_cpu.tipo}) | Restantes: {len(self.time_cpu) - self.idx_cpu}")
        self.lbl_cpu_hp.config(text=f"HP: {int(ativo_cpu.hp)} / {int(ativo_cpu.max_hp)}")
        self.lbl_cpu_nome.config(text=f"{self._emoji_por_tipo(ativo_cpu.tipo)} {ativo_cpu.nome}")
        self.lbl_cpu_tipo.config(text=f"Tipo: {ativo_cpu.tipo}")

        self.lbl_jogador_info.config(text=f"✨ VOCÊ | Combatente: {ativo_jogador.nome} ({ativo_jogador.tipo}) | Restantes: {len(self.time_jogador) - self.idx_jogador}")
        self.lbl_jogador_hp.config(text=f"HP: {int(ativo_jogador.hp)} / {int(ativo_jogador.max_hp)}")
        self.lbl_jogador_nome.config(text=f"{self._emoji_por_tipo(ativo_jogador.tipo)} {ativo_jogador.nome}")
        self.lbl_jogador_tipo.config(text=f"Tipo: {ativo_jogador.tipo}")

        self._atualizar_barra_hp(self.canvas_cpu_hp, ativo_cpu.hp, ativo_cpu.max_hp, "#E53935")
        self._atualizar_barra_hp(self.canvas_jogador_hp, ativo_jogador.hp, ativo_jogador.max_hp, "#43A047")

        movs = ativo_jogador.movimentos
        self.btn_mov1.config(text=f"{movs[0][0]} (Poder: {movs[0][1]})")
        self.btn_mov2.config(text=f"{movs[1][0]} (Poder: {movs[1][1]})")
        self.lbl_resultado.config(text="⚔️ Batalha em andamento")

    def executar_turno(self, escolha_mov_idx):
        if self.batalha_em_andamento:
            return

        self.batalha_em_andamento = True
        self.habilitar_botoes_ataque(False)
        self.root.after(500, self._resolver_ataque_jogador, escolha_mov_idx)

    def _resolver_ataque_jogador(self, escolha_mov_idx):
        ativo_jogador = self.time_jogador[self.idx_jogador]
        ativo_cpu = self.time_cpu[self.idx_cpu]
        mov_jogador = ativo_jogador.movimentos[escolha_mov_idx]
        mov_cpu = random.choice(ativo_cpu.movimentos)

        primeiro, segundo = (ativo_jogador, ativo_cpu) if ativo_jogador.vel >= ativo_cpu.vel else (ativo_cpu, ativo_jogador)
        mov_primeiro = mov_jogador if primeiro == ativo_jogador else mov_cpu
        mov_segundo = mov_cpu if primeiro == ativo_jogador else mov_jogador

        self.turno_atual = {"primeiro": primeiro, "segundo": segundo, "mov_primeiro": mov_primeiro, "mov_segundo": mov_segundo}

        dano1, mult1, nome1 = self.calcular_dano(primeiro, segundo, mov_primeiro)
        segundo.hp -= dano1
        self.log_msg(f"⚡ {primeiro.nome} usou {nome1}! Causou {dano1} de dano.")
        if mult1 > 1.0:
            self.log_msg("   🔥 Foi super efetivo!")

        self.atualizar_interface_batalha()

        if not segundo.esta_vivo():
            self.root.after(600, self._finalizar_turno)
            return

        self.root.after(600, self._resolver_ataque_cpu)

    def _resolver_ataque_cpu(self):
        primeiro = self.turno_atual["primeiro"]
        segundo = self.turno_atual["segundo"]
        mov_segundo = self.turno_atual["mov_segundo"]

        dano2, mult2, nome2 = self.calcular_dano(segundo, primeiro, mov_segundo)
        primeiro.hp -= dano2
        self.log_msg(f"⚡ {segundo.nome} usou {nome2}! Causou {dano2} de dano.")
        if mult2 > 1.0:
            self.log_msg("   🔥 Foi super efetivo!")

        self.atualizar_interface_batalha()
        self.root.after(600, self._finalizar_turno)

    def _finalizar_turno(self):
        self.log_msg("-" * 40)

        if not self.time_jogador[self.idx_jogador].esta_vivo():
            self.log_msg(f"💀 Seu {self.time_jogador[self.idx_jogador].nome} desmaiou!")
            self.lbl_resultado.config(text="💀 Pokémon derrotado")
            self._selecionar_proximo_pokemon_jogador()
            return

        if not self.time_cpu[self.idx_cpu].esta_vivo():
            self.log_msg(f"🏆 O {self.time_cpu[self.idx_cpu].nome} da CPU desmaiou!")
            self.idx_cpu += 1
            if self.idx_cpu < len(self.time_cpu):
                novo_cpu = self.time_cpu[self.idx_cpu]
                self.log_msg(f"🤖 A CPU enviou {novo_cpu.nome}!")
                self.lbl_resultado.config(text=f"🏆 {novo_cpu.nome} apareceu!")
                self.atualizar_interface_batalha()
            else:
                self.lbl_resultado.config(text="🏆 VITÓRIA!")
                messagebox.showinfo("Parabéns!", "🏆 VOCÊ VENCEU A LIGA POKÉMON DE KANTO! 🏆")
                self.criar_tela_selecao()
                return

        self.batalha_em_andamento = False
        self.habilitar_botoes_ataque(True)

    def _selecionar_proximo_pokemon_jogador(self):
        pokemons_disponiveis = [i for i, pokemon in enumerate(self.time_jogador) if pokemon.esta_vivo()]

        if not pokemons_disponiveis:
            self.lbl_resultado.config(text="💔 DERROTA")
            messagebox.showinfo("Fim de Jogo", "💔 Que pena! Você foi derrotado pela CPU...")
            self.criar_tela_selecao()
            return

        janela = tk.Toplevel(self.root)
        janela.title("Escolha o próximo Pokémon")
        janela.geometry("420x220")
        janela.transient(self.root)
        janela.grab_set()

        tk.Label(janela, text="Quem vai entrar no lugar do Pokémon derrotado?", font=("Arial", 12, "bold")).pack(pady=15)

        frame = tk.Frame(janela)
        frame.pack(pady=10)

        for indice in pokemons_disponiveis:
            nome = self.time_jogador[indice].nome
            tk.Button(
                frame,
                text=nome,
                width=18,
                font=("Arial", 10, "bold"),
                bg="#4CAF50",
                fg="white",
                command=lambda idx=indice, win=janela: self._trocar_pokemon_jogador(idx, win)
            ).pack(pady=5)

    def _trocar_pokemon_jogador(self, novo_idx, janela):
        self.idx_jogador = novo_idx
        janela.destroy()
        self.log_msg(f"✨ Vá! {self.time_jogador[self.idx_jogador].nome}!")
        self.atualizar_interface_batalha()
        self.batalha_em_andamento = False
        self.habilitar_botoes_ataque(True)

    def calcular_dano(self, atacante, defensor, movimento):
        nome_mov, poder = movimento
        mult_tipo = VANTAGENS.get(atacante.tipo, {}).get(defensor.tipo, 1.0)
        dano_base = (atacante.atk / max(1, defensor.defesa)) * poder * 0.7
        dano_final = int(dano_base * mult_tipo * random.uniform(0.85, 1.15))
        return max(1, dano_final), mult_tipo, nome_mov

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoPokemonGUI(root)
    root.mainloop()