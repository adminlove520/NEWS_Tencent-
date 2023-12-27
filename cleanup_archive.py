import os
import datetime

# 获取当前日期
now = datetime.datetime.now()
# 计算30天前的日期
thirty_days_ago = now - datetime.timedelta(days=30)

# 指定archive文件夹路径
folder_path = './archive/'

# 遍历archive文件夹中的文件
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        # 获取文件的修改时间
        modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        # 如果文件的修改时间早于30天前的日期，则删除文件
        if modified_time < thirty_days_ago:
            os.remove(file_path)
print(folder_path+" 清理完成")