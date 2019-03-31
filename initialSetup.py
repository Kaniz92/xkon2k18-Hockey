import xkon_hockey
import xkon_hockey.envs
import gym
import pygame

if __name__ == "__main__":
    env = gym.make('AirHockey-v0')
    env.reset()
    for _ in range(500):
        if any([event.type == pygame.QUIT for event in pygame.event.get()]): break
        env.step(debug=True)
    pygame.quit ()

#if __name__ == "__main__":
      #  processor = gym_air_hockey.DataProcessor()