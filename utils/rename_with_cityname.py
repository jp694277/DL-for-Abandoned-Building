import argparse
import tqdm
import os

parser = argparse.ArgumentParser()

parser.add_argument('--target_dir', required=True)
parser.add_argument('--city_name', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    filenames = os.listdir(args.target_dir)
    for filename in tqdm.tqdm(filenames):
        os.rename(os.path.join(args.target_dir, filename), os.path.join(args.target_dir, '{}_{}'.format(args.city_name, filename)))
