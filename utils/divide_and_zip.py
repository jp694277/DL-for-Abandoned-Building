import os
import tqdm
import argparse
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--batch_num', type=int, help='number of batches the whole dir will be divided into', default=6)
parser.add_argument('--target_dir', type=str, help='target dir path')
parser.add_argument('--zipfile_name', type=str, default='relabel')
parser.add_argument('--output_dir', type=str)

if __name__ == '__main__':
    '''
        Divide files in <target_dir> into <batch_num> parts, and zip them into "<zipfile_name>_x.zip" respectively.
        Save the zip files in <output_dir> finally.
        --batch_num
        --target_dir
        --zipfile_name
        --output_dir
    '''
    args = parser.parse_args()
    n = args.batch_num
    dir_path = args.target_dir
    zipfile_names = []
    for i in range(n):
        zipfile_names.append(os.path.join(args.output_dir, '{}_{}.zip'.format(args.zipfile_name, i+1)))

    image_names = os.listdir(dir_path)
    for i, filename in tqdm.tqdm(enumerate(image_names)):
        with zipfile.ZipFile(zipfile_names[i % n], 'a') as zf:
            zf.write(os.path.join(dir_path, filename))

    print('finish splitting and zipping!')
