#!/usr/bin/env python3
"""This script runs an arbitrary command on an arbitrary host"""

import argparse
import paramiko


def arg_parser():
    """This function parses command line arguments"""
    global ARGS
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--user", "-u", dest="USERNAME", required=True, help="Username of target"
    )
    parser.add_argument(
        "--host", required=True, dest="HOSTNAME", help="Target hostname or IP address"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keyfile", "-k")
    group.add_argument("--password")
    parser.add_argument("--port", "-p", required=False, dest="port", default=22)
    parser.add_argument("COMMAND", help="Command to run")
    ARGS = parser.parse_args()


if __name__ == "__main__":
    arg_parser()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        ARGS.HOSTNAME,
        port=ARGS.port,
        username=ARGS.USERNAME,
        password=ARGS.password,
        key_filename=ARGS.keyfile,
    )

    stdin, stdout, stderr = ssh.exec_command(ARGS.COMMAND)
    lines = stdout.readlines()
    print(lines)
