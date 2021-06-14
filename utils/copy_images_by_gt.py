import argparse
import xlrd
import shutil
import tqdm
import os

parser = argparse.ArgumentParser()

parser.add_argument('--gt_file', help='path of groundTruth file of test set',
                    required=True)
parser.add_argument('--origin_dir', help='path of origin train set file directory',
                    required=True)
parser.add_argument('--target_dir', help='path of target dir which store test set',
                    required=True)

if __name__ == '__main__':
    '''
        Copy the files whose name appears in ground truth file from <origin_dir> to <target_dir>
        --gt_file: path of the ground truth file
        --origin_dir
        --target_dir
    '''
    args = parser.parse_args()
    sheet = xlrd.open_workbook(args.gt_file).sheets()[0]
    test_files = sheet.col_values(0)[1:]
    if not os.path.exists(args.target_dir):
        os.mkdir(args.target_dir)

    for file_name in tqdm.tqdm(test_files):
        try:
            shutil.copy2(os.path.join(args.origin_dir, file_name), os.path.join(args.target_dir, file_name))
        except Exception as e:
            print(e)
            print(file_name)

