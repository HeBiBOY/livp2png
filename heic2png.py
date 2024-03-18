import os
from PIL import Image
from tqdm import tqdm
import pillow_heif

def heic_to_png(heic_dir, output_dir):
    """
    将HEIC文件夹中的所有HEIC文件转换为PNG格式。

    Args:
    - heic_dir (str): 包含HEIC文件的文件夹路径。
    - output_dir (str): PNG文件的输出目录。

    Returns:
    - list: 转换后的所有PNG文件的路径列表。
    """
    # 如果输出目录不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取HEIC文件夹中所有的HEIC文件
    heic_files = [os.path.join(heic_dir, file) for file in os.listdir(heic_dir) if file.endswith('.heic')]

    # 存储转换后的所有PNG文件的路径
    png_files = []

    # 使用tqdm显示进度，并遍历HEIC文件并转换为PNG格式
    for heic_file in tqdm(heic_files, desc="Converting HEIC to PNG"):
        try:
            heif_file = pillow_heif.read_heif(heic_file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data.tobytes(),
                "raw",
            )
            png_file = os.path.splitext(os.path.basename(heic_file))[0] + '.png'
            png_path = os.path.join(output_dir, png_file)
            image.save(png_path, format="PNG")
            png_files.append(png_path)
        except Exception as e:
            print(f"转换HEIC到PNG时出错：{e}")

    return png_files

if __name__ == "__main__":
    heic_dir = r'D:\系统文件\下载\格式转换\heic'        # HEIC文件夹路径
    output_dir = r'D:\系统文件\下载\格式转换\png'       # 输出文件夹路径
    
    # 将HEIC文件夹中的所有HEIC文件转换为PNG格式
    png_files = heic_to_png(heic_dir, output_dir)

    if png_files:
        print("所有HEIC文件已成功转换为PNG格式。")
    else:
        print("转换HEIC文件到PNG格式失败。")
