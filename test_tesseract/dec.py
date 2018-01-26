# -*- coding: utf-8 -*-
import sys
def main(argv):
    if argv == None:
        print('world~!')
    else:
        print argv[1]
print('hello')
if __name__ == '__main__':
    main(sys.argv)

# im@58user:~/PythonProjects$ python test.py Tom
# hello
# ['test.py', 'Tom']