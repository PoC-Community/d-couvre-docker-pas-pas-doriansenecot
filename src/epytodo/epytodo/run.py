#!/usr/bin/env python3

from app import app
from session import *

init_global()
session = -1
app.secret_key = 'ZnG]4np}J/KKdJ<A,8u7<aY?vsumM1=D@5bY??oN$B*949NTGnmZ3`w9UI{]c'
app.run(host="0.0.0.0", port=5000)

# 0.0.0.0 pour être accessible en dehors du container
