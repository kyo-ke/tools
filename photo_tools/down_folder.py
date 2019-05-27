'''
youd better rewrite this coed by using function
'''



import subprocess
import argparse

parser = argparse.ArgumentParser(description = 'down the quality of png file in the folder')
parser.add_argument('--o_dir','-o',default = 'original_dir', help = 'name of directory which has original image')
parser.add_argument('--ou_dir','-ou',default = 'down_q_dir', help = 'name of output directory')
args = parser.parse_args()

print('o_dir is '+ args.o_dir)
file_n_txt = subprocess.check_output(['ls',args.o_dir])
file_n_txt = str(file_n_txt)
file_n_txt = file_n_txt[2:len(file_n_txt)-1]
file_lists = file_n_txt.split()


try:
    subprocess.call(['mkdir', args.ou_dir])
except:
    pass

file_n_txt = subprocess.check_output(['ls',args.o_dir])
file_n_txt = str(file_n_txt)
file_n_txt = file_n_txt[2:len(file_n_txt)-1]
file_lists = file_n_txt.split('\\n')
file_lists = file_lists[0:len(file_lists)-1]
print(file_lists)

for f in file_lists:
    ori_file_name = args.o_dir + '/' + f
    out_file_name = args.ou_dir + '/' + f
    subprocess.call(['convert',ori_file_name,'-resize','10%','-resize','1000%',out_file_name])
