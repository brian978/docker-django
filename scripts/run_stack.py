import os
import subprocess

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

command = "docker-compose -f {docker_compose_file} up -d"
command = command.format(docker_compose_file=parent_dir + "/docker-compose.yml")

subprocess.call(command, shell=True)
