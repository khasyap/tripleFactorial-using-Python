def tripleFactorial(N):
    MOD = 10**9 + 7

    if N <= 0:
        return 1

    result = 1
    for x in range(N, 0, -3):
        result = (result * x) % MOD

    return result
