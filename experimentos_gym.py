import random
import time

import gym
import numpy as np


def train_q_learn_gym(env_name, episodes, alpha, gamma, epsilon):
    print("Porcentagem concluída: 0%")
    percent = 0.1

    env = gym.make(env_name)

    q_table = np.zeros([env.observation_space.n, env.action_space.n])

    for i in range(1, episodes):
        state = env.reset()[0]

        epochs, penalties, reward, = 0, 0, 0
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()  # Exploration: executa uma ação aleatória
            else:
                action = np.argmax(q_table[state])  # Exploitation: uso dos q-values já calculados

            next_state, reward, done, truncated, info = env.step(action)

            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])

            # média móvel exponencial para atualização dos q-values na q_table
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -10:
                penalties += 1

            state = next_state
            epochs += 1

        if i >= float(episodes) * percent:
            print(f"Porcentagem concluída: {round(percent*100,1)}%")
            percent += 0.1

    env.close()
    print("Porcentagem concluída 100%.\nFim do treinamento.\n")
    np.save(f"{env_name}-best.npy", q_table)
    print("Modelo salvo!")


def run_q_learn_gym(env_name, episodes, animation=True):
    q_table = None
    try:
        q_table = np.load(f"{env_name}-best.npy")
    except FileNotFoundError:
        print(f"Nenhum modelo treinado para {env_name}. Treine algum modelo antes!")
        exit()
    if animation:
        env = gym.make(env_name, render_mode="human")
    else:
        env = gym.make(env_name)

    total_epochs, total_penalties, total_reward = 0, 0, 0

    for i in range(episodes):
        state = env.reset()[0]
        epochs, penalties, reward = 0, 0, 0

        done = False

        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, truncated, info = env.step(action)
            if reward == -10:
                penalties += 1

            epochs += 1

        total_penalties += penalties
        total_epochs += epochs
        total_reward += reward

    print(f"Resultado(s) depois de {episodes} episódio(s):")
    print(f"Tempo médio por episódio: {total_epochs / episodes}")
    print(f"Penalidade média por episódio: {total_penalties / episodes}")
    print(f"Recompensa média por episódio: {total_reward / episodes}\n")
    env.close()
