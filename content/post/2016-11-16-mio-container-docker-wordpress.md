---
title: Il mio container Docker Wordpress
date: 2016-11-16 00:00:00 +0000
slug: mio-container-docker-wordpress
tags:
- docker
- wordpress
- container
categories:
- dev
aliases:
- "/dev/mio-container-docker-wordpress"
description: Docker implementa un server locale per sviluppare temi e plugin Wordpress

---
Questo è un progetto nato da una mia necessità: avere wordpress
installato senza avere tutti i file in */var/www* o simili ma nella
cartella corrispondenza al progetto. Questo perchè mi è capitato e mi
sta capitando di dover sviluppare più di un ~~sito internet~~ tema
wordpress in contemporanea. Questo mi ha portato a sviluppare un
container docker wordpress.

<!--more-->

[![wordpress\_docker](/images/post/docker/docker.png)](https://github.com/fundor333/Wordpress-Docker)

Per chi non sa cos'è Docker rimando a un mio articolo
[qui](http://www.fundor333.com/docker-la-balena-con-i-container/), per
tutti gli altri continuo con la spiegazione del contenuto del repository
del progetto.

Il [repository](https://github.com/fundor333/Wordpress-Docker) contiene
un file *.gitignore* e un file *run.sh* che permette di lanciare i
docker in modo automatico (non ricordo mai i comandi per lanciare il
docker) che servono al progetto ma non sono la componente principale.

Il file veramente importante è il *docker-compose.yml* che serve a
descrivere come sono configurati i *container* che andremo ad utilizzare
e come interagiscono tra di loro.

Iniziamo quindi da quello che concettualmente è il primo container:

  {{< highlight Docker >}}
  mysql:
	  image: mysql:latest
	  volumes:
		- "./.data/db:/var/lib/mysql"
	  environment:
		  MYSQL_ROOT_PASSWORD: secret
		  MYSQL_DATABASE: project
		  MYSQL_USER: project
		  MYSQL_PASSWORD: project
  {{< / highlight >}}

    in cui

-   *image* definisce da quale immagine prende la base
-   *volumes* definisce dove vengono salvati i dati (altrimenti tra un
    avvio di docker e l'altro perdi i dati)
-   *environment* definisce tutte le variabili d'ambiente, che in questo
    caso sono i dati di configurazione del database

Il secono container *wordpress* contiene, invece, server e installazione
di Wordpress.

	{{< highlight Docker  >}}
    wordpress:
      image: wordpress
      ports:
        - 8080:80
      links:
        - mysql
      working_dir: /var/www/html
      volumes:
        - "./wordpress/wp-content/:/var/www/html/wp-content"
      environment:
        WORDPRESS_DB_PASSWORD: project
        WORDPRESS_DB_USER: project
        WORDPRESS_DB_NAME: project
    {{< / highlight >}}

in cui

-   *imge* definisce che il container deriva dall'ultima installazione
    di Wordpress
-   *ports* definisce su che porta questo docker lavora, in modo da
    poter aprire un browser e simulare una installazione Wordpress
-   *link* definisce a quali altri container è legato per il
    funzionamento, in questo caso al container del database che è
    *mysql*
-   *working\_dir* che è la cartella di installazione di Wordpress
-   *volumes* che configura una cartella *wordpress/wp-content/* nella
    root del progetto dove è possibile installare i temi e plugin che si
    sta sviluppando
-   *enviroment* che configura le variabili d'ambiente per l'accesso al
    database

Tutto questo meccanismo mi permette avere attualmente 5 installazioni di
server Apache e 5 server MySql non comunicanti tra loro. In oltre, tutto
questo non è sempre attivo in background ma viene attivato quando eseguo
i comandi di avvio e termina quando killo il processo. Questo mi
permette, in oltre, di avere 2 versioni di server e PHP installati nella
macchina e, senza tanti problemi, a lavoro finito cestinare tutto senza
lasciare traccia sul computer.

Spero che il codice vi sia utile e lo consiglio se dovete sviluppare
temi, in quanto permette di avere tutto Wordpress installato senza
bisogno di configurare niente, tutto con la root puntata alla cartella
del progetto.

Buon sviluppo

Fundor333
