---
title: "Manage Site and Certificate"
date: 2020-10-01T22:12:20+02:00
feature_image: "manage-site-and-certificate.jpg"
feature_link: "https://unsplash.com/photos/x0t6DiAg118"
feature_text: "Photo by Mike Kenneally on Unsplash"
tags:
- devops
- bot
- dotfiles
slug: "manage-site-and-certificate"
categories: 
- dev
description: "One dev manage 40 sites' domains, SSL and check all of them with a package"
type: "post"
---

After my [other post]({{< relref "post/2020/ssl-check-with-a-script/index.md" >}}) I find we (me and my coworker) need to check between 30 to 40 domain, subdomain and SSL certificate for work and some more for our private life so I put on the test my [other post's script]({{< relref "post/2020/ssl-check-with-a-script/index.md" >}}) but we need to check more. 

We need to check when the domain expire (DNS Lookup), we need to check if the server are up and the SSL certificate. This is a problem because we need to launch the same commands every day for multiple server every day and some time we forgot a domain or a url and we don't check it for days. And if something boom we need to fix it with *zero down time* so we need to do some sysadmin work.

![Sysadmin Devotion](https://imgs.xkcd.com/comics/devotion_to_duty.png)

So, for our task, we need :

* Add a list of url save somewhere. Some have only the domain, some have subdomain and some don't have the protocol at the start[^1]
* Check for all SSL certificate for the saved urls
* Check for the expiration date of the domains
* Plugin or script support for custom things to check

So I write a tool for check all the point: [Server Grimoire](https://github.com/fundor333/servergrimoire)

## How to work?

It is a terminal app, so work all into your console. All the configs and the data are into two *dotfiles*, one called *.servergrimoire_config* and *.servergrimoire_data* (config and data respectively) and can be backup like all [dotfiles](/tags/dotfiles/).

So for start I need to register some urls like google and amazon for example

``` bash
 servergrimoire add --u google.com --u amamzon.it
```

Now you only register the url, nothing is check for now.

For run all job or only one you need to use the *run* directive with the *--c* flag for adding command. 

```bash
 servergrimoire run
```

After this you don't have any return beause this command is for cronjob or similar. If you launch a run and you want to see what appen you need to add *--stats* for gettin an output.

If you need to see what was the last run you can call *stats* and *info* if you want to see what is save into the data file. This way make easy for cronjob, automatic task and will grow with other function. All the command are in the *help* directive if you need more info.

This is a little module but can be extrime usefull in small list of urls but you need other tool if you use it for hundreds urls. 
I also accept help for the plugin.


[^1]: Sometime they don't have the *https* or the *http* prefix
