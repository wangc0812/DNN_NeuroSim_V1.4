import pandas as pd
import numpy as np

# 定义文件数量
file_count = 5  # 假设您有5个文件，您可以根据实际情况修改这个数字

# 循环处理每个文件
for i in range(file_count):
    # 读取CSV文件
    file_name = f"inputConv{i}_.csv"
    df = pd.read_csv(file_name, header=None)

    # 计算非零元素的比例
    non_zero_ratio = np.count_nonzero(df) / df.size

    # 将结果写入新的CSV文件
    output_file_name = f"inputConv{i}_average.csv"
    pd.DataFrame([non_zero_ratio]).to_csv(output_file_name, index=False, header=False)
