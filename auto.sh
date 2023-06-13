#!/bin/bash

echo `date +"%Y%m%d%H"` >> quiz.py

git add -A && git commit -m "Added new line"

git push
