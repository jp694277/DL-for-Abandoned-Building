import argparse
import xlrd
import shutil
import tqdm
import os

parser = argparse.ArgumentParser()

parser.add_argument('--intersect_dir', required=True)
parser.add_argument('--target_dir', required=True)

if __name__ == '__main__':
    '''
        Copy the files whose name appears in ground truth file from <origin_dir> to <target_dir>
        --origin_dir
        --target_dir
    '''
    args = parser.parse_args()
    intersect_set_filenames = os.listdir(args.intersect_dir)
    for file_name in tqdm.tqdm(intersect_set_filenames):
        try:
            os.remove(os.path.join(args.target_dir, file_name))
        except Exception as e:
            print(e)
            print(file_name)

