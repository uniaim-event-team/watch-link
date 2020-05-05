#!/usr/bin/env bash

export PYTHONPATH=/home/ec2-user/watch-link
cd /home/ec2-user/watch-link/alembic
alembic revision --autogenerate -m update
alembic upgrade head
