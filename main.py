#!/usr/bin/env python3

import argparse
import paramiko

def arg_parser():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", "-u", dest="USERNAME", required=True, help="Username of target")
    parser.add_argument("--host", required=True, dest="HOSTNAME", help="Target hostname or IP address")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keyfile", "-k")
    group.add_argument("--password")
    parser.add_argument("--port", "-p", required=False, dest="port", default=22)
    parser.add_argument("COMMAND", help="Command to run")
    args = parser.parse_args()

if __name__ == '__main__':
    arg_parser()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(args.HOSTNAME, port=args.port, username=args.USERNAME, password=args.password, key_filename=args.keyfile)

    stdin, stdout, stderr = ssh.exec_command(args.COMMAND)
    lines = stdout.readlines()
    print(lines)
