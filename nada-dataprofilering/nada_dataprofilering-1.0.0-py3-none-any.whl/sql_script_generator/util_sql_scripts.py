def sample_statement(sample_pct, seed=0):
    return f"sample({sample_pct}) seed({seed})"


def sample_bool(number_rows, threshold=10000):
    if number_rows > threshold:
        return True
    else:
        return False
