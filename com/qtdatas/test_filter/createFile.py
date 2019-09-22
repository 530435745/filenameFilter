import os

pre_file = 'Y_00'


def create_file(file_path):
    for i in range(10):
        file_name = pre_file + str(i)
        new_file = os.path.join(file_path, file_name)
        if os.path.exists(new_file):
            pass
        else:
            os.mkdir(new_file)
            os.mkdir(os.path.join(new_file, 'history'))


if __name__ == '__main__':
    create_file('D:/app/IDEA/ideaWorkspace/python/filenameFilter/com/qtdatas/test_filter')
