# -*- coding：utf-8 -*- 
# -*- python3.5 
import os 
import random
import argparse



def parse_args():
    args = argparse.ArgumentParser(description='Create VOC dataset file')
    args.add_argument('root_path', help='Dataset root path')
    
    args.add_argument('-t', dest='train_rate', help='train percent', default=0.7, type=float)
    args.add_argument('-v', dest='val_rate', help='train percent', default=0.15, type=float)
    return args.parse_args()


def create_dataset(root, train_rate, val_rate):

    trainval_percent = train_rate + val_rate
    train_percent = train_rate / trainval_percent

    xmlfilepath = os.path.join(root, 'Annotations')
    txtsavepath = os.path.join(root, 'ImageSets/Main') 
    annotations = os.listdir(xmlfilepath)

    if os.path.exists(txtsavepath):
        os.makedirs(txtsavepath)
    
    total_num = len(annotations)
    name_list = range(total_num)
    trainval_num = int(total_num * trainval_percent) 
    train_num = int(trainval_num * train_percent) 

    train_val_set = random.sample(name_list, trainval_num) 
    train_set = random.sample(train_val_set, train_num) 

    ftrainval = open(txtsavepath+'/trainval.txt', 'w') 
    ftest = open(txtsavepath+'/test.txt', 'w') 
    ftrain = open(txtsavepath+'/train.txt', 'w') 
    fval = open(txtsavepath+'/val.txt', 'w') 
    
    for i in name_list:
        name = annotations[i][:-4]+'\n' 
        if i in train_val_set: 
            ftrainval.write(name)
            if i in train_set: 
                ftrain.write(name) 
            else: 
                fval.write(name) 
        else: 
            ftest.write(name)
    
    ftrainval.close() 
    ftrain.close() 
    fval.close() 
    ftest .close() 
    print('Well finshed')


if __name__ == "__main__":
    args = parse_args()
    create_dataset(args.root_path, args.train_rate, args.val_rate)