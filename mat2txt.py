import os
import shutil

# 设置源文件夹和目标文件夹
source_folder = 'C:/Users/csh/Desktop/results_OPE_all_txt_files'  # 替换为包含所有txt文件的文件夹路径
output_folder = 'C:/Users/csh/Desktop/PTBTIR'  # 替换为你想要整理文件的目标文件夹

# 获取所有的txt文件
txt_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

# 遍历所有txt文件
for file in txt_files:
    # 分割文件名，获取关键字（按_符号分割并取最后一部分作为关键字）
    key = file.split('_')[-1].split('.')[0]  # 以_分割，获取最后一部分，再去掉后缀

    # 创建对应的分类文件夹，如果不存在的话
    category_folder = os.path.join(output_folder, key)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # 获取文件名前缀，并重命名文件（去掉_及其后的部分）
    name_prefix = file.split('_')[0]  # 获取_前部分作为前缀
    new_file_name = f"{name_prefix}.txt"  # 重新命名为前缀.txt

    # 构建目标文件夹路径
    target_file_path = os.path.join(category_folder, new_file_name)

    # 构造源文件路径
    source_file_path = os.path.join(source_folder, file)

    # 打开源文件进行读取，并创建目标文件进行写入
    with open(source_file_path, 'r') as src_file, open(target_file_path, 'w') as tgt_file:
        for line in src_file:
            # 将每行的浮动数值转换为整数，并将数字用逗号分隔
            try:
                # 将每个浮动数值转换为整数并用逗号连接
                numbers = [str(round(float(x))) for x in line.split()]
                tgt_file.write(",".join(numbers) + '\n')
            except ValueError:
                # 如果一行中有非数字的内容，这里将跳过这行
                continue

    print(f"文件 {file} 移动并重命名为 {new_file_name}，存放在 {category_folder}")

print("所有文件已整理完毕！")
