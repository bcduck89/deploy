'''
Apache(or NGINX) 서버 (웹서버)가 가장 먼저 찾는 파일
wsgi기능은 서버기능을 제공하는 역할
'''

import sys, os

cur_dir = os.getcwd()

# 웹은, 접속로그, 에러로그 존재
sys.stdout = sys.stderr
sys.path.insert(0, cur_dir)

from run import app as application