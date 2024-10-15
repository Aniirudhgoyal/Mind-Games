import numpy as np
import random


class PlayerBase:
    def __init__(self, name):
        self.past_play_styles = [1, 1]
        if name == "Alice":
            self.results = [1, 0]
        else:
            self.results = [0, 1]
        self.opp_play_styles = [1, 1]
        self.points = 1
        self.opp_points = 1

    def observe_result(self, own_style, opp_style, result):
        self.points += result
        self.opp_points += (1 - result)
        self.past_play_styles.append(own_style)
        self.opp_play_styles.append(opp_style)
        self.results.append(result)


class Alice(PlayerBase):
    def __init__(self):
        super().__init__("Alice")

    def play_move(self):
        if self.opp_points / (self.points + self.opp_points) + 127 / 110 >= 329 / 220:
            return 0
        else:
            return 2


class Bob(PlayerBase):
    def __init__(self):
        super().__init__("Bob")

    def play_move(self):
        return np.random.choice([0, 1, 2])


def update_payoff_matrix(payoff_matrix, alice_points, bob_points):
    payoff_matrix[0][0] = (bob_points * 2, 0, alice_points * 2)
    return payoff_matrix


def determine_win_loss(alice_move, bob_move, payoff_matrix):
    prob_ele = payoff_matrix[alice_move][bob_move]
    num = random.randint(1, int(sum(prob_ele)))
    if num <= prob_ele[0]:
        return 1
    elif num <= prob_ele[0] + prob_ele[1]:
        return 0.5
    else:
        return 0


def simulate_round(alice, bob, payoff_matrix):
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    result = determine_win_loss(alice_move, bob_move, payoff_matrix)
    alice.observe_result(alice_move, bob_move, result)
    bob.observe_result(bob_move, alice_move, 1 - result)
    return payoff_matrix


def monte_carlo(num_rounds):
    payoff_matrix = [[(2, 0, 2), (7, 0, 3), (5, 0, 6)],
                     [(3, 0, 7), (1, 1, 1), (3, 5, 2)],
                     [(6, 0, 5), (2, 5, 3), (1, 8, 1)]]
    alice = Alice()
    bob = Bob()
    for _ in range(num_rounds):
        payoff_matrix = update_payoff_matrix(simulate_round(alice, bob, payoff_matrix), alice.points, bob.points)
    print(alice.points, bob.points)


if __name__ == "__main__":
    monte_carlo(num_rounds=10 ** 5)
