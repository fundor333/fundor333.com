---
title: "Manage Site and Certificate"
date: 2020-10-01T22:12:20+02:00
feature_image: "manage-site-and-certificate.jpg"
feature_link: "https://unsplash.com/photos/x0t6DiAg118"
feature_text: "Photo by Mike Kenneally on Unsplash"
tags:
- devops
- bot
slug: "manage-site-and-certificate"
categories: 
- dev
description: "One dev manage 40 sites' domains, SSL and check all of them with a package"
type: "post"
---

After my [other post]({{< relref "post/2020/ssl-check-with-a-script/index.md" >}}) I find we (me and my coworker) need to check between 30 to 40 domain, subdomain and SSL certificate for work and some more for our private life so I put on the test my [other post's script]({{< relref "post/2020/ssl-check-with-a-script/index.md" >}}) but we need to check more. 

We need to check when the domain expire (DNS Lookup), we need to check if the server are up and the SSL certificate. This is a problem because we need to launch the same commands every day for multiple server every day and some time we forgot a domain or a url and we don't check it for days. 
