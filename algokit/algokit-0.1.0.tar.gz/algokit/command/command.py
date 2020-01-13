"""
some useful tool for command line
"""
import subprocess as sp


def exec(cmd):
    """
    execute a shell (or cmd) command
    :param cmd:  the command
    :return: (status, output) same as subprocess.getstatusoutput
    """
    return sp.getstatusoutput(cmd)


def exec_to_file(cmd, file_path):
    """
    execute a command and save the command output to a file
    :param cmd: the command
    :param file_path: the file path for saving the command output
    :return: return the file_path
    """
    with open(file_path, mode="w") as f:
        status, output = sp.getstatusoutput(cmd)
        print("cmd:{%s}, status: {%s}" % (cmd, str(status)))
        f.write(output)
    return file_path


def hive_to_file(sql, file_path):
    """
    execute a hive sql and save the result into a file
    the sql will be simply executed by hive cli in shell
    :param sql: the sql
    :param file_path: the path for saving
    :return: the file_path
    """
    sqltem = "set hive.cli.print.header=true; hive -S -e '{}'"
    cmd = sqltem.format(sql)
    exec_to_file(cmd, file_path)
    return file_path