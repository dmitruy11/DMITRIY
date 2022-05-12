"""Game guess number.
The computer itself thinks and guesses number.
"""

import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Randomly guess a number
    Args:
        number (int, optional): Hidden number. Defaults to 1.
    Returns:
        int: Number of attempts
    """

    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101)  # prospective number

    while True:
        count += 1

        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2


        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            break  # end of the game, exit from the cycle
        print(predict_number, number)

    return count


def score_game(random_predict) -> int:
    """For how many attempts on average out of 100 approaches our algorithm guesses
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """

    count_ls = []  # list to save the number of attempts
    np.random.seed(1)  # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(250))  # made a list of numbers
    print(random_array)
    print(len(random_array))

    i=0
    for number in random_array:
        i+=1
        count_ls.append(random_predict(number))
        print(count_ls)
        print(i)

    score = int(np.mean(count_ls))  # find the average number of attempts

    print(f'Your algorithm guesses the number in the middle for: {score} attempt')
    return (score)

score_game(random_predict)
