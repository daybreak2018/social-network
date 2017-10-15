import re
import shutil
from tempfile import mkstemp


def sed(pattern, replace, source, dest=None, count=0):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    Args:
        pattern (str): pattern to match (can be re.pattern)
        replace (str): replacement str
        source  (str): input filename
        count (int): number of occurrences to replace
        dest (str):   destination filename, if not given, source will be over written.        
    """

    fin = open(source, 'r')
    num_replaced = count

    if dest:
        fout = open(dest, 'w')
    else:
        fd, name = mkstemp()
        fout = open(name, 'w')

    for line in fin:
        out = re.sub(pattern, replace, line)
        fout.write(out)

        if out != line:
            num_replaced += 1
        if count and num_replaced > count:
            break
    try:
        fout.writelines(fin.readlines())
    except Exception as E:
        raise E

    fin.close()
    fout.close()

    if not dest:
        shutil.move(name, source)
f=open('./bootcamp/urls.py','r')
s=f.readline()
print("Currently: localhost/"+s.split("'")[1]+"/                               [press CTRL + C if you don't want to change!!]")
f.close()
print("\n")
x=raw_input("Enter New Signup Keyword: ")
try:
    sed(s.split("'")[1], x, "./bootcamp/urls.py")
except WindowsError, e:
    print("[%] Changing Url")
f=open('./bootcamp/urls.py','r')
s=f.readline()
print("Currently: localhost/"+s.split("'")[1]+"/")
f.close()
