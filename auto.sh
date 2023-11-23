#!/bin/bash

cd /root/repo/games

echo "$(date)" >> quiz.py

git add -A && git commit -m "New line added"

git push
