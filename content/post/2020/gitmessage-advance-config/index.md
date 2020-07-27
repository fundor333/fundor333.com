---
title: "Create a custon Git message with GitConfig"
date: 2020-08-15T15:15:00+02:00
feature_image: "gitmessage-advance-config.jpg"
feature_link: "https://unsplash.com/photos/xDjGxM8N4sY"
feature_text: "Photo by Victoria Zakharchuk on Unsplash"
tags:
- git
- config
- dotfiles
slug: "gitmessage-advance-config"
categories: 
- dev
- fingerfood
description: "Sometime you need to configure your git or have a template for the commit for your work"
---

Sometime you will need to have a template for the commit message.

Allwayse put something (ticket code, bug code, etc...), order of stuff, some command for the CI system, etc...

In Git you can set a a file as the template for the git commit. 
You can do it for a single project or for your user. 
In this case I will show the command for all your project.

First you need to write the file.
Usualy I make a file in the home ***~/.gitmessage*** where I put the message. 
For example a file template is:

{{< highlight bash >}}
# Title of the commit, 50 chars

# Body. What and Why, with Task Id/Bug Id, 72 chars
{{< / highlight >}}

Remember, if a row start with # the row is a comment.

After you make your own themplate you must tell git where is it so you need to launch this command:

{{< highlight bash >}}
 git config --global commit.template ~/.gitmessage
{{< / highlight >}}

After this git will use your new template for the commit.

Good work
