##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## Config object
##

import os

TESTING         = False
DATABASE_HOST   = "db"
DATABASE_NAME   = os.getenv('MYSQL_DATABASE')
DATABASE_USER   = os.getenv('MYSQL_USER')
DATABASE_PASS   = os.getenv('MYSQL_PASSWORD')