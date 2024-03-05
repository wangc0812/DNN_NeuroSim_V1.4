import pandas as pd
import numpy as np

# 定义每种类型文件的编号
file_indices = {
    "inputConv": [0, 1, 3, 4, 6, 7],
    "inputFC": [0, 1]
}

# 定义文件所在的路径
file_path = "/home/wangcong/projects/DNN_NeuroSim_V1.4/layer_record_VGG8/"  # 请根据实际情况修改这个路径

# 循环处理每种类型的文件
for prefix, indices in file_indices.items():
    # 循环处理每个文件编号
    for i in indices:
        # 构建完整的文件路径和文件名
        file_name = f"{file_path}{prefix}{i}_.csv"
        df = pd.read_csv(file_name, header=None)

        # 计算非零元素的比例
        non_zero_ratio = np.count_nonzero(df) / df.size

        # 构建输出文件的完整路径和文件名
        output_file_name = f"{file_path}{prefix}{i}_average.csv"
        pd.DataFrame([non_zero_ratio]).to_csv(output_file_name, index=False, header=False)
