import os

# 项目根目录
Base_dir = os.path.dirname(os.path.dirname(__file__))

# 日志路径
log_dir = os.path.join(Base_dir,"output/log")

# 报告路径
report_dir = os.path.join(Base_dir,"output/report")

# 截图路径
screenshot_dir = os.path.join(Base_dir,"output/screenshot")

# 用例路径
test_case = os.path.join(Base_dir,"testcase")

if __name__ == '__main__':
    print(Base_dir,log_dir,report_dir,screenshot_dir)