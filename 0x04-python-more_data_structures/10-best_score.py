#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key wid biggest integer value."""
    for not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
            return (ret)
        