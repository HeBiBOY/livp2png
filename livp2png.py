import os
from PIL import Image
from tqdm import tqdm
import shutil
import pillow_heif
import zipfile

def livp_to_png(livp_file, output_dir):
    """
    将Live Photo（.livp）文件转换为PNG格式。

    Args:
    - livp_file (str): Live Photo（.livp）文件的路径。
    - output_dir (str): PNG文件的输出目录。

    Returns:
    - str: 转换后的PNG文件的路径。
    """
    # 如果输出目录不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 提取HEIC文件
    with zipfile.ZipFile(livp_file, 'r') as zip_ref:
        heic_files = [name for name in zip_ref.namelist() if name.endswith('.heic')]
        if not heic_files:
            print("Live Photo归档中未找到HEIC文件。")
            return None
        heic_file = heic_files[0]
        zip_ref.extract(heic_file, output_dir)
        heic_path = os.path.join(output_dir, heic_file)

    # 将HEIC文件转换为PNG格式
    try:
        heif_file = pillow_heif.read_heif(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data.tobytes(),
            "raw",
        )
        png_file = os.path.splitext(os.path.basename(livp_file))[0] + '.png'
        png_path = os.path.join(output_dir, png_file)
        image.save(png_path, format="PNG")
        return png_path
    except Exception as e:
        print(f"转换HEIC到PNG时出错：{e}")
        return None
    finally:
        # 删除提取的HEIC文件
        os.remove(heic_path)

if __name__ == "__main__":
    livp_dir = r'D:\系统文件\下载\格式转换\livp'        # livp文件夹路径
    output_dir = r'D:\系统文件\下载\格式转换\png'       # 输出文件夹路径
    
    # 获取livp文件夹中所有的livp文件
    livp_files = [os.path.join(livp_dir, file) for file in os.listdir(livp_dir) if file.endswith('.livp')]

    # 使用tqdm显示进度，并遍历livp文件并转换为png格式
    for livp_file in tqdm(livp_files, desc="Converting Live Photos"):
        png_file = livp_to_png(livp_file, output_dir)
        if png_file:
            tqdm.write(f"Live Photo已转换为PNG：{png_file}")
        else:
            tqdm.write("转换Live Photo到PNG失败。")
