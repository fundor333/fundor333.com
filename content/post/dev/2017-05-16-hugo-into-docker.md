Date: 2017-05-16T12:27:11+02:00
Tags: docker, hugo, image, container
Title: Hugo into Docker
Summary: This blog is publish with a docker image with GitLab. But I don't like the image I was using because wasn't update and it's big and havy. So I fork the project for create an update version for my personal blog.

This blog is publish with a docker image with GitLab. But I don't like the image I was using because wasn't update and it's big and havy. So I fork the project for create an update version for my personal blog.

<!--more-->

![docker logo]({filename}/images/post/docker/docker.png)


So I started with updating the old docker image I was using this image

	#!docker
	FROM debian:wheezy
	MAINTAINER yigal@publysher.nl

	# Install pygments (for syntax highlighting)
	RUN apt-get -qq update \
	&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-recommends python-pygments git ca-certificates \
		&& rm -rf /var/lib/apt/lists/*

	# Download and install hugo
	ENV HUGO_VERSION 0.20.6
	ENV HUGO_BINARY hugo_${HUGO_VERSION}-64bit.deb

	ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} /tmp/hugo.deb
	RUN dpkg -i /tmp/hugo.deb \
		&& rm /tmp/hugo.deb

	# Create working directory
	RUN mkdir /usr/share/blog
	WORKDIR /usr/share/blog

	# Expose default hugo port
	EXPOSE 1313

	# Automatically build site
	ONBUILD ADD site/ /usr/share/blog
	ONBUILD RUN hugo -d /usr/share/nginx/html/

	# By default, serve site
	ENV HUGO_BASE_URL http://localhost:1313
	CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0


So I build an image of this container and it was 171 MB in my machine.

But I can do better than this because i can use _*alpine*_ in the place of _*debian:wheezy*_.

I do this because the image for _*debian*_ is bigger than the image for _*alpine*_. But if I will use _*alpine*_ I need to change somethings because I can't install _*.deb*_ into the image. So i use the binary of Hugo for Linux find on Github. And install it on the image

	#!docker
	FROM alpine
	LABEL maintainer "fundor333@gmail.com"

	# Download and install hugo
	ENV HUGO_VERSION 0.20.6
	ENV HUGO_DIRECTORY hugo_${HUGO_VERSION}_Linux-64bit
	ENV HUGO_BINARY ${HUGO_DIRECTORY}.tar.gz

	# Install HUGO
	RUN set -x
	RUN apk add --update wget ca-certificates
	RUN wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
	RUN tar xzf ${HUGO_BINARY}
	RUN rm -r ${HUGO_BINARY}
	RUN mv hugo /usr/bin/hugo
	RUN rm -r LICENSE.md
	RUN rm -r README.md
	RUN apk del wget ca-certificates
	RUN rm /var/cache/apk/*

	# Create working directory
	RUN mkdir /usr/share/blog
	WORKDIR /usr/share/blog

	# Expose default hugo port
	EXPOSE 1313

	# Automatically build site
	ONBUILD ADD site/ /usr/share/blog
	ONBUILD RUN hugo -d /usr/share/nginx/html/

	# By default, serve site
	ENV HUGO_BASE_URL http://localhost:1313
	CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0

This time the size was 33,5 MB. Good but i can do BETTER.

Whenever you wrote a new line with _*RUN*_ you make the "compiled" into another _*layer*_ so, if you have 22 command (like me) you have 22 layer for the image

	#!docker
	FROM alpine
	LABEL maintainer "fundor333@gmail.com"

	# Download and install hugo
	ENV HUGO_VERSION 0.20.6
	ENV HUGO_DIRECTORY hugo_${HUGO_VERSION}_Linux-64bit
	ENV HUGO_BINARY ${HUGO_DIRECTORY}.tar.gz

	# Install HUGO
	RUN set -x && \
	apk add --update wget ca-certificates && \
	wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} && \
	tar xzf ${HUGO_BINARY} && \
	rm -r ${HUGO_BINARY} && \
	mv hugo /usr/bin/hugo && \
	rm -r LICENSE.md && \
	rm -r README.md && \
	apk del wget ca-certificates && \
	rm /var/cache/apk/*

	# Create working directory
	RUN mkdir /usr/share/blog
	WORKDIR /usr/share/blog

	# Expose default hugo port
	EXPOSE 1313

	# Automatically build site
	ONBUILD ADD site/ /usr/share/blog
	ONBUILD RUN hugo -d /usr/share/nginx/html/

	# By default, serve site
	ENV HUGO_BASE_URL http://localhost:1313
	CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0

Size 3,99 MB in this case.

The maggior part of the total size is caused by the size of the _*Hugo*_ binary itself so I cann't make an image _*lighter*_ than the binary.

Now the image size and number layers can change update after update so I put this image with the allwayes data about the images.

[![hugo_fundor333](https://images.microbadger.com/badges/image/fundor333/hugo.svg)](https://microbadger.com/images/fundor333/hugo "Get your own image badge on microbadger.com")
