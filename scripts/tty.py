import os
import subprocess

app_root_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../").split("/")[-1]
app_dir_name = app_root_path.split("/")[-1]

command = "docker exec -it {app_name}_python_1"
command = command.format(app_name=app_dir_name)

subprocess.call(command, shell=True)
