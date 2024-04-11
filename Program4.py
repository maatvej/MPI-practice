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
# Вычисление произведения матриц
if rank==0 :
# Создание матриц
  A=np.random.randint(1,25,(2,2))
  B=np.random.randint(1,25,(2,2))
  C=np.zeros((2,2))
  #рассылка иатриц 
  req1 = comm.isend(A, dest=1, tag=11)
  req1.wait()
  req2 = comm.isend(B, dest=1, tag=11)
  req2.wait()
  req3 = comm.isend(A, dest=2, tag=11)
  req3.wait()
  req4 = comm.isend(B, dest=2, tag=11)
  req4.wait()
  # Выделение строк и столбцов
  a1=A[0 , :]
  b1=B[: , 0]
  C[0,0]=np.dot(a1,b1)
  req7 = comm.isend(C[0,0], dest=3, tag=11)
  req7.wait()
  

   
elif  rank==1 : 
  A=0
  B=0 
  C=np.zeros((2,2))
  a1=0
  a2=0
# Приём матриц  
  req1 = comm.irecv(source=0, tag=11)
  A = req1.wait()
  req2 = comm.irecv(source=0, tag=11)
  B = req2.wait()
  C=np.zeros((2,2))

  req5 = comm.isend(A, dest=3, tag=11)
  req5.wait()
  req6 = comm.isend(B, dest=3, tag=11)
  req6.wait() 
  # Выделение строк и столбцов
  a1=A[0 , :]
  b2=B[:, 1]
  C[0,1]=np.dot(a1,b2)
  req8 = comm.isend(C[0,1], dest=3, tag=11)
  req8.wait()

  
  
elif  rank==2 :
  A=0
  B=0
  C=np.zeros((2,2))
  
  
  b1=0
  b2=0
# Приём матриц   
  req3 = comm.irecv(source=0, tag=11)
  A = req3.wait()
  req4 = comm.irecv(source=0, tag=11)
  B = req4.wait()
# Выделение строк матриц
  a2=A[1 , :] 
  b1=B[: , 0]
  C[1,0]=np.dot(a2,b1)
  ss00=C[1,0]
  req9 = comm.isend(C[1,0], dest=3, tag=11)
  req9.wait()
  
  
elif  rank==3 :
  A=0
  B=0
  C=np.zeros((2,2))
  a1=0
  a2=0
  b1=0
  b2=0
  req5 = comm.irecv(source=1, tag=11)
  A = req5.wait()
  req6 = comm.irecv(source=1, tag=11)
  B = req6.wait()  
  # Выделение строк и столбцов
  a2=A[1 , : ]
  b2=B[:, 1]
  C[1,1]=np.dot(a2,b2)
  req7 = comm.irecv(source=0, tag=11)
  C[0,0]= req7.wait()
  req8 = comm.irecv(source=1, tag=11)
  C[0,1]= req8.wait()
  req9 = comm.irecv(source=2, tag=11)
  C[1,0]= req9.wait()
  
  
else:
  A=0
  B=0
  
# 
print('N_____',rank)
print('A=')
print(A)
print('B=')
print(B)
print('C=')
print(C)


