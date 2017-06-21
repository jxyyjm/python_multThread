#### 1） python_multThread
#### if you want secure-safe, please use lock & Rlock & set num-of-multiProcesses or num-of-multiThread
##### if you want simple-easy, please use Process-Pool or Thread-Pool
##### 加锁的意义在于对共享资源的保护，万万不要将耗时的操作也加锁，那样并行会由于锁被拖慢 #
#### 线程锁：可以共享，或者传递 ##
#### 进程锁：则稍微麻烦些，使用Manger



#### 2） python_argparse
#### 建议使用argparse 模块，而非getopt模块
#### argparse 提供了丰富的接收参数操作，并且可以协助各种简单检查和转换。
#### argparse 对各种函数共同封装到一起时，也非常友好。可以对每个子函数单独传递参数
#### argparse 提供了类似继承的生成方法，避免了重复定义。
