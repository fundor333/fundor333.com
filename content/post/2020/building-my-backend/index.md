---
title: "Building My Backend"
date: 2020-06-26T09:44:10+02:00
feature_image: "building-my-backend.jpg"
feature_link: "https://unsplash.com/photos/fpmV3dQPUvU"
feature_text: "Photo by Caleb Woods on Unsplash"
tags:
    - django
    - coding
    - api
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

After working all the feed part I build a little gui, inspired by the teming of my blog and I love it. Light background, dark text with the same font and some similarity but also some difference, because I think that mine blog theme is not right for a backend or other type of web app other than blogs.

The problem come from the menu. I don like the menu with submenu so I write a "menu dashboard" for all the "categories" of view I made for my backend but I am not done for it. I need something more "mine" for the navigation inside them. And I need to add some Javascript for adding some gui impovment (color or highlight where needed) and this was a big problem for me.

I am not fluent in js so I need to *Google* a lot of things about *jquery* and *EMACS5* and *"vanilla' JavaScript*.

After all and with some trick learn in *StackOverflow* or some random *blog* I have a functional and someway good looking theme for my backend.

## Third act: Api

Now is time for my favorite part: only backend!

I have some project to migrate into this backend and half of them has some sort of need of endpoint api so I move the first api project into my backend. With some work and some help from the *[Django Rest Framework](https://www.django-rest-framework.org/)* I build some view for outputting the json needed for the other project to work.

After this I build the guis for manage the data of the api. I know that all of this can be done with the *Django Admin* but I don't like it so I need to write the input, edit and view pages for them.

For now I consider this part compleate but, in time, I will porting all my other api into this backend.

## The Fourth is with you

Now I work on the landing of mine backend. I feel it empty so I think about what I can do to fill it.

And for this reason I write client for some weather api and other similar api of my home city for my personal easy access. So, with an little time I write all the backend for the 'widgets' I want and make all into a ClassView Django putting all the info into the context of the view.

With a lot of testing with the layout and changing all the widgets more and more time I ending to make a dashboard with very simple widget for all of theme.

For now it works but if I add another widget I need to redo all the Dashboard but for now I don't have need for another widget.

## Going for Five

After the gui I completely forgot how I write the Api so I need to have an autogenerated Api's documentation. So I use the autogenerating documentation of the *DRF*[^2] and build a Swagger view for my persona use. I subclassed the generator for adding more function on the standard *DRF* implementation of the api like the tag sistem and the server tags for an eventualy testing server (maybe one day with more money...).

## And now the conclusion

With some time I build more function into this system and add more api. For the time coming I am thinking to porting some cronjob into this backend, adding a documentation system for having some tutorial I can't put in the blog or there are no reason to make them public, like some personal stuff and I want to put a system to write my work task and write the time I am working on them for build in a easy way my timetable for work.

Because all the project I am working on I don't have a lot of time so all this project have the least priority of all but, one day after the other I will be updating all of this project with all the function I need but for now I have this.

[^1]: This is an idea I copy from Feedly Premium. 
[^2]: The *DRF* is the *[Django Rest Framework](https://www.django-rest-framework.org/)* 
