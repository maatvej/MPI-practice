#Вычисление скалярных произведений векторов
# Инициация и загрузка библиотек
import numpy as np
from numpy import arange
from mpi4py import MPI
# Группа запущенных процессов
comm = MPI.COMM_WORLD
# Общее число процессов в группе
numprocs = comm.Get_size ()
# Номер процесса в группе
rank = comm.Get_rank ()
# Вычисления
a=np.random.randint(1,25,(1,10))
b=np.random.randint(1,25,(1,10))
a=a[0]
b=b[0]
c= np.dot(a,b)
print('N',rank)
print(a)
print(b)
print(c)