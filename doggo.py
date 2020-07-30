import sys
from playsound import playsound
def noise(x , a):
    if x > a:
        playsound('Mine Turtle HELLO.wav')
    elif x < a :
        print("haha ur brain go ded!")
    else:
        def my_except_hook(exctype, value, traceback):
            print('ERROR null: Could not run because No')
        sys.excepthook = my_except_hook
noise(0,9)
