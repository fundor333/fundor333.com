---
title: Meteo del Sangue e Alta Marea
date: 2016-12-21 00:00:00 +0000
tags:
- bot
- facebook
- open data
- telegram
- twitter
slug: meteo-del-sangue-alta-marea
description: Bot per telegram e twitter per la donazione del sangue e l'alta marea
  a Venezia
categories:
- dev
aliases:
- "/dev/meteo-del-sangue-alta-marea"

---
Ovvero come ho iniziato a scrivere bot per telegram.

Nasce tutto al Pycon It 2016 ove conosco un programmatore Python.  Così
chiaccerando entriamo in contatto e iniziamo a interessarci l'uno
all'altro e così scopro il "Meteo del sangue"


Questo è un servizio che ha rializzato che crea un sistema di
segnalazione automatica dei gruppi sangugni in carenza nella regione
Toscana e posta sui social (Twitter, Facebook e Telegram) i gruppi
sanguigni che necessitano donazioni e quelli che sono a posto attraverso
una grafica.

E da qui nasce il mio progetto Alta Marea.

Il progetto Alta Marea è una applicazione diretta degli open data del
comune di Venezia. Prende i dati dal sito del comune, li formatta e li
pubblica in tre piattaforme formattandoli nel modo migliore per quella
piattaforma.

Per Twitter e Facebook viene inviato il bollettino completo, senza
rimozioni di informazioni di sorta.\
Invece, per telegram, è stato scelto di passare a una forma più filtrata
dei dati: solo i dati che superano la quota di allerta di 90 cm sopra il
livello del mare. Questo è stato fatto per tenere il servizio più pulito
possibile, in quanto risulta essere um canale diretto con l'utente in
quanto si lo contatta direttamente sul telefono.

Questo è stato fatto attraverso due bot, uno twitter e uno telegram, che
ricevono i dati a un intervallo regolare di 5 minuti l'uno dall'altro e
vengono aggiornati solo se i dati sono quelli non ancora pubblicati.

Tutto questo è iniziato mangiando bigne e parlando di Python a una
convention...

PS: per chi è curioso del progetto [qui](https://mareabot.github.io/)
trova altre info su questo progetto o twittatemi a @fundor333
