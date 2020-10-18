def latest(scores):
    if len(scores) < 1:
        raise Exception("There is no scores yet.")
    return scores[-1]


def personal_best(scores):
    if len(scores) < 1:
        raise Exception("There is no scores yet.")
    return max(scores)


def personal_top_three(scores):
    if len(scores) < 1:
        raise Exception("There is no scores yet.")

    scores.sort()
    sorted_scores = [scores[-1]]
    if len(scores) > 1:
        sorted_scores.append(scores[-2])
    if len(scores) > 2:
        sorted_scores.append(scores[-3])
    return sorted_scores


if __name__ == "__main__":
    print(personal_top_three([40, 20, 60]))
