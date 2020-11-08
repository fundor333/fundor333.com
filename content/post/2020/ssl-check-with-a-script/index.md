---
title: "SSL Check With a Script"
date: 2020-08-20T14:13:40+02:00
feature_image: "ssl-check-with-a-script.jpg"
feature_link: "https://unsplash.com/photos/OVEWbIgffDk"
feature_text: "Photo by Denisse Leon on Unsplash"
tags:
- coding
- devops
slug: "ssl-check-with-a-script"
categories: 
description: "You need to check a lot of SSL certificate, some domain and others things"
type: "post"
---

As a backend developer I made a lot of web application, site and other stuffs which have one or more domains. Because I don't have money I use [Let's Encrypt](https://letsencrypt.org/) for make the SSL certificate for the HTTPS and, because it is free, it is only 3 month worty certificate so you need to renovate it.

Every sistem I have use CertBot, the bot for Let's Encrypt, who renew the certificate when needed with a cronjob. Sometime you will recive a mail from Let's Encrypt about some ending certificate and I don't want to check manualy every time because some of our certificate are for multiple domain in one certificate.

## Script out the problem

For this script we need 

* Python 3.6 or more
* PyOpenssl

I don't want to use module outside the python core but, in this case, I need a module for the newest type of certificate so... I write it with a config file with all my site.

``` python
#!/usr/bin/env python3

import datetime
import logging
import os
import socket
import ssl

import OpenSSL

logger = logging.getLogger("SSLVerify")
```

Start with the import for working with date, log, make a request for a ssl certificate and open a file. Also set the logger for the script.


``` python {linenostart=14}
def ssl_expiry_datetime(hostname: str) -> datetime.datetime:
  cert = ssl.get_server_certificate((hostname, 443))
  x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
  return datetime.datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
```

This function get a url, get the certificate of the domain and return a datetime python object listing the last minute the certificate validity. After this the site is not _https_

``` python {linenostart=20}
def ssl_valid_time_remaining(hostname: str) -> datetime.timedelta:
  expires = ssl_expiry_datetime(hostname)
  logger.debug("SSL cert for {} expires at {}".format(hostname, expires.isoformat()))
  return expires - datetime.datetime.utcnow()
```

Return a python object with the remaining days of the certificate. It can be negative if is exspired.

``` python {linenostart=27}

def test_host(hostname: str, buffer_days: int = 30) -> str:
  try:
    will_expire_in = ssl_valid_time_remaining(hostname)
  except ValueError as e:
    return "❌ " + hostname + " cert error " + str(e)
  except socket.timeout as e:
    return "❌ " + hostname + " could not connect"
  else:
    if will_expire_in < datetime.timedelta(days=0):
      return "❌ " + hostname + " cert will expired"
    elif will_expire_in < datetime.timedelta(days=buffer_days):
      return "⏳ " + hostname + " cert will expire in " + will_expire_in
    else:
      return "✔️ " + hostname + " cert is fine"
```

This function build the string for the user to see about the domain. Use the _emoji_ for fast reading for error[^1]


``` python {linenostart=44}
def popupmsg(msg):
  logger.info(msg)
```

Print into the console the output. I search a good way for making a popup or a toast for gui purpuise but I can't make it multiOS so I use the standard output

```python {linenostart=48}
if __name__ == "__main__":
  f = open(os.path.expanduser("~/.sslverify"), "r")
  end_message = ""
  for host in f.readlines():
    host = host.strip()
    message = test_host(host)
    end_message += "\n" + message
  print(end_message)
  popupmsg(end_message)

```

The starter of the all script. The input of the script is a [dotfiles]({{< ref "post/2020/dotfiles-bot-yaml/index" >}}), a _.txt_ with one site for row,
In this way I backup it with my  [dotbot](https://github.com/anishathalye/dotbot) and take with me into every machine I work in.

Changing the output system you can easly make a cronjob out of this script or a lambda function for your need.

I am thinking about making this script into a module or bash app in the near future.

## All the code

We end with all the code into a single block

``` python
#!/usr/bin/env python3

import datetime
import logging
import os
import socket
import ssl

import OpenSSL

logger = logging.getLogger("SSLVerify")


def ssl_expiry_datetime(hostname: str) -> datetime.datetime:
  cert = ssl.get_server_certificate((hostname, 443))
  x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
  return datetime.datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')


def ssl_valid_time_remaining(hostname: str) -> datetime.timedelta:
  expires = ssl_expiry_datetime(hostname)
  logger.debug("SSL cert for {} expires at {}".format(hostname, expires.isoformat()))
  return expires - datetime.datetime.utcnow()


def test_host(hostname: str, buffer_days: int = 30) -> str:
  try:
    will_expire_in = ssl_valid_time_remaining(hostname)
  except ValueError as e:
    return "❌ " + hostname + " cert error " + str(e)
  except socket.timeout as e:
    return "❌ " + hostname + " could not connect"
  else:
    if will_expire_in < datetime.timedelta(days=0):
      return "❌ " + hostname + " cert will expired"
    elif will_expire_in < datetime.timedelta(days=buffer_days):
      return "⏳ " + hostname + " cert will expire in " + will_expire_in
    else:
      return "✔️ " + hostname + " cert is fine"


def popupmsg(msg):
  logger.info(msg)


if __name__ == "__main__":
  f = open(os.path.expanduser("~/.sslverify"), "r")
  end_message = ""
  for host in f.readlines():
    host = host.strip()
    message = test_host(host)
    end_message += "\n" + message
  print(end_message)
  popupmsg(end_message)

```

[^1]: The "error" in this case are the only one colored emoji of the bunch.
