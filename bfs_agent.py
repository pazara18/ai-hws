# Abdulkadir Pazar 150180028

import time
import random
from copy import deepcopy
from agent import Agent

#  use whichever data structure you like, or create a custom one
import queue
import heapq
from collections import deque

"""
  you may use the following Node class
  modify it if needed, or create your own
"""


class Node:
    def __init__(self, parent_node, level_matrix, player_row, player_column, depth, chosen_dir):
        self.parent_node = parent_node
        self.level_matrix = level_matrix
        self.player_row = player_row
        self.player_col = player_column
        self.depth = depth
        self.chosen_dir = chosen_dir


class BFSAgent(Agent):

    def __init__(self):
        super().__init__()

    def solve(self, level_matrix, goal, player_row, player_column):
        super().solve(level_matrix, goal, player_row, player_column)
        move_sequence = []

        """
            YOUR CODE STARTS HERE
            fill move_sequence list with directions chars
        """
        row_count, col_count = len(level_matrix), len(level_matrix[0])
        position = (player_row, player_column)
        q = deque()
        q.appendleft(Node(None, level_matrix, position[0], position[1], 0, None))
        self.generated_node_count = 1
        self.maximum_node_in_memory_count = len(q)
        visited = [[False] * col_count for i in range(row_count)]
        while True:
            if self.maximum_node_in_memory_count < len(q):
                self.maximum_node_in_memory_count = len(q)
            node = q.pop()
            self.expanded_node_count += 1
            visited[node.player_row][node.player_col] = True
            if node.player_row == goal[0] and node.player_col == goal[1]:
                while node.parent_node is not None:
                    move_sequence.insert(0, node.chosen_dir)
                    node = node.parent_node
                break

            directions = [('U', (node.player_row - 1, node.player_col)), ('D', (node.player_row + 1, node.player_col)),
                          ('L', (node.player_row, node.player_col - 1)), ('R', (node.player_row, node.player_col + 1))]
            for i in range(len(directions)):
                row, col = directions[i][1]
                if level_matrix[row][col] != "W" and not visited[row][col]:
                    q.appendleft(Node(node, level_matrix, row, col, node.depth + 1, directions[i][0]))
                    self.generated_node_count += 1
        """
            YOUR CODE ENDS HERE
            return move_sequence
        """
        return move_sequence
