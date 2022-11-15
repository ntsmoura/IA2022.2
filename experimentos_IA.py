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
        action = int(input("Escolha a ação:\n1-Treinar\n2-Executar\n3-Finalizar\n"))
    except ValueError:
        print("Ação não reconhecida! Tente novamente!")
        continue
    match action:
        case 1:
            episodes = int(input("Digite a quantidade de episódios:"))
            alpha = float(input("Digite o hiperparâmetro alpha:"))
            gamma = float(input("Digite o hiperparâmetro gamma:"))
            epsilon = float(input("Digite o hiperparâmetro epsilon:"))
            q_table = train_q_learn_gym(env_name, episodes, alpha, gamma, epsilon)
        case 2:
            if q_table is None:
                print(f"Nenhum modelo treinado para {env_name}. Treine algum modelo antes!")
            else:
                episodes = int(input("Digite a quantidade de episódios:"))
                animation = int(input("Deseja animação?\n1-Sim\n2-Não\n"))
                if animation == 1:
                    run_q_learn_gym(env_name, q_table, episodes, True)
                else:
                    run_q_learn_gym(env_name, q_table, episodes, False)
        case 3:
            print("Até mais!")
            break
        case _:
            print("Ação não reconhecida! Tente novamente!")
