"""
Runner for the IDS Game GUI Manual Game
"""
from gym_idsgame.envs.rendering.viewer import Viewer
from gym_idsgame.envs.dao.game_config import GameConfig
from gym_idsgame.envs.dao.idsgame_config import IdsGameConfig
from gym_idsgame.envs.dao.render_config import RenderConfig
from gym_idsgame.envs.policy_baselines.random_defense import RandomDefense

if __name__ == '__main__':
    game_config = GameConfig(num_layers = 2, num_servers_per_layer = 3, num_attack_types = 10, max_value = 10)
    defender_policy = RandomDefense(game_config)
    render_config = RenderConfig()
    render_config.manual_default()
    idsgame_config = IdsGameConfig(game_config=game_config, defender_policy=defender_policy,
                                   render_config=render_config)
    viewer = Viewer(idsgame_config)
    viewer.manual_start()