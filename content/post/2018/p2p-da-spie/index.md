---
title: P2P offline come le Spie
date: 2018-02-16 00:00:00 +0000
tags:
- p2p
- hacking
slug: p2p-offline-da-spie
description: Esistono altri sistemi per la condivisione p2p e quelli offline sono
  particolarmente interessanti. Eccone alcuni dei più interessanti
categories:
- rant
feature_image: "freccia.jpg"
---
Da poco ho scoperto che nel 2006 l'agenzia Russa FSB ha accusato gli inglesi di spionaggio attraverso una roccia "_wirless_"[^1] e questo mi ha ricordato di alcuni progetti P2P che seguivo.

Partiamo con ordine: cos'è il P2P?

*P2P* sta per "**P**oint **to** **P**oint" ovvero "*punto a punto*". Significa che la comunicazione è tra il "mittente" e il destinatario senza utilizzare intermediari. Questo, nel mondo moderno di internet e nel mondo delle nuove tecnologie, è rarissimo da trovare. Solo le tecnologie *.torrent* e dei *magnet link* assieme ad alcune rare eccezioni di servizi di chat sono gli unici servizi per l'utente puramente *P2P* (il p2p tra macchine non lo prendo in considerazione perchè esce dal punto dell'articolo anche se è importante notare che c'è ed è molto presente)

Questo ha portato alla creazione di alcuni progetti hardware/software che cercano di creare questa comunicazione "offline" (in modo da evitare terzi) partendo dal concetto di *Dead Drops*.

Nonostante quello che mostrano nei film, lo scambio 'di persona' è molto pericoloso e raramente usato. Viene invece usato il *Dead Drops* o *consegna morta*:
dopo essersi accordati su un punto di consegna, il mittente lascia il "pacchetto" nel punto di consegna dove, il ricevente, lo viene a ritirare
	
Da questa idea nasce il primo progetto che esamino da lungo tempo: il progetto "*Dead Drops*"

## Dead Drop
![Dead Drop USB](deaddrops.jpg)

Nato come progetto d'arte di Aram Bartholl, un artista con base a Berlino, è un progetto che è stato molto apprezzato nelle comunità underground urbane e di hacking.[^2]

Infatti è considerabile come _hack urbano_ in quanto è, semplicemente, il posizionamento di supporti di memoria fissa nel territorio. Ad esempio il murare una chiavetta usb su una parete o legare, con una sicura, ad un albero un supporto usb.

Tutto questo viene gestito all'interno di un sito internet [link](https://deaddrops.com/dead-drops/db-map/) che ha anche un [database](https://deaddrops.com/dead-drops/db-map/) in cui vengono segnalati i dead drop esistenti, il contenuto di partenza e lo stato del supporto stesso per rendere tutto più semplice e funzionale. 

Questo sistema risulta essere molto interessante da un punto di vista tecnico ma difficile da mantenere in quanto molto soggetta allo stato della parete stessa e alle condizioni atmosferiche dell'area. In oltre può essere anche intesa come _danneggiamento di suolo pubblico/privato_.

Personalmente lo trovo un sistema molto funzionale nel caso venga applicato in un campus o una situazione controllata come all'interno di un negozio o di un caffè, in quanto riesce a essere più facilmente mantenuta.

[Manifesto Dead Drop](https://deaddrops.com/dead-drops/manifesto/)

---

Invece esistono dispositivi più facilmente mantenibili che ottengono lo stesso risultato di condivisione offline.

## PirateBox

Ispirata dal sistema delle radio pirata, la PiratBox è un sistema hardware di offline sharing che utilizza tecnologie OpenSource (FLOSS per gli amici) per la condivisione dei file e contenuti.[^3]

![Pirate Box](piratebox.gif)

Tecnicamente è un router modificato in modo da creare un _hotspot_ "offile" da cui prendere e lasciare file e commenti. Si basa su una "patch" di _OpenWrt_ che trasforma il router compatibile in un hotspot/server. 

Attraverso una interfaccia web e collegandosi via WiFi è possibile caricare e scaricare i file contenuti all'interno della _PirateBox_.

Ovviamente, essendo tutto FLOSS è possibile modificare sia la patch che il sito in modo da creare un dispositivo più adatto al proprio scopo.

In particolare sono state effettuate delle "_mod_" della PirateBox basate proprio su questo principio che utilizzano come base la PirateBox per ottenere però la condivisione unilaterale di contenuti di uno specifico tipo:

* __PirateBox Streaming Radio with Icecast__ Utilizzando _IceCast_ è possibile utilizzare la PiratBox come "server" per la radio[^3.1]
* __OpenStreetMap on PirateBox__ Con alcune modifiche è possibile condividere mappe di OpenStreetMap sulla PirateBox[^3.2]
* __Calibre eBook Server on PirateBox__ Utilizzando [COPS](https://blog.slucas.fr/projects/calibre-opds-php-server/) è possibile avere un server contente una biblioteca di Calibre sulla propria PirateBox[^3.3]

In oltre alcune di queste modifiche sono diventate talmente _grosse_ da diventare progetti indipendenti come LibraryBox.

---

## LibraryBox

Mod e poi fork di _PirateBox_, è la versione "per libri" della _PirateBox_. 

Risulta utilizzare la stessa base hardware (sempre un router con una unità di memoria) ed è sempre una "_patch_" di _OpenrWrt_ a cui viene cambiata l'interfaccia grafica e alcune funzionalità.

![Library Box](librarybox.png)

Infatti è un sistema di condivisione unidirezionale, pensato per ottenere in una location un mediaserver di condivisione di documenti offline, che permetta la _distribuzione_ di una scelta di documenti/file. Questo ha portato il dispositivo a essere molto aprezzato nel mondo dell'educazione, dove rende possibile la condivisione di documenti _pesanti_ semplicemente attaccandosi al WiFi del dispositivo, senza appesantire le reti della struttura.

In oltre viene molto aprezzato in alcune aree in cui viene _censurato_ l'accesso alla rete, che porta a aver bisogno di costose _VPN_ per il recupero di determinate risorse, che la _LibraryBox_ permette di condividere molto più facilmente.

Questo ha portato molti a sfruttare molto più pesantemente la _LibraryBox_ rispetto alla _PirateBox_ portandone anche a un maggiore sviluppo della stessa, che risulta molto più facile da costumizzare nella parte grafica (cosa molto più complessa nella _PirateBox_).

---

Fondamentalmente queste sono le tecnologie _P2P_ offline che suggerisco e di cui mi sono interessato nel mio tempo libero. Nel caso ne trovi di nuove mi preoccuperò di fare un aggiornamento in quanto l'argomento a me piace in modo particolare e lo trovo anche particolarmente interessante anche dal punto di vista umano, perchè è sempre interessante vedere i nuovi sistemi con cui il genere umano condivide la conoscenza.
 
[^1]: [The Guardian: Moscow names British 'spies' in NGO row](https://www.theguardian.com/world/2006/jan/23/russia.politics)
[^2]: [Sito ufficiale del progetto Dead Drops](https://deaddrops.com)
[^3]: [Sito ufficiale del progetto Pirate Box](https://piratebox.cc)
[^3.1]: [Thread sulla mod con Icecast](http://forum.piratebox.cc/read.php?2,3764) e [tutorial](https://github.com/janbre/Assorted/tree/master/Piratebox/PirateBoxRadio)
[^3.2]: [Thread sulla mod con OpenStreetMap](http://forum.piratebox.cc/read.php?2,6988) e [tutorial](https://github.com/reinvented/openstreetbox)
[^3.3]: [Tutorial](https://forum.piratebox.cc/read.php?8,7921,7921#msg-7921)
[^4]: [Sito ufficiale del progetto Library Box](http://librarybox.us)
