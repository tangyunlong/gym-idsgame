import math
import gym
from gym_idsgame.envs.dao.game_state import GameState
from gym_idsgame.envs.dao.network_config import NetworkConfig

class GameConfig():
    """
    DTO with game configuration parameters
    """
    def __init__(self, network_config:NetworkConfig = None, manual:bool = True, num_layers:int = 1,
                 num_servers_per_layer:int = 2, num_attack_types:int = 10, max_value:int = 9,
                 initial_state:bool = None):
        self.manual = manual
        self.num_layers = num_layers
        self.num_servers_per_layer = num_servers_per_layer
        self.num_attack_types = num_attack_types
        self.max_value = max_value
        self.num_rows = self.num_layers + 2
        self.num_nodes = self.num_layers * self.num_servers_per_layer + 2  # +2 for Start and Data Nodes
        self.num_cols = self.num_servers_per_layer
        self.num_actions = self.num_attack_types * self.num_nodes
        self.num_states = math.pow(self.max_value+1, self.num_attack_types * 2 * self.num_nodes) \
                          * math.pow(10, self.max_value+1)
        self.network_config = network_config
        if network_config is None:
            self.network_config = NetworkConfig(self.num_rows, self.num_cols)
        self.initial_state = initial_state
        if self.initial_state is None:
            self.initial_state = GameState()
            self.initial_state.default_state(self.network_config.node_list, self.network_config.start_pos,
                                             self.num_attack_types)

    def get_attacker_action_space(self):
        action_space = gym.spaces.Discrete(self.num_actions)
        return action_space

    def get_attacker_observation_space(self, max_value, num_attack_types, num_nodes):
        return GameState.get_attacker_observation_space(self.max_value, self.num_attack_types, self.num_nodes)