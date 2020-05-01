---
title: Scrivi, push e publica
date: 2017-01-14 00:00:00 +0000
tags:
- github
- wordpress
- container
- pelican
- travis
- git
slug: scrivi-push-public
categories:
- dev
description: Come scrivere un blog interamente in pelican, gestito in github e travis
  con autopubblicazioni
aliases:
- "/dev/scrivi-push-public/"
feature_image: "/post/scrivi-push-public/scrivi-push.jpg"
feature_image_name: "scrivi-push.jpg"
feature_link: "https://unsplash.com/photos/ICW6QYOcdlg"
feature_text: "Photo by Galymzhan Abdugalimov on Unsplash"
---
Ho riscritto interamente il blog. Ora gira tutto in Python... Anche se nel server è tutto in HTML5.

Questo perchè sento la necessità di legarmi a una tecnologia più elastica e a me congeniale rispetto a PHP. Prima infatti tutto il blog era basato su wordpress ma, cercando di sviluppare un tema per il blog non ero convinto.

Così sono passato da un blog dinamico a uno statico.

Come mi hanno detto una volta, le storie miglioni non hanno un inizio, si parte già al centro dell'azione e questo è quello che è successo: io stavo scrivendo un layout html per questo blog ma non ero soddisfatto di dover utilizzare PHP come linguaggio di composizione delle pagine. E' qui che ho iniziato a farmi idee su come potermi sganciare da wordpress e PHP verso qualcosa di più _nel mio stile_ più _mio_. Qui è quando ho visto un blog che seguo da tempo nel mio aggregatore di RSS, il blog di [Eevee](https://eev.ee/). E' un blog di questo programmatore che seguo da un po' appassionato di Python e gaming, con una _leggera_ passione per i PokeMon.

Qui avevo notato che, nel footer, c'era l'avviso che il blog è stato realizzato in Python ma con un "_web framework_" che non conoscevo, [Pelican](http://docs.getpelican.com/en/stable/#).
Dopo una prima analisi della documentazione mi rendo conto che è un generatore di siti statici, ovvero dato qualcosa ritorna un sito HTML completamente costruito dai dati che gli dai in pasto (nel mio caso dati in formato [Markdown](https://it.wikipedia.org/wiki/Markdown)) compreso di post e pagine.
* * *
Questo mi ha portato a realizzare un tema basato sulla sintassi utilizzata dal [Jinja2](http://jinja.pocoo.org/docs/dev/).

## Definizione del tema
Il tema in se non è stato difficile da realizzare, molto css era già pronto da miei precedenti tentativi di realizzare un tema personale ma è stato lungo realizzare tutti i cicli per la visualizzazione corretta di pagine, articoli e link più per una questione di mio gusto artistico che che per un reale problema tecnico/limite di Pelican.

Con l'aiuto di [Bootstrap](http://getbootstrap.com/) mi è anche stato facile realizzare il sito in modo responsive, sistemando così anche questo problema.

## Backup da wordpress
Con l'aiuto di un comando integrato di Pelican è stato possibile importare il vecchio sito wordpress. Questo mi ha permesso di poter mantenere i post del blog vecchio assieme alle pagine. Tutto questo è stato quindi salvato in formato Markdown e suddiviso nelle rispettive directory in base alla categoria e ri-etichettate in base al nuovo sistema utilizzato da Pelican.

_Piccola nota a parte sulla cosa: io mi trovo MOLTO meglio con il sistema di gestione di pagine e articoli di Pelican che quello di Wordpress. Qui io posso aggiungere ai miei post un nuovo meta-dato e creare una corretta visualizzazione del metadato stesso senza andare a toccare Pelican stesso (come avresti dovuto fare con Wordpress)._

## Installazione plugin
Inizialmente io ho pensato di utilizzare la "nuova" funzionalità dei sub-moduli di Git ma questo mi ha portato più problemi che altro.

Dopo svariati tentativi e poca comprensione di perchè continua a essere elaborato male da git e dal mio ide ho pensato che i plugin sono più facili da gestire semplicemente copiandoli in una cartella e aggiornando a mano.

## Sistemazione articoli e pagine
Ho fatto un po' di pulizia perchè il meccanismo di importazione automatica lascia dello "sporco" qui e li sotto forma di codice html/css non più desiderato in alcuni punti (precedentemente era usato da plugin e dal tema di wordpress per fare cosucce ma col passaggio è risultato inutile).

Stessa cosa è successa con le pagine ed è stato più veloce. Sono, per ora, in attesa di revisione e correzione, in modo che siano aggiornate e più coerenti con la grafica del nuovo tema.

## Travis e la autopublicazione
Dopo aver elaborato le pagine e gli altricoli ho quindi preparato il repository github seguendo il paradigma di [Git Flow](http://danielkummer.github.io/git-flow-cheatsheet/) e preparando TravisCI per la autopublicazione degli articoli. Questo mi consente di accedere a un qualunque pc collegato a internet, andare sul sito di github, aggiungere il post o editare parte del sito e travis si occupa dell'elaborazione e di mandarmi il log in caso di fallimento, tutto intermente sul server, senza aver niente installato sul pc che sto usando per scrivere.

Il settaggio di Travis in se mi ha tolto circa un ora di sonno perchè non sono stato in grado di capire alcuni piccoli comandi. Ora però il meccanismo funziona e, grazie alle funzionalità beta di Travis ho avuto una idea...

## Progetti per il futuro
Intanto spero di rilanciare il blog, renderlo più attivo e seguito e poi spero di riuscire a scrivere un piccolo plugin per Pelican ma questa è una storia per un altra volta...
