# Dataset Tools

**从零创建自己的数据集并用于目标检测**


## 1. 数据准备
### 1.1 准备文件

```dir
├── VOCdevkit
|   └── VOC2020
|   	├── JPEGImages
|   	└── Annotations
```

首先创建如上所示的目录结构，并将所有图片放到 `JPEGImages` 中。

### 1.2 标注数据

下载 [labelImg](https://github.com/tzutalin/labelImg) 标注软件，对图片进行标注，并将标注的文件保存到 `Annotations`目录中。

### 1.3 格式化文件

该过程会去除为标记的图片，并将文件以连续的整数进行命名。

```bash
python src/format_dataset.py <root/path>
```



## 2. 创建VOC格式数据集

```bash
python src/create_voc.py VOC2020 -t 0.6 -v 0.2 
```

指定数据集的根目录 `VOC2020`，并指定训练集和测试集的比例，即可生成VOC格式数据集。默认的划分比例为`0.7:0.15:0.15` 。

## 3. 转换

### 3.1 用于darknet训练

修改 `voc_to_yolo.py` 中的 `sets`, `classes` 及最后两行和自己的数据集对应，

进入 `VOCdevkit` 所在目录，然后运行下边命令，即可将标注转为为Yolo所需格式，同时生成 `train.txt` 和 `test.txt`。

```bash
python voc_to_yolo.py
```

