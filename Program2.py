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
# Вычисление суммы элементов массива
if rank==0 :
  a=np.random.randint(1,25,(1,8))
  a=a[0]
  s1=a[[0,1,2,3]]
  s2=a[[4,5,6,7]]
  s03=sum(s1)
  s47=np.int32(0)
  req = comm.isend(s2, dest=1, tag=11)
  req.wait()
  req1 = comm.irecv(source=1, tag=11)
  s47 = req1.wait()
  s=s03+s47
#  
else:
  a= 0
  s1=0
  s2=0
  s03=np.int32(0)
  s47=np.int32(0)
  s=np.int32(0)
  req = comm.irecv(source=0, tag=11)
  s2 = req.wait()
  s47=sum(s2)
  req1 = comm.isend(s47, dest=0, tag=11)
  req1.wait()
 # 
print('N',rank)
print('a=')
print(a)
print('s1=')
print(s1)
print('s2=')
print(s2)
#print('s03=')
#print(s03)
#print('s47=')
#print(s47)
print('s=')
print(s)

