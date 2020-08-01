---
title: Grumpy, come convertire il serpente nel gopher
date: 2017-01-26 00:00:00 +0000
tags:
- golang
- python
- google
slug: grumpy-come-convertire-il-serpente-nel-gopher
description: Cos'è Grumpy e come la penso su questo progetto di Google e le sue conseguenze
categories:
- rant
feature_image: "grumpy-go.jpg"
feature_link: "https://unsplash.com/photos/ICW6QYOcdlg"
feature_text: "Photo by Marius Masalar on Unsplash"

---
Io sono un pythonista che cerca di rimanere informato di quello che succede nel mondo di Python e quello che fanno alcune aziende particolarmente grosse o di mio interesse.

Quindi quando ho visto che Google lancia Grumpy in un articolo nel loro [blog](https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html) non potevo che essere incuriosito  e interessato ad avere ancora più notizie sul questo progetto. E, grazie ad un podcast che ascolto ho avuto ancora più notizie.

Io sono iscritto al podcast [Talk Python](https://talkpython.fm/) dove in un [episodio](https://talkpython.fm/episodes/show/95/grumpy-running-python-on-go) è stato intervistato Dylan Trotter, Ingegniere Youtube e un entusiasta di GoLang.

<!--more-->

Questa intervista mi ha permesso approfondire questo progetto che mi incuriosiva molto.

[Grumpy](https://github.com/google/grumpy) è un compilatore source-to-source ovvero un software che, dato del codice in un linguaggio, lo converte in un altro linguaggio di programmazione, con un compilatore che lo compila e esegue.

Personalmente lo trovo molto interessante perchè mappa alcune strutture Python (dico alcune in quanto il 70%-80% delle strutture di Python sono state "mappate" da Grumpy ma non ancora tutte) vengono transposte in GoLang, ottenendo così le ottimizzazioni di GoLang per quanto riguarda i processi concorrenti e alcune strutture, oltre a un tempo migliore in quanto non sarebbe più codice interpretato ma eseguito.

La cosa che, però, a me interessa di più è capire perchè Google ha spinto in questa direzione e qui mi viene in aiuto il podcast di TalkPython: Google, il motore di ricerca e YouTube, il front end per lo meno, sono interamente gestiti da codice Python 2.7.x.

Infatti Google vuole sostituire tutto il codice Python 2.7.x (definito legacy code) con una versione più "nuova e performante" per mantenere il sistema performante e sempre al massimo della potenza. Per questa ragione potrebbe, in futuro, convertire alcune componenti da Python 2.7.x (notare bene che, per ora, Grumpy non supporta la conversione di Python 3.x) in GoLang in modo automatico per semplificare e velocizzare il lavoro. Questo mostra, anche, una grossa intenzione di abbandonare Python 2.7.x (NB: non è possibile fare assunzioni su Python 3.x da Grumpy) in favore di altri linguaggi più moderni/efficaci/adatti al sistema immenso di cluster che Google deve gestire.

Per questo motivo io inizierò a sperimentare con Grumpy per capirne i limiti e i vantaggi rispetto a un CPyhton o Jython e a fare più attenzioni alle librerie per GoLang rilasciate da Google.
