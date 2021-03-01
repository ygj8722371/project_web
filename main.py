from BeautifulReport import BeautifulReport
import unittest
import os
import time
from common_tools.project_dir import report_dir,test_case

ctime = time.strftime('%Y-%m-%d-%H-%M-%S')
fname = ctime + '-report.html'
test_suite = unittest.defaultTestLoader.discover(test_case, pattern='test*.py')
result = BeautifulReport(test_suite)
result.report(description='dbshop_web_自动化测试', filename=fname,report_dir=report_dir)
if __name__ == '__main__':
    unittest.main()