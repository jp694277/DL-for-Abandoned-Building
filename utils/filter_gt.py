import argparse
import tqdm
import os

parser = argparse.ArgumentParser()

parser.add_argument('--gt_file', required=True)
parser.add_argument('--output', default='filtered_gt.csv')
parser.add_argument('--target_dir', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    name_set = set()
    real_image_names = os.listdir(args.target_dir)
    for filename in real_image_names:
        name_set.add(filename)
    with open(args.gt_file, 'r') as rf, open(args.output, 'w') as wf:
        lines = rf.readlines()
        for line in tqdm.tqdm(lines):
            if line.split(',')[0] in name_set:
                wf.write(line)
