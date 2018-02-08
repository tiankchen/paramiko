import socket

import time

import paramiko
import threading


def test1():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='JD1', username='chenchen', password='password')
    client.invoke_shell()
    stdin, stdout, stderr = client.exec_command('su -')
    stdin.write("password\n")
    stdin.flush()
    data = stderr.read().splitlines()
    for line in data:
        if line:
            print(line)


test1()
#
#
#
#
# chan = None
#
#
# def continue_print():
#     d = chan.recv(1024).decode('utf-8')
#     while not len(d) == 0:
#         print(d, end=None)
#         print("length: {}".format(len(d)))
#         d = chan.recv(1024).decode('utf-8')
#
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('JD1', 22))
#
# t = paramiko.Transport(sock)
# t.connect(username='chenchen', password='password')
#
# chan = t.open_session()
# chan.get_pty()
# chan.invoke_shell()
# chan.settimeout(60)
#
# th = threading.Thread(target=continue_print)
# th.start()
#
# chan.send("ldde \n")
# chan.send("echo $? \n")
# chan.send("test \n")
# chan.send("echo $? \n")
# time.sleep(10)
#
# t.close()
# th.join()
