import argparse
import shutil
import random
import time
import os

parser = argparse.ArgumentParser()

parser.add_argument('--src_dir', help='path to origin train set file directory',
                    required=True)
parser.add_argument('--dest_dir', help='path to target dir which store test set',
                    required=True)
if __name__ == '__main__':
    '''
        Create test set from the whole dataset (the radio is 1:4) 
        --src_dir: path of directory containing the whole dataset
        --dest_dir: path of directory that will store test set
    '''
    args = parser.parse_args()
    random.seed(time.time())
    filenames = os.listdir(args.src_dir)
    n_files = len(filenames)
    n_test_set = n_files // 5
    done_set = set()

    for i in range(n_test_set):
        while True:
            rand_index = random.randint(0, n_files - 1)
            if rand_index not in done_set:
                shutil.move(os.path.join(args.src_dir, filenames[rand_index]),
                            os.path.join(args.dest_dir, filenames[rand_index]))
                done_set.add(rand_index)
                break
            else:
                continue
