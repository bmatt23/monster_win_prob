# monster_win_prob
This file is meant to use steady state Markov Chains to calculate the probability of defeating a monster in the game "Four Souls".

In this game, the player has a level of health and attack, as does the monster. Each monster also has a "dice roll" statistic.
If the player rolls greater than or equal to the dice roll, the player delivers their amount of attack onto the monster's health.
If the player rolls less than the dice roll, the monster delivers their amount of attack onto the player's health.
Rolls occur until either the player or the monster dies. 

This code can take in an input of player_health, monster_health, player_attack, monster_attack, and dice_roll_needed. The code will output the player's chances of winning against said monster.
