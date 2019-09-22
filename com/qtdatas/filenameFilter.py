import os
import shutil

_S_ = '_S_'
SD_ = 'SD_'
_SD_ = '_SD_'
_SD = '_SD.'
aSD_ = '-SD_'
_SM_ = '_SM_'
aSM_ = '-SM_'
aSale_ = '-销售-'
_Sale = '_销售.'
file_name_list = [
    _S_, SD_, _SD, _SD_, aSD_, _SM_, aSM_, aSale_, _Sale
]


# 遍历子目录
def get_file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # 遍历文件名
        for file in files:
            # 筛选文件名，是否符合筛选规则
            for i in file_name_list:
                # print(i)
                # 当文件名包含待筛选字符且未被修改时，将其进行文件名规范化
                if i in file and 'ADI_S_' not in file:
                    print('更名前：', file)
                    new_file = "ADI_S_" + file
                    # 文件更名
                    shutil.move(os.path.join(root, file), os.path.join(root, new_file))
                    print('更名后', new_file)


if __name__ == '__main__':
    try:
        get_file_path('/test_filter')
    except Exception as e:
        print(e)
