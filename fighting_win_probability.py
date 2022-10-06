# -*- coding: utf-8 -*-



from itertools import product
from collections import defaultdict
from pprint import pprint
import numpy as np
import pandas as pd
from numpy.linalg import matrix_power

player_health = 2
player_attack = 2
monster_health = 5
monster_attack = 1
dice_roll_needed = 4



player_hit_probability = (7-dice_roll_needed)/6

def create_transition_matrix(player_health, player_attack, monster_health, monster_attack, player_hit_probability):
    t_mat = defaultdict(lambda: defaultdict(lambda: 0))
    queue = [(player_health, monster_health)]
    while queue:
        curr_state = queue.pop(0)
        player_gets_hit, player_hits = (), ()
        if 0 not in curr_state:
            player_gets_hit = (max(0, curr_state[0] - monster_attack), curr_state[1])
            player_hits = (curr_state[0], max(0, curr_state[1] - player_attack))
        if player_gets_hit:
            queue.append(player_gets_hit)
        if player_hits:
            queue.append(player_hits)
        t_mat[curr_state][player_gets_hit] = 1 - player_hit_probability
        t_mat[curr_state][player_hits] = player_hit_probability
    return accumulate_win_loss(t_mat)


def stringify(t):
    return f"P{t[0]}M{t[1]}"

def accumulate_win_loss(t_mat):
    states = list(t_mat.keys())
    t_mat_final = {stringify(state): dict() for state in states}
    transitions = list(product(states, states))
    for curr, nxt in transitions:
        if (curr[0] == nxt[0] == 0) and (curr[1] == nxt[1]):
            t_mat_final[stringify(curr)][stringify(nxt)] = 1
        elif (curr[1] == nxt[1] == 0) and (curr[0] == nxt[0]):
            t_mat_final[stringify(curr)][stringify(nxt)] = 1            
        else:
            t_mat_final[stringify(curr)][stringify(nxt)] = t_mat[curr][nxt]
    return t_mat_final

df = pd.DataFrame(create_transition_matrix(player_health, player_attack, monster_health, monster_attack, player_hit_probability)).transpose()
ss = pd.DataFrame(matrix_power(df, 100), index=df.index, columns=df.columns)
first_row = (ss.loc[f"P{player_health}M{monster_health}"])
print("Win %: ", round(first_row.filter(regex=("..M0")).sum() * 100, 2))
print("Loss %: ", round(first_row.filter(regex=("P0..")).sum() * 100, 2))





