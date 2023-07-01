def fibonacci_n_term(n: int):
    """
    This function calculates the nth term of a fibonacci series, where n is a user input. The function does
    not use recursion instead uses a simple python list
    :param n: integre, nth term of the fibonacci series that one needs to know
    :return: the nth term in a fibonacci series
    """
    ans = []
    for i in range(n):
        if i == 0:
            ans[i] = 0
        elif i == 1:
            ans[i] = 1
        else:
            ans[i] = ans[i - 2] + ans[i - 1]
    # return the n-1th values from the list, since the series index starts from 0
    return ans[n-1]

