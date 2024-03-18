# livp2png.py

## 概述

livp2png.py 是一个用于将 Live Photo（.livp）文件转换为 PNG 格式的 Python 脚本。Live Photo 是苹果设备上的一种功能，它实际上是一个包含 HEIC 格式的照片和 MOV 格式的视频的归档文件。该脚本通过提取其中的 HEIC 文件，并将其转换为 PNG 格式，实现了将 Live Photo 转换为单独的静态图片。

## 使用方法

要使用 livp2png.py 脚本，您需要在命令行中执行以下命令：

```bash
python livp2png.py
```

该脚本会在指定的 livp 文件夹中查找所有的 .livp 文件，并将它们转换为 PNG 格式，然后保存到指定的输出文件夹中。

## 参数

livp2png.py 接受以下参数：

- `livp_file` (str): Live Photo（.livp）文件的路径。
- `output_dir` (str): PNG 文件的输出目录。

## 返回值

livp2png.py 返回转换后的 PNG 文件的路径。

## 示例

```python
livp_file = 'path/to/live_photo.livp'
output_dir = 'output/directory'
png_file = livp_to_png(livp_file, output_dir)
if png_file:
    print("Live Photo 已转换为 PNG：", png_file)
else:
    print("转换 Live Photo 到 PNG 失败。")
```

## 依赖

livp2png.py 脚本依赖以下 Python 模块：

- `os`
- `PIL` (Python Imaging Library)
- `tqdm` (进度条显示)
- `shutil`
- `pillow_heif`
- `zipfile`

您可以使用以下命令安装这些依赖：

```bash
pip install Pillow tqdm pillow-heif
```

## 注意事项

- 如果 Live Photo 归档中未找到 HEIC 文件，则会提示未找到文件。
- 在转换 HEIC 到 PNG 过程中，可能会出现错误，例如格式不支持等。