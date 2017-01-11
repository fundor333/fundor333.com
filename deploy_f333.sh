#!/usr/bin/env bash

pelican content -s publishconf.py
ghp-import output -b master
git push origin master