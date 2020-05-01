---
title: "Dotfiles, bot and yaml files"
date: 2020-05-01T16:00:00+00:00
feature_image: "/post/dotfiles-bot-yaml/dotfiles-bot-yaml.jpg"
feature_image_name: "dotfiles-bot-yaml.jpg"
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

![Give me a big fat break](givemy.gif)

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

I re-read the wiki and I make the _meta_ files. The make file are the solution of my problem.

There are two plus one type of meta file:

-   **_meta/configs/_**: single script of config. You can set into this a single program or a "program" of config. In any case this is the "atomic config" of the bot: you can call it as an all not part of this
-   **_meta/profiles/_**: the profile of the machine. I use this for make distinction between _mac_, _linux_ or _windows_ but you can set for something like _work_ or _server_
-   **_meta/base.yaml_**: the base, allways called one. Here you set some default and the cleaner command

Whith this I need to change the install file and make some difference as show in the Wiki[^1]

{{< highlight bash >}}
#!/usr/bin/env bash

set -e

BASE_CONFIG="base"
CONFIG_SUFFIX=".yaml"

META_DIR="meta"
CONFIG_DIR="configs"
PROFILES_DIR="profiles"

DOTBOT_DIR=".dotbot"
DOTBOT_BIN="bin/dotbot"

BASE_DIR="$(cd "$(dirname "\${BASH_SOURCE[0]}")" && pwd)"

cd "${BASE_DIR}"
git -C "${META_DIR}/${DOTBOT_DIR}" submodule sync --quiet --recursive
git submodule update --init --recursive "${META_DIR}/\${DOTBOT_DIR}"

while IFS= read -r config; do
CONFIGS+=" ${config}"
done < "${META_DIR}/${PROFILES_DIR}/$1"

shift

echo \${CONFIGS}

for config in ${CONFIGS} ${@}; do
echo -e "\nConfigure $config"
	configFile="$(mktemp)" ; echo -e "$(<"${BASE_DIR}/${META_DIR}/${BASE_CONFIG}${CONFIG_SUFFIX}")\n$(<"${BASE_DIR}/${META_DIR}/${CONFIG_DIR}/${config}${CONFIG_SUFFIX}")" > "$configFile"
"${BASE_DIR}/${META_DIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASE_DIR}" -c "$configFile" ; rm -f "\$configFile"
done
{{< / highlight >}}

Make particolar attention of the begginning of the script because is were you can find the configuration for the script.

This new script can run with or without profile. And you can also add plugins in the command as the first install script.

## The config files

Now I need to write the config files and it is an easy task. All I need to do is to use this commands and their options:

-   **_link_**: make a _symbolically link_ of the file or directory from one of the file or one of the directory of the dotfiles' repo
-   **_create_**: make an empty directory
-   **_shell_**: execute command in shell in the base directory (that is specified when running the installer)
-   **_clean_**: remove all the dead symbolic links in the path
-   **_defaults_**: default option for all the command that follow
-   **_plugins commands_**: the command of the installed plugins

Now I need to write a **_meta/base.yaml_** file for the default command:

{{< highlight yaml "linenostart=1">}}
- defaults:
    link:
      create: true
      relink: true
      force: true

- link:
    ~/script:

- shell:
    - [git submodule update --init --recursive, Installing submodules]
    - [chmod +x ~/script/*]

- clean: ["~"]
{{< / highlight >}}

I start with the default option for the *link* command:

* __*create*__ for creating the parent directories as needed
* __*relink*__ removing the old symlink if present
* __*force*__ force the new link

This is default for my configs.

After this there is a *link* to make my default script directory linked in the home directory of the user.

Then we have the *shell* command with the command for import/download all the submodules of the project and the command for make executable the script folder.

And we end with the *clean* command with I clean the home from dead symbolic links and delete them all.

After this I need to make my fist profile, the *mac* one. So I make a new file __*make/profiles/mac*__

{{< highlight text >}}
git
programming
ssh
zsh
{{< / highlight >}}

Every one of this name is a yaml file in the __*makefile/configs*__ with the command to make/copy/something for the program/stuff is name of.
For example *git* is:

{{< highlight yaml >}}
- link:
          ~/.gitconfig:
          ~/.gitignore_global:
{{< / highlight >}}

In this yaml the bot links in the path __*~/.gitconfig*__ to the file __*gitconfig*__ and make the same with __*~/.gitignore_global*__.[^2]

In this way I can build multiple file for all the case I need. Some example is *ssh* or *zsh* or the *emacs* config in my [repo](https://github.com/fundor333/dotfiles) which use the configuration describe in this post. There are some files not used like a __*requirements.txt*__ or __*choco.ps1*__ that I don't know if it's a good idea. 

In any case if you write a good *dotfiles repo* with *dotbot* you need to keep the __*idempotency*__[^3] of the bot execution so you are __*mathematically*__ certan that the execution don't make different installation with the same command.

If you want to copy some part of my config you can do it but remember: 

>Dotfiles are supposed to contain your personal settings — what works for someone else isn’t necessarily optimal for you. If certain configurations worked for everybody, those settings would have been built into programs as defaults. Blindly cloning someone else’s dotfiles, especially without having an understanding of how everything works, is not the optimal approach.
>
>[Anish Athalye - Managing Your Dotfiles](https://www.anishathalye.com/2014/08/03/managing-your-dotfiles/)

[^1]: As describe in the wiki I rename the file as _install-profile_
[^2]: Be carefull, if you put a path after the *:* the bot use the path. If you don't the bot will search a file in the dotfile folder for the same path without the starting dot (if present)
[^3]: __*Idempotence*__: is the property of certain operations in mathematics and computer science whereby they can be applied multiple times without changing the result beyond the initial application (from [Wikipedia](https://en.wikipedia.org/wiki/Idempotence))
