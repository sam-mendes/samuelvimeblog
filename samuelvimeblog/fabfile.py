from fabric.api import local

def prepare_deploy():
    local("git add -A && git commit")
    local("git push")

def deploy():
    code_dir = '/home/samuel/Python/workspace'