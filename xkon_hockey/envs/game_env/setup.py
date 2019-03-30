from setuptools import setup

setup(name='air_hockey',
      version='0.0.1',
      description='OpenAI Gym Environment Wrapper for Air Hockey Game Simulator',
      install_requires=['gym',
                        'pygame',
                        'numpy',
                        'opencv-python']
)