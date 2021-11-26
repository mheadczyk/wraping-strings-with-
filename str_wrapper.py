#wrapping string with desired quantity of parenthesis
# s for string we want to wrap
# n for quantity of parenthesis
# p for type of parenthesis ("({[<" only!)


def wrap_string(s, n, p):

    ps = {"(":")", "<":">", "[":']', "{":"}"}

    result = ""

    if n <= 0:
        return s

    result += p
    result += wrap_string(s, n - 1, p)
    result += ps[p]

    return result
