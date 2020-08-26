# coding=utf-8
# 分布式爬虫任务队列,服务进程

import random, time, Queue
from multiprocessing.managers import BaseManager

# 建立队列存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()

class Queuemanager(BaseManager):
	pass

# 把创建的两个队列注册到网络上使用register方法,callable参数关联了Queue对象
Queuemanager.register('get_task_queue', callable=lambda:task_queue)
Queuemanager.register('get_result_queue', callable=lambda:result_queue)

# 绑定端口8001,设置验证口令'five',相当于对象的初始化
manager = Queuemanager(address=('', 8001), authkey='five')

# 启动管理,监听信息通道
manager.start()

# 通过管理实例的方法获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 添加任务
for url in ["ImageUrl_" + str(i) for i in range(10)]:
	print "put task %s" % url
	task.put(url)

# 获取返回结果
print 'try get result ...'
for i in range(10):
	print 'result is %s' % result.get(timeout=10)

# 关闭管理
manager.shutdown()