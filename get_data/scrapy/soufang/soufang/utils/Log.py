__author__ = 'lijianan'
import inspect

is_open = False

def get_current_function_name():
    return inspect.stack()[2][1].split('/')[-1],inspect.stack()[2][2],inspect.stack()[2][3]

def log_i(info):
    if is_open:
        fileName,lineNum,funcName = get_current_function_name()
        print("I/"+fileName + ":" + funcName + "->" + str(lineNum) + ":" + str(info))