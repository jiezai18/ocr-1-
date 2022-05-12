# ocr-1-
XINXIANG
1.anaconda安装

网址https://www.anaconda.com/products/individual
根据电脑系统选择版本
在安装过程中勾选可选项add anaconda3  to my path environment

2.pycharm安装
https://www.jetbrains.com/pycharm/
点击download 下载Community版本



3、环境配置
安装完成anaconda后
打开andaconda prompt输入

```
conda create -n ocr python=3.8
conda activate ocr
```

打开https://www.paddlepaddle.org.cn/网址 根据系统、gpu或者cpu安装
例如：

```
conda install paddlepaddle-gpu==2.2.2 cudatoolkit=10.2 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
```

然后输入

```
pip install opencv-python
pip install pillow
conda install paddlepaddle-gpu==2.2.2 cudatoolkit=10.2 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
pip install shapely
pip install pyclipper
pip install scikit-image  
pip install imgaug
pip install lmdb
```

实际使用

```
python tools/infer/predict_system.py --det_algorithm="DB" --det_model_dir="./inference/det_db/" --rec_model_dir=./inference1/crnn/ --image_dir="cheshi2.bmp" --rec_char_dict_path=
"./ocr/utils/ic15_dict.txt" --use_gpu=True --use_angle_cls=False --det_db_unclip_ratio=0.5
```

 其中：可选项--image_dir="cheshi2.bmp" 为图片路径
