#!/bin/bash

cd /root/repo/games

echo "$(date)" >> quiz.py

git add -A && git commit -m "Added new line"

git push
