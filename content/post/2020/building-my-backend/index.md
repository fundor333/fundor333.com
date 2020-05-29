---
title: "Building My Backend"
date: 2020-06-26T09:44:10+02:00
feature_image: "building-my-backend.jpg"
feature_link: "https://unsplash.com/photos/fpmV3dQPUvU"
feature_text: "Photo by Caleb Woods on Unsplash"
tags:
    - django
    - backend
    - automatism
slug: "building-my-backend"
categories: 
    - dev
description: "Why someone need a server and how I build mine"
---

More time pass more time I need a server for my cronjob and other process. 
Sometime the cron was a supid thing, working only for the short period and after can be trashed but the real problem start with Feedly, the subscription for feed I use.

One day, adding a new feed to my Feedly account, I discovered that I can't add more in the free subscription. 
So I start thinking some alternative.

## What I need

* __web app__ i need to use on the run, not only in my machine but in other as well.
* __auto update__ I need to find the newer or the newest post from my feed
* __feed from wep page__ I need to have the feed from an url not only from the feed url
* __mark read and not read__ because I need to read only the new stuff and not only the old one
* __some endpoint for personal use__ I need some endpoint api rest for another project of mine

So I need:

* __a web server__ for serving pages -> Nginx
* __a task manager__ for have a heap for work which the server do in the free time -> Redis
* __a database for the data__ where I put my data -> PostgreSql
* __a server framework__ for writing my server-app -> Django

Whith this stack I start my backend.

## Fist problem: feeds

First I need to have an alternative to __Feedly__ so I start building my personal feed manager.
And I discovered there are multiple type of feed: atoms, rss 1.0, rss 2.0, etc... So I "read" some of my feed manualy and start writing some generic reader for the rss and atom (the most popular format of the feed formats) and write some code for reading Xml in this two type.

After this I write a Django model for the post inside the feeds so I can save it without thinking about the feed format but reading it, share it or deleting it.

In this way I discover some dead blog and other formats of feed (old one from some old site but still very active).

After this I builds the task for the cronjob for getting all the feed of the multiple sources. This task add a command into redis and when the wrapper (celery in my case) can do the job, it does it and log into the database a row with the log in case of failure.

I did the same also for the "mark as read" task so if I mark one this is a task done by the browser but if I do for the "last month" or "all" posts they make a Celery task into Redis because it can be a lot of work for the server because I can do more thinks with this but not now. 

In the future I am thinking about point system for the post and other thinks that need a after processing for making a "prefernce system" or other similar thinks for my personal use[^1] and I want to save the top post into my Poket account or save it in a way I can store for personal reference with or without the site working and store it indefenitly.

## Second problem: gui

After working all the feed part I build a little gui, inspired by the teming of my blog and I love it. 


[^1]: This is an idea I copy from Feedly Premium. 
