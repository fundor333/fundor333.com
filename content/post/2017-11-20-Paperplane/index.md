---
date: 2017-11-18 00:00:00 +0000
tags:
- python
- telegram
- paperplane
- status
- framework
title: Il mio Paperplane
description: Presentazione del mio progetto chiamato Paperplane, framework per Telegram
categories:
- rant
slug: il-mio-paperplane
aliases:
- "/blog/il-mio-paperplane/"

feature_image: "/post/il-mio-paperplane/paperplane.jpg"
feature_link: "https://unsplash.com/photos/BwXBIo0a1ts"
feature_text: "Photo by Adetunji Paul on Unsplash"
---
Ultimamente ho cambiato lavoro e ho cambiato alcuni aspetti secondari della mia vita di cui non sento la mancanza ma risulto stare meglio. In tutto ciò ho deciso che sono troppo vecchio (25 anni sono tanti, tutta una vita per me) e che non posso permettermi di perdere altro tempo (e qui sembro una delle vittime dei Signori Grigi di Momo). Per questo motivo mi sono lanciato in un grosso progetto personale:  **Paperplane**.

Per ora solo in Alfa, è un modulo/framework python per scrivere bot telegram che utilizza pesantemente la parte funzionale, le annotazioni e, presto, la parte asincrona di Python per comunicare con telegram.

Per ora mi baso su *Requests* per fare il lavoro di muscoli ma penso di passare poi alla versione asincrona fatta con *Tornado* (credo).

Questo però non è detto, in quanto, pensando di implementare la possibilità di avere multipli bot in un unico applicativo, potrei preintegrarla con *Tornado* o simili in modo di poter ottenere un flusso di lavoro più continuo per il bot senza farlo passare dalla fase di attesa a quella di esecuzione di comandi.

E tutto questo utilizzando soltando ***Python 3*** in quanto credo seriamente che sia un mio obbligo personale di scrivere solo in *Python 3* visto che sta finalmente per essere deprecato *Python 2.7*.

Speriamo che sia un progetto utile e, se interessati, lo trovate [qui](https://github.com/fundor333/paperplane)
