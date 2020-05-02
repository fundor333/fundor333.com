---
title: Emacs e mai più mouse
date: 2017-02-14 00:00:00 +0000
tags:
- emacs
- texteditor
- programmazione
- tool
- rant
slug: emacs-e-mai-piu-mouse
description: Cos'è Emacs e perchè ho iniziato a usarlo e rimosso il mouse dal mio
  set per il pc
categories:
- rant
feature_image: "emacs-mouse.jpg"
feature_link: "https://unsplash.com/photos/oZMUrWFHOB4"
feature_text: "Photo by Paul Esch-Laurent on Unsplash"

---
E ho iniziato a scrivere con Emacs questo blog. Questo mi porta a essere orgoglioso di dire che questo blog è _mouse free_!

Ok posso capire che per la maggior parte di voi non capirà perchè questo cambiamento è rilevante per me ma, dal mio punto di vista, è un _ENORME_ upgrade tecnico. La possibilità di avere un intero editor di testo personalizzabile, multipiattaforma e completamente open source mi ha sempre particolarmente colpito ma non ho mai trovato uno che lo sentissi mio. Attualmente uso molto Atom ma lo sento molto stretto soprattutto perchè, visto che deve supportare molti linguaggi (e di conseguenza molti plugin), risulta rallentato.

<!--more-->

## Come sono arrivato a questa scelta
Io ho bisogno di un software di editor di testo che avesse determinate funzioni:

* __Multipiattaforma__ in generale preferisco software che sia multipiattaforma e che quindi mi permetta di passare senza problemi da un sistema ad un altro.

* __Completamente configurabile__ permettendomi di trasformare l'ide/editor in esattamente quello di cui ho bisogno.

* __Open Source__ personalmente preferisco software open source a quello a pagamento ma non disdegno software a pagamento.

* __Deve poter supportare tutti i linguaggi che voglio__ questo è il problema più grosso. Se il programma scelto ha un buon sistema di plugin, questo permette anche di avere un buon supporto per un ampio numero di linguaggi attraverso i plugin stessi.


## I candidati alla posizione

Ho esaminato alcuni editor di testo e ho analizzato i loro punti di forza e di debolezza. Questa analisi rimane soggettiva e basata sulle mie personali esigenze e non obbligatoriamente quello che per me è un difetto per altri potrebbe essere un pregio.

* __Atom, Code e Sublime__ Gruppo di editor di testo espandibili ma per me poco pratici: Sublime ha il discorso della licenza da pagare e, da quello che ho visto nella versione di prova, per le mie esigenze non è motivata la spesa. Atom e Code di perse funzionerebbero anche bene ma è il sistema di plugin e i limiti dati da Node.js (esempio il fatto che devi aver installato Node.js e che per alcuni file abbastanza grandi soffrono, senza contare crash non comprensibili) risultano troppo "esigenti" rispetto a quello che necessito a livello di funzionalità. Infatti se sovraccaricati di funzionalità/plugin entrambi gli editor ne risentono molto e molto velocemente.

* __Vim__ Editor testuale tra i più vecchi al mondo. Installato in ogni sistema server esegue egregiamente il suo lavoro ma, dopo una brutta esperienza con lui per un commit, non sarei molto per usarlo.

* __Emacs__ Altro editor testuale molto vecchio, completamente open source risulta molto leggero ed è completamente configurabile conoscendo Lisp e usando i plugin appositi

Oltre a questi ce ne sono molti altri che sono troppo situazionali che non ho nemmeno considerato o perché sono close source che amo.

Da qui mi sono informato sui plugin disponibili per Emacs e, dopo aver visto che c'è​ il plugin per pelican e molti per Python, ora sto imparando a usare Emacs
