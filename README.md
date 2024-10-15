Optimal Strategy Development for Competitive Game Theory 
Overview

This repository contains solutions for MTL106 Assignment 1: Mind Games, which is part of the Probability and Stochastic Processes course. The assignment involves calculating probabilities, expectations, variances, and performing Monte Carlo simulations for a game played between Alice and Bob using varying strategies.

Problem Breakdown

1. Calculating Probabilities for Alice and Bob
In this part, we calculate the probability that Alice wins a specified number of rounds, and Bob wins another set of rounds after T rounds, where T is derived from the last two digits of the student's entry number.

1a. Probability Calculation

The script for this problem computes the probability based on Alice's and Bob's strategies using dynamic programming.

Script: q1a.py

Functions:
calc_prob(alice_wins, bob_wins) — Calculates the probability that Alice wins after a certain number of rounds.


1b. Expectation and Variance Calculation

For this part, we calculate both the expectation and variance of Alice's wins over a specified number of rounds.

Script: q1b.py
Functions:
calc_expectation(t) — Computes the expectation value of Alice's wins.
calc_variance(t) — Computes the variance in Alice's wins.



2. Monte Carlo Simulations for Optimal Strategies


2a. Simulating Optimal Strategy for Alice Against Bob

We simulate a game where Alice and Bob play multiple rounds with specific strategies, and Alice adjusts her strategy based on the previous results.

Script: q2a.py
Functions:
monte_carlo(num_rounds) — Simulates a game between Alice and Bob for a given number of rounds using Monte Carlo simulation.

2b. Non-Greedy Strategy

In this part, we test if Alice’s non-greedy strategy could outperform the greedy strategy in certain cases and run Monte Carlo simulations to validate the results.

Script: q2b.py
Functions:
monte_carlo(num_rounds) — Simulates a game to check the performance of non-greedy strategy.

2c. Estimating the Number of Rounds for Alice to Win T Matches

This part estimates the expected number of rounds Alice will need to win T matches, using a Monte Carlo simulation.

Script: q2c.py
Functions:
estimate_tau(T) — Uses Monte Carlo simulations to estimate how many rounds Alice will need to win T matches.

3. Advanced Strategies and Simulations

3a. Optimal Strategy for Alice When Bob Plays Randomly

This problem involves running a simulation where Bob plays randomly, and Alice tries to adjust her strategy to maximize the expected points.

Script: q3a.py
Functions:
monte_carlo(num_rounds) — Runs a simulation to determine Alice's optimal strategy against Bob's random play.

3b. Maximizing Expected Points Over Multiple Rounds

Here, we calculate the expected number of points Alice will have after T rounds and determine her optimal strategy.

Script: q3b.py
Functions:
optimal_strategy(na, nb, tot_rounds) — Determines Alice’s optimal strategy over T rounds.
expected_points(tot_rounds) — Calculates the expected number of points Alice will have at the end of T rounds.
