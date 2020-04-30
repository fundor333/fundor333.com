---
title: "Dotfiles, bot and yaml files"
date: 2020-05-02T00:00:00+00:00
feature_image: "/images/post/dotfiles-bot-yaml/dotfiles-bot-yaml.jpg"
feature_link: "https://unsplash.com/photos/y7T1lYkfg0c"
feature_text: "Photo by Amith Nair on Unsplash"
tags:
    - bot
    - dotfiles
    - dotbot
slug: "dotfiles-bot-yaml"
categories:
    - dev
description: "Using the same dotfiles on multiple computer in the easy way"
---

If you ever use _Unix_ based system you are familiar with _dotfiles_ for configuration.
Any program has some of this file or folders laying arrount in your user root.

And many time it was a booring job to setup all your stuff before starting with all the work because I want the config to be the same every where I work.
So, in the end of the 2017 i find an article about dotfiles: [Managing your Dotfiles](https://www.anishathalye.com/2014/08/03/managing-your-dotfiles/).
With this article and some _copy-and-paste_ from other dotfiles repo's on Github I made [mine](https://github.com/fundor333/dotfiles).
This was in November 2017. Github suggest it was the 20 of Novembre the first version of the repo but I remember I was trying multiple idea of it and only later make a repo with clean code so It was sometime in November.

Now some time has pass and I have a **_BIG FAT PROBLEM_**. I need to have my _dotfiles_ synced and working on a _Linux Machine_ (Arch), an _Apple Machine_ and a _Windows Machine_... So not only I have multiple versions of configs but for multiple platform. And I need also some of this config on all my machine like the _ssh's config_.

So for some time I use a notebook (_a book where i write notes_ not a pc) where I log the change and this make some problems. A lots of problems.

![Give me a big fat break](/images/post/dotfiles-bot-yaml/givemy.gif)

So I search for a system for launch a command and update all and I find it: **_[dotbot](https://github.com/anishathalye/dotbot)_**.

# The bot

This is a project python where you can write an _install script_ from a template and write one or more _\_.conf.yaml_ with the instructions. And there are multiple plugin for some package manager (_pip, rust, apt, brew..._) which can be usefull.

The best way to use (and the only one) is to make the plugin repo into a submodule so it can be updated and will be always an unicum.

In my case I have a multiple config installer

{{< highlight bash >}}
#!/usr/bin/env bash

set -e

DEFAULT_CONFIG_PREFIX="default"
CONFIG_SUFFIX=".conf.yaml"
DOTBOT_DIR=".dotbot"

DOTBOT_BIN="bin/dotbot"
BASEDIR="$(cd "$(dirname "\${BASH_SOURCE[0]}")" && pwd)"

cd "${BASEDIR}"
git submodule update --init --recursive "${DOTBOT_DIR}"

for conf in ${DEFAULT_CONFIG_PREFIX} ${@}; do
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASEDIR}" --plugin-dir .dotbot-brew -c "${conf}${CONFIG_SUFFIX}"
done
{{< / highlight >}}

The only thing you need to pay attention is the _--plugin-dir <folder of the plugin>_ which can be use multiple times in the command, one for plugin you have. Also you can install a plugin as a submodule for the same reasons as the bot.

# My Idea

I have a install script which can execute one config all the time (the _default_ one) and any number of config as add for the default.

So I make multiple _setting.conf.yaml_ one for every configuration I have and i don't like it.
I have:

-   **_default.conf.yaml_**: ssh setting, git setting and some command for one or two folder
-   **_windows.conf.yaml_**: cmd aliases for my pleasure
-   **_mac.conf.yaml_**: zsh and some mac specific config
-   **_linux.conf.yaml_**: zsh and some linux specific config

Every time you run the command _./install_ the _default.conf.yaml_ run and, if you request multiple config, it run _default.cong.yaml_ plus every config you request. And all the configs files are into a folder, one for each and no way to make something similar to function or there is?

I need something more modular, where i can set the config for program/app/stuff in one file and "import" in a list-config, so I can call a list-config or a single/multiple program's configs.

In this way I don't have duplication of code or config long km and make multiple list-config more easy to read because they become easy to read.

# New Idea because I don' t like the first
