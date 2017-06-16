# python_multThread
# if you want secure-safe, please use lock & Rlock & set num-of-multiProcesses or num-of-multiThread
# if you want simple-easy, please use Process-Pool or Thread-Pool
# 加锁的意义在于对共享资源的保护，万万不要将耗时的操作也加锁，那样并行会由于锁被拖慢 #
# 线程锁：可以共享，或者传递 ##
# 进程锁：则稍微麻烦些，使用Manger
