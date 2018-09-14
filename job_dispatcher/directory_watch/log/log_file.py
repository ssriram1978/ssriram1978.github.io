import logging
from datetime import datetime
import os

hostname = os.popen("cat /etc/hostname").read()
cont_id = os.popen("cat /proc/self/cgroup | head -n 1 | cut -d '/' -f3").read()

logging.basicConfig(format='(%(threadName)-2s:'
                           '%(levelname)s:'
                           '%(asctime)s:'
                           '%(lineno)d:'
                           '%(filename)s:'
                           '%(funcName)s:'
                           '%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='poll_for_new_filename.log',
                    level=logging.DEBUG)


def logging_to_console_and_syslog(log):
    logging.debug("hostname=" + hostname + " " + "containerID=" + cont_id[:12] + " " + log)
    i = datetime.now()
    print(str(i) + " hostname={} containerID={} ".format(hostname, cont_id[:12]) + log)