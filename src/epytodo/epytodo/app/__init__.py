##
## EPITECH PROJECT, 2019
## Untitled (Workspace)
## File description:
## __init__
##

#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')

from app import controller
from app import views
