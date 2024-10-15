M = 10**9 + 7


class Num(int):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def __int__(self):
        return self.num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Num((((self.num % M + M) % M) + ((int(other) % M + M) % M)) % M)

    def __radd__(self, other):
        return Num((((self.num % M + M) % M) + ((int(other) % M + M) % M)) % M)

    def __mul__(self, other):
        return Num((((self.num % M + M) % M) * ((int(other) % M + M) % M)) % M)

    def __rmul__(self, other):
        return Num((((self.num % M + M) % M) * ((int(other) % M + M) % M)) % M)

    def __truediv__(self, other):
        return Num((((self.num % M + M) % M) * pow((int(other) % M + M) % M, M-2, M)) % M)

    def __rtruediv__(self, other):
        return Num((((self.num % M + M) % M) * pow((int(other) % M + M) % M, M-2, M)) % M)

    def __sub__(self, other):
        return Num((((self.num % M + M) % M) - ((int(other) % M + M) % M)) % M)

    def __rsub__(self, other):
        return Num((((int(other) % M + M) % M) - ((self.num % M + M) % M)) % M)

    def __eq__(self, other):
        return self.num == Num(int(other)).num

    def __ne__(self, other):
        return self.num != Num(int(other)).num

    def __pow__(self, power, modulo=None):
        return Num(pow(self.num, int(power), M))


def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M


def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M


def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))


class CalculateProbability:
    def __init__(self, alice_wins, bob_wins):
        self.max_alice_wins = alice_wins
        self.max_bob_wins = bob_wins
        self.dp = [[Num(-1)] * (bob_wins + 1) for _ in range(alice_wins + 1)]
        self.dp[alice_wins][bob_wins] = Num(1)

    def calc_dp(self, alice_wins, bob_wins):
        if alice_wins > self.max_alice_wins or bob_wins > self.max_bob_wins:
            return 0
        if self.dp[alice_wins][bob_wins] != Num(-1):
            return self.dp[alice_wins][bob_wins]
        self.dp[alice_wins][bob_wins] = self.calc_dp(alice_wins, bob_wins + 1) * (Num(alice_wins) / Num(alice_wins + bob_wins)) + self.calc_dp(alice_wins + 1, bob_wins) * (Num(bob_wins) / Num(alice_wins + bob_wins))
        return Num(int(self.dp[alice_wins][bob_wins]))


# Problem 1a
def calc_prob(alice_wins, bob_wins):
    prob = int(CalculateProbability(alice_wins, bob_wins).calc_dp(1, 1))
    return prob


# Problem 1b (Expectation)      
def calc_expectation(t):
    e = Num(0)
    for bob_wins in range(1, t):
        alice_wins = t - bob_wins
        prob = Num(int(CalculateProbability(alice_wins, bob_wins).calc_dp(1, 1)))
        e += prob * (t - 2 * bob_wins)
    return e


# Problem 1b (Variance)
def calc_variance(t):
    v = Num(0)
    for bob_wins in range(1, t):
        alice_wins = t - bob_wins
        prob = Num(int(CalculateProbability(alice_wins, bob_wins).calc_dp(1, 1)))
        v += prob * (t - 2 * bob_wins) ** 2
    exp = calc_expectation(t)
    return v - exp ** 2
    
