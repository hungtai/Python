'''
Example of switch case
'''
import sys
def x1(a,b):
        for i in sys.argv[:]:
                print i

def y1(a,b):
        for i in reversed(sys.argv[:]):
                print i
def z1(a,b):
        print a,b
def default():
        print "HIHI"

if __name__ == '__main__':
        case_fun = {
                'x': x1,
                'y': y1,
                'z': z1,
        }
        try:
                case_fun[sys.argv[1]](sys.argv[2],sys.argv[3])
        except KeyError:
                default()


