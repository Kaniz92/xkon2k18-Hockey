from gym.envs.registration import register

register(
    id='AirHockey-v0',
    entry_point='xkon_hockey.envs:AirHockeyEnv'
)

from xkon_hockey.processor import DataProcessor