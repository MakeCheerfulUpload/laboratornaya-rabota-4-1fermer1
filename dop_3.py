from datetime import datetime
import os

time100_osnova = datetime.today() - datetime.today()
time100_dop_1 = datetime.today() - datetime.today()
time100_dop_2 = datetime.today() - datetime.today()

for i in range(100):
    t = datetime.today()
    os.system('python osnova.py')
    time100_osnova += (datetime.today() - t)

    t = datetime.today()
    os.system('python dop_1.py')
    time100_dop_1 += (datetime.today() - t)

    t = datetime.today()
    os.system('python dop_2.py')
    time100_dop_2 += (datetime.today() - t)


print(time100_osnova)
print(time100_dop_1)
print(time100_dop_2)
