import tensorflow as tf
import gym
import numpy as np

# Ambiente CartPole do Gym
env = gym.make('CartPole-v1')

# Modelo simples de Aprendizado por Reforço
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Treinamento por reforço
max_episodes = 1000  # define o numero máximo de episodios
gamma = 0.95  # fator de desconto
rewards_history = []


for episode in range(max_episodes):
    state = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        next_state, reward, done, terminated, truncated,  _ = env.step(action)
        done = terminated or truncated

        # Q-learning atualiza a estimativa de Q
        q_target = reward + gamma * np.amax(model.predict(next_state.reshape(1, -1), verbose=0))
        q_values = model.predict(state.reshape(1, -1), verbose=0)
        q_values[0][action] = q_target

        model.fit(state.reshape(1, -1), q_values, epochs=1, verbose=0)

        state = next_state

        # guarda o total de recompensas
        # rewards_history.append(total_reward)

        # A cada 10 episódios, exibe a média
        if episode % 10 == 0:
            average_reward = np.mean(rewards_history[10:])

            print(f'Episode {episode}, Average Reward (últimos 10): {average_reward}')

            # adicionando condicao de parada
            if average_reward >= 195:  # pode ajustar esse valor conforme necessario
                print(f'Evironment solved in episode {episode}')

            break