Title: Gource, visualizzare Git repository
Date: 2016-11-07 13:25
Author: fundor333
Category: blog
Tags: Git, Gource, Video, Visualizzazione
Slug: gource-visualizzare-git-repository
Status: published

Quando hai un progetto Git, normalmente lo usi per fare controllo delle
versioni.\
Una volta che il progetto è nella fase di rilascio tu hai quindi un
repository molto "pieno" di dati temporali e di chi a modificato cosa e
quando. E' solitamente in questo momento che io faccio il "Gource" del
progetto.

<!--more-->

Cos'è questo "Gource" che io faccio dei miei progetti? E' una
rappresentazione grafica dello sviluppo del progetto utilizzando i log
del version controll software utilizzato per il progetto.\
Il video qui sotto è esattamente questo: un progetto sviluppato per il
corso di Ingegneria del software con Git come vcs.

<iframe src="https://www.youtube.com/embed/8cZPHhazUeE" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

[Gource](http://gource.io/) quindi è solo un applicativo software per
visualizzare la crescita dei file di un progetto come fosse una pianta
che cresce e muore in base ai file modificati, tolti e aggiunti del
progetto.

Personalmente lo trovo molto utile per capire i momenti in cui ci sono
stati problemi nello sviluppo ad esempio creazione di grandi
quantitativi di file presto eliminati o un gruppo di sviluppo che va a
toccare troppo i file di altri gruppi puo' servire a una revisione di
fine progetto.

Molto interessante risulta essere anche il progetto derivato da Gource
ovvero [Lostalgia](http://logstalgia.io/). Lostalgia è un visualizzatore
di log per server web. Ti permette di visualizzare le richieste ricevute
e servite in modo pratico e veloce.

<iframe width="560" height="315" src="https://www.youtube.com/embed/K8muK-o80ZU" frameborder="0" allowfullscreen></iframe>

In particolare è possibile vedere molto velocemente traffico "sospetto"
come quello nel video qui sopra. Infatti questo video è un attacco
SQLInjection con un successivo DDOS attack. Questo vuole dire che prima
raccoglie tutto quello che può da un unico indirizzo client e
successivamente intasa tutte le richieste
