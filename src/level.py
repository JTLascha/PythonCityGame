import os
import pygame

from . import board

def get_level_list(directory):
    """Returns a list of .lvl files in directory"""
    level_names = []

    for level_config in os.listdir(directory):
        name, ext = os.path.splitext(level_config)
        
        if ext.lower() == ".lvl":
            level_names.append(name.lower())
        
    return level_names

def get_level_board(directory, level_name):
    """Returns a board with square positions from level file"""
    with open(directory + level_name, "r") as f:
        num_buildings = int(f.readline())
        building_list = []

        for b in range(num_buildings):
            building_list.append(tuple(map(int, f.readline().split(" "))))

    return board.Board(building_list)


