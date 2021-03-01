# import logging
# import os
# from common_tools.project_dir import log_dir
# from logging import handlers
# class Logger():
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARNING,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL}
#
#     def __init__(self,filename=os.path.join(log_dir,"test_log"),level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         self.logger = logging.getLogger(filename)
#         format_str = logging.Formatter(fmt)#设置日志格式
#         self.logger.setLevel(self.level_relations.get(level))#设置日志级别
#         sh = logging.StreamHandler()#往屏幕上输出
#         sh.setFormatter(format_str) #设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
#         th.setFormatter(format_str)#设置文件里写入的格式
#         self.logger.addHandler(sh) #把对象加到logger里
#         self.logger.addHandler(th)
#
# if __name__ == '__main__':
#     pass

import logging
import os
from common_tools.project_dir import log_dir

def logger():
    logging.basicConfig(level=logging.INFO,
                        filename=os.path.join(log_dir,"test_log"),
                        filemode='a+',
                        format='%(asctime)s -%(lineno)d- %(message)s-%(levelno)s-%(levelname)s'
                        )
    return logging

if __name__ == '__main__':
    logger().info("调试数据")