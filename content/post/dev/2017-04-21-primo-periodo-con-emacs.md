+++
title = "Il primo periodo con Emacs"
date = "2017-04-21"
categories=["dev"]
slug="il-primo-periodo-con-emacs"
tags=["emacs","editor","ide"]
description="Diario del mio primo periodo di utilizzo di Emacs"
+++

Ho iniziato a utilizzare Emacs in modo sempre più completo, dai piccoli file a quelli sempre più grossi fino  usarlo come editor unico.
La parte più difficile è stata la parte iniziale dove sono dovuto entrare nella mentalità di Emacs ovvero quando ho dovuto imparare a lavorare su buffer e windows.

Da questo punto di vista il tutorial dentro emacs è un ottimo punto di partenza e ambiente ove testare e provare i comandi su un documento "bloccato e non danneggiabile".

<!-- more-->

Questo primo periodo di utilizzo mi ha permesso di vedere che è un programma completo e molto efficente. In modo particolare ho addirittura iniziato a sviluppare una prima bozza di personalizzazione del mio Emacs attraverso una prima configurazione di _.emacs.d/_ disponibile su [Github](https://github.com/fundor333/emacs.d).


## Prima fase installazione di base

Partiamo con ordine: si inizia con l'installazione e comprensione dei config.
Dopo l'installazione ottenuta attravero il classico

     sudo apt-get install emacs

Fatto questo io mi aspettavo che, dopo il primo avvio generasse i file di configurazione. Per come è stato programmato Emacs l'avvio genera solamente il file _.emacs_ se non presente mentre tutto il resto della "struttura" viene generata man mano che si modificano le impostazioni dei singoli elementi.

Quindi ho fatto una piccola ricerca di come cambiare il tema di Emacs che, a mio parere, puo' essere la personalizzazione corretta per iniziare a utilizzare Emacs.

All'avvio Emacs cerca un file _.emacs_ ove dovrebbe trovare i config e, nel caso non lo trovi, va a _.emacs.d/init.el_ ove cerca i config e, nel caso non trova nessuno dei due, genera un file _.emacs_ vuoto o con le configurazioni delle "sessione" corrente. E qui c'è il primo punto di interesse:

## Conviene usare _.emacs_ o _.emacs.d/init.el_?
Per le configurazioni in _Emacs_ ci sono due possibili impostazioni:

 * **Impostazione storica** che utilizza _.emacs_ per mettere tutte le configurazioni
 * **Impostazione a progetto** che utilizza _.emacs.d/init.el_

La versione storica ha il vantaggio di essere facilmente "condivisa" essendo un unico file ma la versione a progetto ti permette di realizzare un sistema più ordinato di configurazioni e permette di usare sistemi di versioning (nel mio caso git) per ordinare e gestire un backup o comunque un sistema di condivisione delle config.

## La mia configurazione in particolare

Ho impostato Emacs utilizzando una impostazione a progetto, in modo da poterlo condividere facilmente su GitHub o altri servizi di hosting per repository git.
Di base utilizzo _init.el_ ove ho settato le basi e il tema, in modo che sia caricato senza problemi

    (add-to-list 'custom-theme-load-path "~/.emacs.d/themes")

    (load "~/.emacs.d/init-packages")

    (custom-set-variables
     ;; custom-set-variables was added by Custom.
     ;; If you edit it by hand, you could mess it up, so be careful.
     ;; Your init file should contain only one such instance.
     ;; If there is more than one, they won't work right.
     '(custom-enabled-themes (quote (dracula)))
     '(custom-safe-themes
       (quote
        ("b97a01622103266c1a26a032567e02d920b2c697ff69d40b7d9956821ab666cc" default))))
    (custom-set-faces
     ;; custom-set-faces was added by Custom.
     ;; If you edit it by hand, you could mess it up, so be careful.
     ;; Your init file should contain only one such instance.
     ;; If there is more than one, they won't work right.
     )


Con questa configurazione si divide le variabili di ambiente settate da Emacs (che devo ancora capira a cosa servano), il tema scelto ([Dracula](https://draculatheme.com/emacs) in questo caso) e i settaggi per i pacchetti che vengono definiti nel file _init-packages.el_.

    (require 'package)
    
    (add-to-list 'package-archives
                 '("elpy" . "http://jorgenschaefer.github.io/packages/"))
    
    (add-to-list 'package-archives
                 '("marmalade" . "http://marmalade-repo.org/packages/"))
    
    (add-to-list 'package-archives
                 '("melpa-stable" . "http://melpa-stable.milkbox.net/packages/") t)
    
    (add-to-list 'package-archives
    	     '("melpa" . "https://melpa.org/package/")t)
    
    
    (add-to-list 'load-path "~/.emacs.d/site-lisp/")
    
    
    ; list the packages you want
    (setq package-list
        '(magit easy-hugo python dracula-theme))
    
    
    ; activate all the packages
    (package-initialize)
    
    ; fetch the list of packages available
    (unless package-archive-contents
      (package-refresh-contents))
    
    ; install the missing packages
    (dolist (package package-list)
      (unless (package-installed-p package)
        (package-install package)))
    
    (when (< emacs-major-version 24)
      ;; For important compatibility libraries like cl-lib
      (add-to-list 'package-archives '("gnu" . "https://elpa.gnu.org/packages/")))
    (package-initialize)


Questo script in Lisp permette di elencare nella prima parte tutta una serie di repository extra da aggiungere all'elenco dei plugin disponibili e li aggiunge all'elenco di Emacs.

    (add-to-list 'package-archives
    	     '("melpa" . "https://melpa.org/package/")t)

Ad esempio questo codice aggiunge il repository [Melpa](https://melpa.org/) all'archivio in modo da rendere disponibili i suoi pacchetti a Emacs.

   (setq package-list
   	 '(magit easy-hugo python dracula-theme))

Questo comando invece permette di elencare i pacchetti di nostro interesse. Ogni pacchetto elencato verrà installato o aggirnato e successivamente attivato all'avvio del server Emacs

    ; install the missing packages
    (dolist (package package-list)
      (unless (package-installed-p package)
        (package-install package)))


Questo è infatti il codice per l'installazione dei pacchetti mancanti.

Con questa configurazione e l'aggiunta di un _.gitignore_ abbastanza pulito mi è possibile mantenere una versione di ripristino dell'ambiente di lavoro Emacs compatibile con ogni sistema operativo che supporta Emacs.

Questa è la mia prima esperienza con Emacs e ne sono entusiasta anche se devo ancora consultare appunti per certi shortcut ma credo che andando avanti non ne avrò di bisogno.
