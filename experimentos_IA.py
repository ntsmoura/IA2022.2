from time import sleep

from experimentos_gym import *

q_table = None

while True:
    try:
        env_name = input("Digite o nome do ambiente:")
        env = gym.make(env_name)
        env.close()
        break
    except gym.error.NameNotFound:
        print("Ambiente não encontrado! Tente novamente em instantes...")
        sleep(1)

while True:
    try:
        action = int(input("Escolha a ação:\n1-Treinar\n2-Executar\n3-Métricas\n4-Sair\n"))
    except ValueError:
        print("Ação não válida! Tente novamente!")
        continue
    match action:
        case 1:
            episodes = int(input("Digite a quantidade de episódios:"))
            alpha = float(input("Digite o hiperparâmetro alpha:"))
            gamma = float(input("Digite o hiperparâmetro gamma:"))
            epsilon = float(input("Digite o hiperparâmetro epsilon:"))
            q_table = train_q_learn_gym(env_name, episodes, alpha, gamma, epsilon)
        case 2:
            run_q_learn_gym(env_name, 10)
        case 3:
            episodes = int(input("Digite a quantidade de episódios:"))
            run_q_learn_gym(env_name, episodes, False)
        case 4:
            print("Até mais!")
            break
        case _:
            print("Ação inválida! Tente novamente.")
