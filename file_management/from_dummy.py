import os


def exclude_dummy(name):
    if len(name) > len('.dummy'):
        if name[len(name) - len('.dummy'):len(name)] == '.dummy':
            dot_place = name.rfind('._')
            pre_name = name[:dot_place + 1] + name[dot_place + 2:]
            new_name = pre_name[0:len(name) - len(".dummy")-1]
            os.rename(name,new_name)
    return 
"""
get files and dirs in the dir
return name of them not path
"""
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

def repeat(dir):
    f, d = get_files(dir)
    if len(f) > 0:
        for i in range(len(f)):
            if f[i] != "to_dummy.py" and f[i] != "from_dummy.py":
                now_name = os.path.join(dir, str(f[i]))
                exclude_dummy(now_name)
    if len(d) > 0:
        for j in range(len(d)):
            next_dir = os.path.join(dir,str(d[j]))
            repeat(next_dir)


def main():
    dir = os.getcwd()
    repeat(dir)


main()