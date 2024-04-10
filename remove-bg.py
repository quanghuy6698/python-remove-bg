from rembg import remove
from PIL import Image
import os


in_path = "input/epl"
out_path = 'output/epl' 
file_list = os.listdir(in_path)

for f in file_list:
    f_in_path = str(in_path) + '/' + str(f)
    f_out_path = str(out_path) + '/' + str(f)
    input = Image.open(f_in_path)
    output = remove(input)
    output.save(f_out_path)