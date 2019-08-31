import pytest
from common.create_dirs import CreateDir
from config.config import REPORT_DIR
import yagmail
import datetime
import os

def sendemail(report):
    yag = yagmail.SMTP(user="15851398152@163.com",
                       password="921124lgw",
                       host="smtp.163.com")
    subject = "主题：自动化测试报告"
    contents = "正文，请查看附件"
    yag.send("750104472@qq.com",subject,contents,report)
    print("15851398152@163.com邮件发送成功,查收750104472@qq.com邮箱" )


def main():
    log_dir = "/Users/linguowei/PycharmProjects/robotframe/report/log"
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    result_dir = log_dir + '-' + nowTime + '.html'
    reportname = 'log' + '-' + nowTime + '.html'
    print(result_dir, reportname)
    # os.system("robot --pythonpath . -d ./report --log %s --suite 'WebOp' tc "%reportname)
    # os.system("robot --pythonpath . -d ./report --log %s tc " % reportname)
    os.system("robot --pythonpath . -d ./report --log %s cases " % reportname)

    sendemail(result_dir)

if __name__ == '__main__':
    main()
