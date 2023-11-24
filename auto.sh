#!/bin/bash

cd /home/ubuntu/games

echo "$(date)" >> quiz.py

git add -A && git commit -m "New line added"

git push
