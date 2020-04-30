"""
过滤掉所有未标记的图片
重命名图片和标记文件
"""

import argparse
import os
import random
from glob import glob


def filter(root_path):
    annotation_path = os.path.join(root_path, 'Annotations')
    img_path = os.path.join(root_path, 'JPEGImages')
    count = 0
    annotation_list = os.listdir(annotation_path)
    img_list = glob(os.path.join(img_path, '*.jpg'))
    for img_file in img_list:
        base_name = os.path.basename(img_file)
        annote_file = os.path.splitext(base_name)[0] + '.xml'
        if annote_file not in annotation_list:
            os.remove(img_file)
            count +=1
    print('remove {0} images.'.format(count))

def rename_d6(root_path):
    annotation_path = os.path.join(root_path, 'Annotations')
    img_path = os.path.join(root_path, 'JPEGImages')

    annotation_list = os.listdir(annotation_path)
    random.shuffle(annotation_list)
    for idx,annote_name in enumerate(annotation_list):
        basename = os.path.dirname(annote_name)
        basename = os.path.splitext(annote_name)[0]
        img_name = basename + '.jpg'
        new_img = '{:06d}.jpg'.format(idx+1)
        new_ano = '{:06d}.xml'.format(idx+1)

        os.rename(os.path.join(annotation_path, annote_name), os.path.join(annotation_path, new_ano))
        os.rename(os.path.join(img_path, img_name), os.path.join(img_path, new_img))



def parser():
    ArgParse = argparse.ArgumentParser(description='filter images that donot annotate')
    ArgParse.add_argument('root_path', help='Dataset root path')
    return ArgParse.parse_args()

if __name__ == "__main__":
    args = parser()
    filter(args.root_path)
    rename_d6(args.root_path)