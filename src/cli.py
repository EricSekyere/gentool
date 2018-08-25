#!/usr/bin/env python

import click
import os
from src.scripts import unzip_folder, unzip_folders, log_num, move_files

@click.group()
def gtools():
    pass


@gtools.command()
@click.argument("sourcefolder", type = click.Path())
@click.argument("targetfolder", required=False, type = click.Path())
def moveall(sourcefolder, targetfolder=os.getcwd(), filters = "*"):
    click.echo("move all files")
    unzip_folder(sourcefolder, targetfolder)


@gtools.command()
@click.argument("sourcefolder", type=click.Path())
@click.argument("targetfolder", required=False, type=click.Path())
def move(sourcefolder, targetfolder=os.getcwd(), filters="*"):
    click.echo("move all files")
    unzip_folder(sourcefolder, targetfolder)


@gtools.command()
@click.argument("sourcefolder", type=click.Path())
@click.argument("targetfolder", required=False, type=click.Path())
def unzip( sourcefolder, targetfolder = os.getcwd()):
    click.echo("unzip a single folder")
    unzip_folder(sourcefolder, targetfolder)


@gtools.command()
@click.argument("sourcefolder", type=click.Path())
#@click.option("--kd", default = False)
def unzipall():
    click.echo("Unzip all zip folders")
    unzip_folders(os.getcwd())


@gtools.command()
@click.argument("lower_limit", nargs=1)
@click.argument("upper_limit", nargs=1, required=False)
def log(lower_limit, upper_limit):
    log_num(lower_limit, upper_limit)

if __name__ ==  "__main__":
    gtools()
