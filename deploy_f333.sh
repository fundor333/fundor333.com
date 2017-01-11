#!/usr/bin/env bash

git branch gh-pages
ghp-import output
git checkout master
git merge gh-pages
git push --all