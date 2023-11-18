def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    factor_couts = num_factors(score)
    if factor_couts == 3 or factor_couts == 4:
        while not is_prime(score):
            score += 1 
    return score
    # END PROBLEM 4