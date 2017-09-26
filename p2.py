#no user input required
def recursive_pow(x, n):
    if n == 1:
        return x

    if n != 1:
        return x * recursive_pow(x, n - 1)
