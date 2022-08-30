import os

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(dir_path, "data")
if not os.path.isdir(data_path):
    os.mkdir(data_path)
