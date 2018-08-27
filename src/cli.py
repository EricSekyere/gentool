#!/usr/bin/env python

import click
import os
from src.scripts import unzip_folder, unzip_folders, log_num, move_files, move_file

@click.group()
def gtools():
    pass


@gtools.command()
@click.argument("sourcefolder", type = click.Path())
@click.argument("targetfolder", required=False, type = click.Path())
@click.argument("filters", required=False)
def moveall(sourcefolder, targetfolder=os.getcwd(), filters = "*"):
    click.echo("move all files")
    move_files(sourcefolder, targetfolder, filters)


@gtools.command()
@click.argument("source", type=click.Path())
@click.argument("target", required=False, type=click.Path())
def move(source, target=os.getcwd()):
    click.echo("move file")
    move_file(source, target)


@gtools.command()
@click.argument("sourcefolder", type=click.Path())
@click.argument("targetfolder", required=False, type=click.Path())
def unzip( sourcefolder, targetfolder = os.getcwd()):
    click.echo("unzip a single folder")
    unzip_folder(sourcefolder, targetfolder)


@gtools.command()
@click.argument("source", type=click.Path())
@click.argument("target", type=click.Path())
def unzipall(source, target):
    click.echo("Unzip all zip folders")
    unzip_folders(source, target)


@gtools.command()
@click.argument("lower_limit", nargs=1)
@click.argument("upper_limit", nargs=1, required=False)
def log(lower_limit, upper_limit):
    log_num(lower_limit, upper_limit)

if __name__ ==  "__main__":
    gtools()