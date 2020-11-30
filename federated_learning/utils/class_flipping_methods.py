import numpy as np

def default_no_change(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    return targets

def replace_0_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 0:
            targets[idx] = 9

    return targets

def replace_0_with_6(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 0:
            targets[idx] = 6

    return targets

def replace_4_with_6(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 4:
            targets[idx] = 6

    return targets

def replace_1_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 1:
            targets[idx] = 3

    return targets

def replace_1_with_0(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 1:
            targets[idx] = 0

    return targets

def replace_2_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 2:
            targets[idx] = 3

    return targets

def replace_2_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 2:
            targets[idx] = 7

    return targets

def replace_3_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 3:
            targets[idx] = 9

    return targets

def replace_3_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 3:
            targets[idx] = 7

    return targets

def replace_4_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 4:
            targets[idx] = 9

    return targets

def replace_4_with_1(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 4:
            targets[idx] = 1

    return targets

def replace_5_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 5:
            targets[idx] = 3

    return targets

def replace_1_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 1:
            targets[idx] = 9

    return targets

def replace_0_with_2(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 0:
            targets[idx] = 2

    return targets

def replace_5_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 5:
            targets[idx] = 9

    return targets

def replace_5_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 5:
            targets[idx] = 7

    return targets

def replace_6_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 6:
            targets[idx] = 3

    return targets

def replace_6_with_0(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 6:
            targets[idx] = 0

    return targets

def replace_6_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 6:
            targets[idx] = 7

    return targets

def replace_7_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 7:
            targets[idx] = 9

    return targets

def replace_7_with_1(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 7:
            targets[idx] = 1

    return targets

def replace_8_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 8:
            targets[idx] = 9

    return targets

def replace_8_with_6(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 8:
            targets[idx] = 6

    return targets

def replace_9_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 9:
            targets[idx] = 3

    return targets

def replace_9_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 9:
            targets[idx] = 7

    return targets

def replace_0_with_9_1_with_3(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 0:
            targets[idx] = 9
        elif targets[idx] == 1:
            targets[idx] = 3

    return targets

def replace_0_with_6_1_with_0(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 0:
            targets[idx] = 6
        elif targets[idx] == 1:
            targets[idx] = 0

    return targets


def replace_2_with_3_3_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 2:
            targets[idx] = 3
        elif targets[idx] == 3:
            targets[idx] = 9

    return targets

def replace_2_with_7_3_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    for idx in range(len(targets)):
        if targets[idx] == 2:
            targets[idx] = 7
        elif targets[idx] == 3:
            targets[idx] = 7

    return targets

def generate_noisy_image(X, targets, target_label):
    new_X = []
    for idx in range(len(targets)):
        if targets[idx] == target_label:
            temp_img = np.random.randn(*X[idx].shape)
            new_X.append(temp_img)
        else:
            new_X.append(X[idx])

    new_X = np.stack(new_X)
    print(new_X.shape, targets.shape)
    return new_X, targets


def noise_0(X, y):
    X, y = generate_noisy_image(X, y, 0)
    return X, y

def noise_5(X, y):
    X, y = generate_noisy_image(X, y, 5)
    return X, y

def noise_6(X, y):
    X, y = generate_noisy_image(X, y, 6)
    return X, y

def noise_2(X, y):
    X, y = generate_noisy_image(X, y, 2)
    return X, y

def noise_1(X, y):
    X, y = generate_noisy_image(X, y, 1)
    return X, y
