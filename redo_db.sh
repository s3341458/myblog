#!/bin/bash

dropdb blog
createdb blog
python init_db.py
