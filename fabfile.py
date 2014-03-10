from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ["ubuntu@blog.samuelvime.com.br"]
env.key_filename = "/home/samuel/Dropbox/amazon/ssh/aws-samuelvime.pem"

def prepare_deploy():
    local("git add -A && git commit")
    local("git push")

def deploy():
    code_dir = "/var/www/samuelvimeblog"
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/milk-df/samuelvimeblog.git %s" % code_dir)
    with cd(code_dir):
        run("sudo git pull origin master")
        run("touch app.wsgi")