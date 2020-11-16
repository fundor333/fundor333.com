---
title: "Keep update Gitlab"
date: 2020-11-16T20:30:00+01:00
feature_image: "Keep_update_Gitlab.jpg"
feature_link: "https://unsplash.com/photos/8rTwokBwz1w"
feature_text: "Photo by hue12 photography on Unsplash"
tags:
- devops
- hacking
slug: "Keep_update_Gitlab"
categories: post
description: "How to check if your GitLab is update automaticaly"
type: "post"
---

Some time ago I had a problem with a selfhosted Gitlab instances. I had a new user, johnyj12345, which create a repo and an issiue and log off.
This is an attack made to my instance because I don't upgraded it for some time so I cleanit and remove all the trace of this user and update all.[^1]

After this I was ready to tacle the elephant in the room: how to check if my self hosted GitLab.

## How to check if GitLab is updated

Official documentation of GitLab[^2] say that the __/help__ page where there is, if logged, a label with

* __Up to date__
* __new version out__
* __update asap__

And with it decide what you need to do.

So I decide to hack the system and make an allert for me.

## Hack the GitLab help page

First ve need to understand how the label work.
A rapid ispection of the page show that the label is a responde of a _get_ at the url *https://version.gitlab.com/check.svg* with some parameters.

In particolar we need the GitLab version installed. So we need it too. And for them we need the token from the self hosted installation[^3]. 

### Get the version of GitLab
For this project we only need python and [_requests_](https://pypi.org/project/requests/)

``` python
def get_gitlab_version():
	url = BASE_GITLAB_URL + "/api/v4/version"
    headers = {"Private-Token": GITLAB_PERSONAL_TOKEN}
    req = requests.get(url, headers=headers)
    return req.json()
```

and this return a json like this as python dict

``` json
{
  "version": "8.13.0-pre",
  "revision": "4e963fe"
}
```

From this json we know the _version_ of GitLab for the next step.

### Get the label of the Help GitLab page

``` python
def last_version_gitlab():
	response = get_gitlab_version()
    url = BASE_GITLAB_URL
    ver = response["version"]
    gfg = urlsafe_b64encode(str.encode('{"version":"' + str(ver) + '"}'))
    logger.debug(gfg)
    r = requests.get(url="https://version.gitlab.com/check.svg", params={'gitlab_info': gfg}, headers={'Referer': url})
	return r.text
```

In this way you return a string with the label as xml img. 
So if you want a feedback when is to update it you can do this.

``` python
def gitlab_check():
	return "up-to-date" in last_version_gitlab()
```

In this way you return _False_ if you need to update, _True_ elsewhere.

## Conclusion

Whith this you can make another function for sending a notification or a mail for the update. 
I make all this code into a cronjob with mail sender for getting at the start of my work hours a mail for unupdated gitlab installation.
I also suggest Slack or Telegram for the notification for the unupgraded GitLab.

[^1]: [Link](https://www.netways.de/blog/2020/07/14/gitlab-johnyj12345-hack/) of a guide for clean. Update following the guide of GitLab.
[^2]: [Official documentation Version Check](https://about.gitlab.com/blog/2015/05/07/version-check/)
[^3]: [Official documentation Acess Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
