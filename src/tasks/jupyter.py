from invoke import task
import os, sys, re, time
import skp_env, skp_util

@task
def build(c):
    cmd = f'envsubst < {skp_env.JUPYTER_HOME}/service.yml | docker-compose -f - build'
    skp_util.run_with_exit(c, cmd)

@task
def start(c):
    cmd = f"envsubst < {skp_env.JUPYTER_HOME}/service.yml | docker-compose -f - up -d"
    skp_util.run_with_exit(c, cmd)


@task
def stop(c):
    cmd = f"envsubst < {skp_env.JUPYTER_HOME}/service.yml | docker-compose -f - down"
    skp_util.run_with_exit(c, cmd)

@task
def restart(c):
    stop(c)
    time.sleep(2)
    start(c)
