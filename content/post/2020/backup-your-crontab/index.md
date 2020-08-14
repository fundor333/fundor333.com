---
title: "Backup Your Crontab"
date: 2020-08-15T13:49:30+02:00
feature_image: "backup-your-crontab.jpg"
feature_link: "https://unsplash.com/photos/eMzR8FW4N9M"
feature_text: "Photo by Jonathan Pielmayer on Unsplash"
tags:
- dotfiles
- coding
slug: "backup-your-crontab"
categories: dev
description: "Using DotBot for backup and sync crontab job"
type: "post"
---

With covid I work sometime at home, sometime at office, allwayse with different computer.

This is one of the reason of my [dotfile]( {{< ref "post/2020/dotfiles-bot-yaml/index" >}}) and, for some project I am working on, I need to have some cronjob in every computer but some cronjob is machine specific so I don't need to sync all, only some.

So I contact the developer of DotBot[^1] and talk about it but it wasn' t implemented so I make a plugin for this.

## The plugin

Definition of needs:

* Sync cronjob
* Delete/update cronjob
* Work only on the user's cronjob
* Only the bot' cronjobs will be edited, not the others
* Work with __Crontab__, I'm not interested in others cronjobs' apps

So I use the command of crontab and make it works

## How to use it

Like every plugin for [dotbot](https://github.com/anishathalye/dotbot) you need to clone the [plugin's repo](https://github.com/fundor333/crontab-dotbot) and add it to the script.[^2]

After installation you can use the directive _crontab_ for adding job to your crontab.
In this way you can write multiple config for multiple type of intallations you have.

The direction will look like this

``` yaml
- crontab
	-cron: 0 * * * *
	 command: echo "Hello world"
```

For now this is a little thing working only on _Crontab_ but I am thinking about adding Windows support but I don't have any idea about how I make it, so if you have idea about Windows implementation comment in this post or open an issiue or a pull request on the repo

[^1]: The bot who manage my _.dotfiles_ and other configs
[^2]: The repo of the plugin has all the instruction about the installation
