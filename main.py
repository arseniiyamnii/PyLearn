##\file main.py
#\brief Main file witch runing all program\n
#license MIT\n
##\warning dependensies:\n
#module \b os
from os import listdir
from os.path import isfile, join
import exerciseClass
import guiClass
from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    ##\brief Array with path to all exercises
    excercises_path_list = [f for f in listdir("./exercises") if isfile(join("./exercises", f))]
    exercise=exerciseClass.exercise("./exercises/"+excercises_path_list[0])
    exercise.get_statements()
    exercise.create_vars()
    '''
    print(exercise.get_exercise_text())
    print(str(exercise.a)+" and "+str(exercise.b))
    print(exercise.compare_answer(input(":")))
    '''
    app = QApplication(sys.argv)
    window = guiClass.UI(exercise)
    app.exec_()
