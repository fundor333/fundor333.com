---
title: 'DevOps, ChatBot e NPM'
date: 2019-02-05T10:11:07.668Z
draft: false
feature_image: /images/uploads/octocat.png
tags:
  - devops
  - bot
  - chat
  - chatbot
  - npm
categories:
  - dev
slug: devops-chatbot-npm
description: Aggiornamento su cosa mi sta succedendo e perché ho iniziato a fare il DevOps
---
Attualmente al lavoro il team di sviluppo é "giusto per le esigenze aziendali". Questo significa due persone. Questo comporta anche che non esiste un _backendista_ e un _frontendista_ full time ma tutti fanno tutto.

Con poi anche problemi legati alla pipeline di rilascio in produzione del codice che viene fatto manualmente e con molta (poca) attenzione. Fino al giorno dell'ARMAGEDDON.

# Buona Apocalisse a tutti e grazie per il pesce

Kube, k8, Kubernetes o come lo chiamiamo noi _il clousterone_ é stata la cosa che ha sconvolto la quiete del nostro reparto sviluppo.

Per chi non é avvezzo al rilascio attraverso Kubernetes la cosa importante da sapere é che serve una o piú immagine Docker contenete il codice da eseguire, un set di permessi (sul cluster su cui si pubblica il progetto) e tanti comandi via terminale per i settaggi e simili.
Questo ha portato alla creazione di _N_ sistemi di notifica, deployment e automatizzazione che devono convivere assieme. Questo sta portando a molto scripting soltanto per risolvere queste problematiche.

## Scelta delle tecnologie ovvero di che morte devo morire

Qui cade la parte divertente e parte quella pesante. Per far funzionare i nostri sistemi ci siamo affidati per prima cosa a dei linguaggi con cui preparavamo degli script che, una volta lanciati, buildavano o facevano cose per la messa in produzione. Questi erano in Python e Bash e fondamentalmente ogni progetto aveva comandi diversi per la messa in opera con parametri diversi e path diversi. Una volta che si inizia ad avere tanti progetti diventa quindi necessario rivederli e unificarli in modo da stare tranquilli. Questo vale anche per il sistema di logging e notifica degli errori.

## Le nostre marionette

Questo ha portato alla creazione di sistemi automatici/bot per i task. Partendo da due scuole di pensiero differenti abbiamo sviluppato entrambe le scuole in modo da essere piú completi.

* _**Hook**_ basati su _git_ questi lanciano build in modo automatico basandosi sul co0dice che scriviamo. Interamente indipendente da il nostro intervento
* _**URL**_ collegati a _bot_ ci permettono di lanciare operazioni in qualsiasi momento e sono chiamabili a disponibilitá.

Questo ha portato alla creazione di un modulo per la [gestione del té in _coffescript_](https://www.npmjs.com/package/hubot-tea-timer) per _Hubot_, framework per bot di Github.

A presto altri dettagli e info su bot per automatismi e, se posso, anche del codice annesso.
