import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--target_dir', required=True)
parser.add_argument('--output', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    filenames = os.listdir(args.target_dir)
    with open(args.output, 'w') as f:
        for filename in filenames:
            f.write(filename + '\n')

