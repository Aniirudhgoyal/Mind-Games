def fractional_payoff_matrix(alice_points, bob_points):
    return [[(bob_points/(alice_points+bob_points), 0, alice_points/(alice_points+bob_points)), (7/10, 0, 3/10), (5/11, 0, 6/11)],
            [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)],
            [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]]


def probability(alice_points, bob_points, alice_mode, event):
    # returns probability of event=event happening to alice given that she has alice_points and bob has bob_points, and she chooses to use alice_mode
    if event == 1:
        return (fractional_payoff_matrix(alice_points, bob_points)[alice_mode][0][0] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][1][0] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][2][0]) / 3
    elif event == 0.5:
        return (fractional_payoff_matrix(alice_points, bob_points)[alice_mode][0][1] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][1][1] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][2][1]) / 3
    else:
        return (fractional_payoff_matrix(alice_points, bob_points)[alice_mode][0][2] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][1][2] + fractional_payoff_matrix(alice_points, bob_points)[alice_mode][2][2]) / 3


class CalculateExpectation:
    def __init__(self, num_rounds):
        self.dp = [[(-1, -1)] * (2*num_rounds+1) for _ in range(2*num_rounds+1)]
        # dp[i][j] = expected value of points that alice will gain from this point on given that she has i/2 points and bob has j/2 points to reach a total of num_rounds rounds
        self.num_rounds = num_rounds
        for i in range(2*num_rounds+1):
            self.dp[i][2*num_rounds-i] = (0, -1)

    def calc_dp(self, alice_points_scaled, bob_points_scaled):
        if alice_points_scaled > 2*self.num_rounds or bob_points_scaled > 2*self.num_rounds or alice_points_scaled <= 0 or bob_points_scaled <= 0 or alice_points_scaled + bob_points_scaled > 2*self.num_rounds:
            return 0
        if self.dp[alice_points_scaled][bob_points_scaled][0] != -1:
            return self.dp[alice_points_scaled][bob_points_scaled][0]
        x = []
        for i in range(3):
            x.append(
                (self.calc_dp(alice_points_scaled+2, bob_points_scaled) + 1) * probability(alice_points_scaled, bob_points_scaled, i, 1) +
                (self.calc_dp(alice_points_scaled+1, bob_points_scaled+1) + 0.5) * probability(alice_points_scaled, bob_points_scaled, i, 0.5) +
                (self.calc_dp(alice_points_scaled, bob_points_scaled+2) + 0) * probability(alice_points_scaled, bob_points_scaled, i, 0))
        max_index = x.index(max(x))
        self.dp[alice_points_scaled][bob_points_scaled] = (x[max_index], max_index)
        return self.dp[alice_points_scaled][bob_points_scaled][0]

    def calc_expectation(self):
        return 1 + self.calc_dp(2, 2)


def optimal_strategy(na, nb, tot_rounds):
    expectation_object = CalculateExpectation(tot_rounds)
    expectation_object.calc_dp(int(na*2), int(nb*2))
    tup = expectation_object.dp[int(na*2)][int(nb*2)]
    if tup[1] == 0:
        return [1, 0, 0]
    elif tup[1] == 1:
        return [0, 1, 0]
    else:
        return [0, 0, 1]


def expected_points(tot_rounds):
    expectation_object = CalculateExpectation(tot_rounds)
    return expectation_object.calc_expectation()