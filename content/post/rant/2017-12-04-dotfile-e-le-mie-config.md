---
title: "DotFile e le mie config"
date: "2017-12-04"
slug: "dotfile-e-le-mie-config"
tags: ["dotfile", "config", "repository", "dotbot"]
description: "DotFile e la mia configurazione di tutto"
---

Da quasi 10 anni io utilizzo _Linux_ o sistemi _Unix_ su tutti i pc che utilizzo. Questo mi ha portato a creare svariate configurazioni personalizzate legate a i vari servizi/programmi/script che utilizzo tutti i giorni, perdendo un tempo notevole in caso di ripristino a risettare tutto com'era.

Quindi ho imparato a "backappare" i file di configurazione e stavo iniziando a scrivere un orrendo accrocchio per la generazione delle configurazioni in modo automatico partendo da un database sqlite, che, per quanto intelligente come idea, non è una cosa di facile gestione ne adatto alla situazione che si è creata. 

Quindi, girando su _GitHub_ ho incontrato il progetto [DotFiles](https://dotfiles.github.io). Questo è una abitudine/gioco/sistema che va "di moda" su _GitHub_. Viene fatto un repository dei propri file di config (che, nei sistemi _Linux/Unix_ iniziano sempre con il punto) con uno script di _install.sh_ che, quando lanciato, installa correttamente le config e permette di partire dopo un ripristino o una reinstallazione in modo molto veloce.

Per quanto mi riguarda io lo ho stutturato in modo da seguire nel modo migliore le mie esigenze e ho utilizzato un software per la gestione dei _dotfile_ 

* DotBot
Utility scritto in _Python_, gestisce l'installazione dei file di configurazione nella home utilizzando la configurazione presente nel file _install.conf.yaml_

* DotBot Pip
Plugin per il DotBot che mi permette di gestire l'installazione dei moduli python in automatico. Questo mi permette di settare in automatico già alcune mie dipendenze che installo praticamente sempre.

* install.conf.yaml
Il file di configurazione, necessario per il funzionamento di DotBot. Raccoglie tutto ciò che il bot deve fare per ripristinare le config

* I dotfiles
Tutti i file e le cartelle predisposte per essere importate per ripristinare le configurazioni. Si suggerisce la divisione in cartelle anche per poter tenere meglio organizzato il repository/backup

* Aggiornamento
Bisogna tenere sempre i file e per farlo va fatto a mano. Personalmente credo che sia il modo migliore per aggiornarli è farlo a mano. Si ha così controllo e si riesce a mantenere puliti i file di configurazione. 

* Per terminare
E' importante rimanere anche aggiornati su come cambiano i config dei programmi e servizi che si usano. Per questo suggerisco di seguire gli aggiornamenti dei programmi/servizi di cui si stanno tenendo i dotfile e di seguire anche i tweet di @EditorConfig che da utili consigli e condivide altri repository di dotfile per confronto/copia. 

Comunque la cosa importante è rimanere sempre informati dei cambiamenti che avvengono nei propri dotfile e perchè accadono. Questo permetterà anche di capire meglio le stesse impostazioni e controllare che siano sempre come vorremmo.

Spero che questi consigli vi tornino utili.

Fundor333
