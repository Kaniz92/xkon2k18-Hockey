import xkon_hockey
import gym
import pygame

if __name__ == "__main__":
    env = gym.make('AirHockey-v0')
    while True:
        if any([event.type == pygame.QUIT for event in pygame.event.get()]): break
        env.step()
    pygame.quit ()

#if __name__ == "__main__":
      #  processor = gym_air_hockey.DataProcessor()