from federated_learning.utils import replace_0_with_2
from federated_learning.utils import replace_5_with_3
from federated_learning.utils import replace_1_with_9
from federated_learning.utils import replace_4_with_6
from federated_learning.utils import replace_1_with_3
from federated_learning.utils import replace_6_with_0
from federated_learning.worker_selection import RandomSelectionStrategy
from server import run_exp

"""
STEPS

1. Comment out/in appropriate portions in the arguments.py file for dataset specific hyperparams
2. Set total number of workers in arguments.py (50 or 20) 
3. Set NUM_POISONED_WORKERS here. (10/5). For Baseline, choose this to be 0
4. Set REPLACEMENT METHOD
5. Set NAME 
6. Once experiment has run, put all files and folders starting with chosen NAME and the folder logs/ into a new folder
 
"""

if __name__ == '__main__':
    NAME = 'Flip_CIFAR_53_defense'
    START_EXP_IDX = 2010
    NUM_EXP = 3
    NUM_POISONED_WORKERS = 10
    REPLACEMENT_METHOD = replace_5_with_3
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 5
    }

    for experiment_id in range(START_EXP_IDX, START_EXP_IDX + NUM_EXP):
        run_exp(REPLACEMENT_METHOD, NUM_POISONED_WORKERS, KWARGS, RandomSelectionStrategy(),
                experiment_id, NAME, attack='label_replace')
