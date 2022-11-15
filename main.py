import os
import time

from pick import pick
from experimentos_gym import *

q_table = None

CLEAR_TERMINAL = 'cls' if os.name == 'nt' else 'clear'

os.system(CLEAR_TERMINAL)

title = 'Escolha um ambiente: '
options = ['Taxi-v3', 'CliffWalking-v0', 'FrozenLake-v1', ]

env_name, index = pick(options, title, indicator='=>', default_index=0)

while True:
    try:
        try:
            title = 'Escolha uma ação: '
            options = ['Treinar', 'Executar', 'Métricas', 'Sair']
            _, action = pick(options, title, indicator='=>', default_index=0)
            os.system(CLEAR_TERMINAL)
        except ValueError:
            print("Ação não válida! Tente novamente!")
            continue
        match action:
            case 0:
                episodes = int(input("Digite a quantidade de episódios:"))
                alpha = float(input("Digite o hiperparâmetro alpha:"))
                gamma = float(input("Digite o hiperparâmetro gamma:"))
                epsilon = float(input("Digite o hiperparâmetro epsilon:"))
                q_table = train_q_learn_gym(env_name, episodes, alpha, gamma, epsilon)
            case 1:
                run_q_learn_gym(env_name, 5)
            case 2:
                episodes = int(input("Digite a quantidade de episódios:"))
                os.system(CLEAR_TERMINAL)
                run_q_learn_gym(env_name, episodes, False)

            case 3:
                print("Até mais!")
                break
            case _:
                print("Ação inválida! Tente novamente.")
        input("Enter para continuar...")
    except KeyboardInterrupt:
        print("Até mais!")
        exit()
