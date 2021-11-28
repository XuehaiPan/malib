import gym
import numpy as np

from malib.utils.typing import Dict, AgentID
from malib.utils.episode import Episode

from .env import GymEnv


def env_desc_gen(env_id: str, scenario_configs: Dict = None):
    env = GymEnv(env_id=env_id, scenario_config=scenario_configs)
    env_desc = {
        "creator": GymEnv,
        "possible_agents": env.possible_agents,
        "action_spaces": env.action_spaces,
        "observation_spaces": env.observation_spaces,
        "config": {
            "env_id": env_id,
            "scenario_configs": scenario_configs or {},
        },
    }
    env.close()
    return env_desc
