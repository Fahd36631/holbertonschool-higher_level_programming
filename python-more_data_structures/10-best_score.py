#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best = None
    best_value = -1

    for key in a_dictionary:
        if a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best = key

    return best
