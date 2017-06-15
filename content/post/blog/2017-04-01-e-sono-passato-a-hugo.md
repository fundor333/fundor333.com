+++
title= "E sono passato a Hugo"
date= "2017-04-04"
tags= ["hugo","pelican","blog","golang","https"]
description= "Come e perchè sono passato a Hugo da Pelican"
+++

E sono passato a Hugo da Pelican perchè Pelican non mi soddisfa.
Dopo un po' di utilizzo di Pelican ho deciso di prendere e fare due cose a modo mio perchè non mi piacciono o non supportate: una risistema al tema che è vermente una mostrosità di codice e la gestione delle categorie

<!-- more -->

### Problemi personali
Perchè ho deciso di cambiare? Perchè ci sono due cose che sento strette:

 - La strutturazione del layout, che sento stretta e strutturata in modo "sbagliato"
 - L'impossibilità di avere multiple _category_ per un singolo post senza implementare io stesso un plugin

A questi si aggiunge che non sono mai riuscito a far funzionare correttamente la configurazione che obbliga a renderizzare solo i post "passati" e non "futuri" am credo che questo sia un problema mio.

### La scelta
Ho scelto Hugo rispetto a Jekyll in quanto non ho interesse a lavorare in Ruby ma, invece, sono incuriosito a lavorare in GoLang (linguaggio in cui è interamente scritto Hugo) e me ne hanno parlato molto bene.

Leggendo anche in giro non mi è sembrava particolarmente difficile la conversione Pelican -> Hugo per cui ho dato una occhiata a come eseguirla.

Per avere un blog di Hugo devi avere:

  1. Una "installazione" aggiornata di Hugo
  2. Uno spazio web dove poterti connettere
  3. Un tema per Hugo

### Realizzazione

Scelto il generatore statico di siti è stata la volta di implementareil resto del sito.

#### Installazione

L'installazione di Hugo è la cosa più semplice. Scarichi dal [sito](https://gohugo.io/) e segui le istruzioni per installarlo nel sistema operativo che si possiede.

Una volta installato è stato possibile utilizzare comandi di Hugo da terminale costruendo così lo scheletro del tema e della struttura del blog.


#### Contenuto

Bisogna convertire tutto il contenuto in un formato conpatibile con Hugo. Per mia fortuna il formato è sempre un _Markdown_ per i contenuti mentre uso il formato Toml per i metadata. Hugo supporta anche altri formati per i metadata ma quello in cui mi trovo meglio è il Toml e di conseguenza ho modificato (a mano) tutti i post e le pagine per farli funzionare col nuovo sistema.


#### Tema
Per il porting del sito è stato necessario fare il porting del tema in Hugo da Pelican o usare uno dei temi disponibili online.
Ho quindi deciso di prendere i css e i js del tema pelican e riscriverlo per Hugo. E' stato retalivamente facile una volta capito il sistema di temi di GoLang che risulta diverso da [Jinja](http://jinja.pocoo.org/), che è il sistema utilizzato da Pelican.

#### Publicazione
Fatto questo ho portato tutto su GitLab dove ho configurato il settaggio per la compilazione automatica in modo da porter pushare i file e lui pensa a ricompilare tutti il sito.

    image: publysher/hugo
    pages:
      script:
      - hugo
      artifacts:
        paths:
        - public
      only:
      - source

Con questa configurazione ogni qual volta viene pushato un commit del branch _source_ lui esegue l'elaborazione del sito nella cartella _public_ che viene a sua volta visualizzata da GitLab come _root_ del sito internet e distribuita online a chiunque richieda la pagina.

#### HTTPS
Ho utilizzato [Let's Encrypt](https://letsencrypt.org/) per generare un certificato per il dominio associato al sito e lo ho caricato su _static/.well-known_ come indicato dal servizio ottenendo così una connessione https configurata per il mio dominio
