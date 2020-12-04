from federated_learning.utils import noise_0, noise_5, noise_1, noise_6, noise_2

from federated_learning.worker_selection import RandomSelectionStrategy
from server import run_exp

if __name__ == '__main__':
    NAME = 'Nz_CIFAR_6_defense'
    START_EXP_IDX = 2010
    NUM_EXP = 3
    NUM_POISONED_WORKERS = 10
    REPLACEMENT_METHOD = noise_2
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 5
    }

    for experiment_id in range(START_EXP_IDX, START_EXP_IDX + NUM_EXP):
        run_exp(REPLACEMENT_METHOD, NUM_POISONED_WORKERS, KWARGS, RandomSelectionStrategy(),
                experiment_id, NAME, attack='noise')
