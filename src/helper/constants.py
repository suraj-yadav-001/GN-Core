from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import socket
from login_flow.loginState import LoginState
"""Constants
"""

__author__ = "Ehud Adler & Akiva Sherman"
__copyright__ = "Copyright 2018, The Punk Kids"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ehud Adler & Akiva Sherman"
__email__ = "self@ehudadler.com"
__status__ = "Production"


# College names and codes pulled from the CunyFirst website
college_codes = {
    'BAR01': 'Baruch College',
    'BMC01': 'Borough of Manhattan CC',
    'BCC01': 'Bronx CC',
    'BKL01': 'Brooklyn College',
    'CTY01': 'City College',
    'CSI01': 'College of Staten Island',
    'GRD01': 'Graduate Center',
    'NCC01': 'Guttman CC',
    'HOS01': 'Hostos CC',
    'HTR01': 'Hunter College',
    'JJC01': 'John Jay College',
    'KCC01': 'Kingsborough CC',
    'LAG01': 'LaGuardia CC',
    'LEH01': 'Lehman College',
    'MHC01': 'Macaulay Honors College',
    'MEC01': 'Medgar Evers College',
    'NYT01': 'NYC College of Technology',
    'QNS01': 'Queens College',
    'QCC01': 'Queensborough CC',
    'SOJ01': 'School of Journalism',
    'SLU01': 'School of Labor&Urban Studies',
    'LAW01': 'School of Law',
    'MED01': 'School of Medicine',
    'SPS01': 'School of Professional Studies',
    'SPH01': 'School of Public Health',
    'UAPC1': 'University Processing Center',
    'YRK01': 'York College'
}

INSTANCE_ABS_PATH = "/home/fa18/313/adeh6562/public_html/grade-notifier/instances.txt"
INSTANCE_ABS_PATH_TEST = "/home/fa18/313/adeh6562/public_html/grade-notifier" \
    + "/test-instances.txt"
INSTANCE_ABS_PATH_DEV = "./instances.txt"
SCRIPT_PATH = "/home/fa18/313/adeh6562/public_html/grade-notifier/Grade-Notifier/src/core"
SCRIPT_PATH_DEV = "./src/core"
REPO_ABS_DIRECTORY_PATH = "/home/fa18/313/adeh6562/public_html/grade-notifier/Grade-Notifier"
ALREADY_IN_SESSION = "This username already has an instance running. " \
    + "You should recieve a text message when a grade changes. " \
    + "Please contact me @ Ehud.Adler62@qmail.cuny.edu if you have any futher questions"
SESSION_ENDED_TEXT = "Your session has ended. " \
    + "If you'd like to continue using Grade-Notifier please sign back in at "\
    + "https://venus.cs.qc.cuny.edu/~adeh6562/index.php"
LOG_PATH = "/home/fa18/313/adeh6562/public_html/grade-notifier/logs"
LOG_PATH_DEV = "./logs"


def abs_repo_path():
    return REPO_ABS_DIRECTORY_PATH

def is_local():
    return not ((socket.gethostname() == 'mars' or socket.gethostname() == 'venus'))

def log_path():
    if is_local():
        return LOG_PATH_DEV
    else:
        return LOG_PATH

def script_path():
    if is_local():
        return SCRIPT_PATH_DEV
    else:
        return SCRIPT_PATH

def instance_path(state=LoginState.DEV):
    if state == LoginState.PROD:
        return INSTANCE_ABS_PATH
    elif state == LoginState.TEST:
        return INSTANCE_ABS_PATH_TEST
    else:
        return INSTANCE_ABS_PATH_DEV
