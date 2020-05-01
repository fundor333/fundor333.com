---
title: "Sock and socket"
date: 2020-04-15T00:00:00+00:00
feature_image: "/post/sock-and-socket/socket-adn-other-socket.jpg"
feature_link: "https://unsplash.com/photos/kBGVM2mVgcI"
feature_text: "Photo by Tai's Captures on Unsplash"
tags:
    - socket
    - python
slug: "sock-and-socket"
categories:
    - rant
description: "A little thing about socket in python"
---

Sometime the life has a distorted sens of humor and make a hole in your sock wen you are going to work.

It make feel you strange because you fell it and you only want to pull off both of them but Irony come in your live looking like a mail:

>Hello
>
>we need to connect to [last thing buy for the boss] system for [stuff i don't understand/like/want] reason so your team need to make a sock to talk with this system.
>
>Love
>
>[human(?) in my personal blacklist]

So I have a broken sock and I neet to make a socket.

## So how to make a socket?

In python all you need is in the core of the language. If you want to start you only need to import __socket__ and start coding.

After this we add some parameter like the __host__, the __port__ and the __size__ of the socket.

{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=1" >}}
import socket

HOST = "0.0.0.0"
PORT = 9000
SIZE =8192
{{< / highlight >}}

Now we need a socket object. Usualy i make it into custom object or function like this

{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=6" >}}
def server_program():
	server_socket = socket.socket()
	server_socket.bind((HOST, PORT))
	server_socket.listen(20)
{{< / highlight >}}

Where we 

* Start a socket with __socket.socket()__
* Set the socket to the Host and Port with __.bind((HOST, PORT))__
* Set the max connection with __.listen(20)__[^1]

After this you need to accept new incomming request. I also set a timeout because I don't want a connection unused on my socket.

{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=10" >}}
	while True:
		conn, address = server_socket.accept()
		conn.settimeout(60)
		data_raw = conn.recv(SIZE)
{{< / highlight >}}

We put into __data_raw__ the data from the connection (here we use size)[^2] and we have 2 more interesting object:

* __conn__ a socket with *this* connection 
* __address__ the *ip* for *this* connection


Now we have the data and we need to do something with this

{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=14" >}}
		# Sometimes you need this
		# data = data_raw.decode()
		do__somethings(adress,data_raw)
		conn.close()
{{< / highlight >}}

And after you do what you need to do close the connection.

This is a complete example of a working socket. If you need to response you can use *conn.send()* to send the data to the client.

If you need help or not understand something write me in the comment below or to my social.

This is the full code for __*Python3*__[^3]

{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=1" >}}
import socket

HOST = "0.0.0.0"
PORT = 9000
SIZE =8192

def server_program():
	server_socket = socket.socket()
	server_socket.bind((HOST, PORT))
	server_socket.listen(20)

	while True:
		conn, address = server_socket.accept()
		conn.settimeout(60)
		data_raw = conn.recv(SIZE)
		# Sometimes you need this
		# data = data_raw.decode()
		do__somethings(adress,data_raw)
		conn.close()

if __name__ == "__main__":
    server_program()
{{< / highlight >}}

[^1]: In this case we use localhost for the host, 9000 for the port and 20 for the max connection but you can change it for your need.
[^2]: Client and server must have the same size or bad this will be appening in your socket
[^3]: Tested from 3.5 to 3.8
