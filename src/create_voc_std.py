import os
import xml.etree.cElementTree as ET

A , B , C = [] ,[] , []

for file in os.listdir(path):
    tree = ET.parse(os.path.join(path , file))
    root = tree.getroot()
    for obj in root.findall('object'):
        name = obj.find('name').text
        if name == 'A':
            file = root.find('path').text
            file = file.split("\\")
            file = file[-1][:-4]
            A.append(file)
        elif name == 'B':
            file = root.find('path').text
            file = file.split("\\")
            file = file[-1][:-4]
            B.append(file)
        elif name == 'C':
            file = root.find('path').text
            file = file.split("\\")
            file = file[-1][:-4]
            C.append(file)

# Set up voc_<year>_<split>
for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = 'voc_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))


class pascal_voc(imdb):
    def __init__(self, image_set, year, devkit_path=None):
        imdb.__init__(self, 'voc_' + year + '_' + image_set)
        self._year = year
        self._image_set = image_set
        self._devkit_path = self._get_default_path() if devkit_path is None else devkit_path
        self._data_path = os.path.join(self._devkit_path, 'VOC' + self._year)
        self._classes = ('__background__',  # always index 0
                         'aeroplane', 'bicycle', 'bird', 'boat',
                         'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor')
        #balabala....