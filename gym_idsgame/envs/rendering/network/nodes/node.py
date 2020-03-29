"""
Abstract node in the network of the gym-idsgame environment
"""
from abc import ABC, abstractmethod
from typing import Union

class Node(ABC):
    """
    Abstract node in the grid network
    """

    @property
    @abstractmethod
    def node_type(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    @property
    def pos(self):
        return (self.row, self.col)

    @abstractmethod
    def manual_blink_defense(self, i):
        pass

    @abstractmethod
    def manual_blink_attack(self, i, attacker_pos: Union[int, int], edges=None):
        pass

    @abstractmethod
    def set_state(self, attack_values, defense_values, det_value):
        pass

    @abstractmethod
    def unschedule(self):
        pass

    @abstractmethod
    def visualize_defense(self, defense_type):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_in_edges(self, edges):
        pass

    @abstractmethod
    def add_out_edges(self, edges):
        pass

    @abstractmethod
    def get_link_coords(self, upper=True, lower=False):
        pass