---
title: "Advance Git Config and Ssh Config"
date: 2021-03-11T10:00:25+01:00
feature_image: "Advance-git-config-and-ssh-config.jpg"
feature_link: "https://unsplash.com/photos/9PRQ44avKik"
feature_text: "Photo by Tomáš Stanislavský on Unsplash"
tags: 
- dotfiles
- devops
slug: "Advance-git-config-and-ssh-config"
description: "My advance config for git e ssh"
type: "post"
---

Many and many times I update my dotfiles[^1] and rewrite part of them for keep my work config and personal config in a same repo with all the config split for usage.

So I discover that I can have multiple _ssh config_ and _gitconfig_ on the same machine.

##  Multiple SSH config files

The SSH's config file was too long to manage so one day I need to break it for make it easy for managing. 
So I implement one of the feature of the ssh config[^2]: the __include__ command.

### How is it work?

You write your normal config ssh for work or personal user. Something like this for the personal config

~~~ yaml
Host fundor333
	User root
	HostName fundor333.com
	IdentityFile ~/.ssh/keys/fundor333
	PreferredAuthentications publickey
~~~

After this you do all the same for yor work setting and rename all like _personal_config_ or _job_config_ and write an empty setting as _~/.ssh/config_.

So you have something like this

* ~/.ssh/config
* ~/.ssh/config-dir/personal_config
* ~/.ssh/config-dir/job_config

Where _config_ is empty. So I linking my _stuff_config_ in to the main config with the import like this:

~~~ bash
Include ~/.ssh/config-dir/personal_config
Include ~/.ssh/config-dir/job_config
~~~

In this way I can have sorted in a better way all my ssh config.

## Multiple config for git

In reality I don't need two gitconfig. I need two identity with git, one with some project one with others projects.
Like ssh i need to use 2 account, one for work one for personal user.

In my case my repo structure is looking like this:

* ~/Coding
* ~/Coding/Personal
* ~/Coding/Job

So I need to have three git identities:

* A generic one for the default
* A personal git identity for my personal project
* A "job" git identity for my job project

### How to do it

You need to write the _.gitconfig_ and one file for every identities after the default one (so in this example three file, the _gitconfig_, the _job_config_ and the _personal_config_).

So if you follow my example you have this
 
* ~/.gitconfig
* ~/.git-identities/job
* ~/.git-identities/personal

where you need a default user for the _.gitconfig_ linke this

~~~ yaml
[user]
email = git@fundor333.com
name = Fundor333
~~~

and add the regex for the path of the directory of the projects with the path for the config like this:

~~~ yaml
[includeIf "gitdir:~/Github/**"]
path = ~/.git-identities/gitconfig-fundor333

[includeIf "gitdir:~/Coding/**"]
path = ~/.git-identities/gitconfig-fundor333

[includeIf "gitdir:~/Coding/Personale/**"]
path = ~/.git-identities/gitconfig-fundor333

[includeIf "gitdir:~/Coding/job/**"]
path = ~/.git-identities/gitconfig-job
~~~

If you put in the config define in the path the gitconfig you need you will override for the target project/s like for the _gitconfig-job_

~~~yaml
[user]
email = job@fundor333.com
name = Fundor333's Job account
~~~

This is a example for the _user_ config but you can override all the config for the project like _alias_ or the rule _core_ for the commit and style of them.

[^1]:[Dotfiles, bot and yaml files]({{< relref "post/2020/dotfiles-bot-yaml/index.md" >}})
[^2]: This examples need OpenSSH 7.3 or newer for work
