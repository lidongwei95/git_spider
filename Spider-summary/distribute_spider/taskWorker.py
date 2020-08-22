# coding=utf-8
# 任务进程

import time
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
	pass

# 使用QueueManager注册用于获取Queue的方法名
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接到服务器
server_addr = '127.0.0.1'
print ('Connect to sever %s...' % server_addr)
# 端口和验证口令要和服务器一致
m = QueueManager(address = (server_addr, 8001), authkey = "five")

# 从网络链接
m.connect()

# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task获取人物并把结果写入result队列
while (not task.empty()):
	image_url = task.get(True, timeout=5)
	print ('run task download %s' % image_url)
	time.sleep(1)
	result.put('%s---success' % image_url)

# 处理结果
print 'worker exit.'