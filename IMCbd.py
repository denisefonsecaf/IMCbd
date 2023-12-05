#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Crie um programa que calcule o IMC e armazene o resultado no Banco de Dados

import sqlite3

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect('imc_database.db')

# Criar a tabela se não existir
conn.execute('''
    CREATE TABLE IF NOT EXISTS imc_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        altura REAL,
        peso REAL,
        imc REAL
    )
''')

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para inserir dados no banco de dados
def inserir_dados(nome, altura, peso):
    imc = calcular_imc(peso, altura)

    # Inserir dados na tabela
    conn.execute('''
        INSERT INTO imc_data (nome, altura, peso, imc)
        VALUES (?, ?, ?, ?)
    ''', (nome, altura, peso, imc))

    # Commit para salvar as alterações
    conn.commit()

# Função para visualizar os dados no banco de dados
def visualizar_dados():
    cursor = conn.execute('SELECT * FROM imc_data')
    for row in cursor:
        print(f"ID: {row[0]}, Nome: {row[1]}, Altura: {row[2]}, Peso: {row[3]}, IMC: {row[4]}")

# Exemplo de uso
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

inserir_dados(nome, altura, peso)
print("Dados inseridos com sucesso!\n")

print("Dados no banco de dados:")
visualizar_dados()

# Fechar a conexão com o banco de dados
conn.close()