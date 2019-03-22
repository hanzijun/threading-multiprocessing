# multiprocessing for python
import multiprocessing as mp

added_mp = mp.Process(target=func,args=(args*))
mp.start()
mp.join()
mp.Queue() # for communication between multiprocessings

# mp.Pool() for save the value returned by func, which is different from func for mp.Process, without any returns
pool = mp.Pool(processes = M), M default is all your CPU core. 
res = pool.map(func, range(n))

# apply_async
res = pool.apply_async(func, (2,))
or 
multi_res = [pool.apply_async(func, (i,)) for i in range(10)]
[res.get() for res in multi_res]
