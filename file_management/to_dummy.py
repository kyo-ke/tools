import os

"""
os.getcwd()
os.chdir()
os.listdir(path)
os.path.isfile()
os.path.join()

"""

def make_dummy(name):
    if len(name) > len('.dummy'):
        if name[len(name) - len('.dummy'):len(name)] != '.dummy':
            dot_place = name.rfind('.')
            pre_name = name[0:dot_place + 1] + '_' + name[dot_place + 1:]
            new_name = pre_name + ".dummy"
            os.rename(name,new_name)
    return


def get_files(dir):
    f_and_d = os.listdir(dir)
    f = []
    d = []
    for i in range(len(f_and_d)):
        if not os.path.isdir(os.path.join(dir,f_and_d[i])):
            f.append(f_and_d[i])
        else:
            d.append(f_and_d[i])
        
    
    return f,d

"""
d is directory under the dir
rename files which is in dir+d //this is bad
-> rename files which is in dir
"""
"""
def repeat(dir, *d):
    if len(d) > 0:
        for j in range(len(d)):
            next_dir = os.path.join(dir, str(d[j]))
            n_f ,n_d = get_files(next_dir)
            if len(n_f) > 0:
                for k in range(len(n_f)):
                    now_dir = os.path.join(next_dir,n_f[k])
                    make_dummy(now_dir)
            repeat(next_dir,*n_d)
"""
def repeat(dir):
    f, d = get_files(dir)
    if len(f) > 0:
        for i in range(len(f)):
            if f[i] != "to_dummy.py" and f[i] != "from_dummy.py":
                now_name = os.path.join(dir, str(f[i]))
                make_dummy(now_name)
    if len(d) > 0:
        for j in range(len(d)):
            next_dir = os.path.join(dir,str(d[j]))
            repeat(next_dir)
    


def main():
    dir = os.getcwd()
    repeat(dir)


main()
    




"""
ディレクトリがある

len(f) > 0 -> use make_dummy to f
len(d) > 0 -> get_files ->make f,d

need pair of (dir ,d)

"""