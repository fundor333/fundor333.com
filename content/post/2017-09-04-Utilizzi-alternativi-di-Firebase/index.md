---
title: Utilizzi alternativi di Firebase
slug: utilizzi-alternativi-di-farebase
date: 2017-09-04 00:00:00 +0000
tags:
- firebase
- logging
description: Utilizzare le funzionalità di Firebase in modo non 'standard'
categories:
- rant
aliases:
- "/blog/utilizzi-alternativi-di-farebase/"

feature_image: "/post/utilizzi-alternativi-di-farebase/alternativi-firebase.jpg"
feature_link: "https://unsplash.com/photos/pKeF6Tt3c08"
feature_text: "Photo by Brendan Church on Unsplash"
---
Uno dei problemi che avevamo al lavoro era quello di controllare un insieme di processi remoti. Quando hai un applicativo gestionale che deve visualizzare in breve tempo i dati all'utente senza rallentare mai la visualizzazione, devi avere alcune componenti/operazioni che lavorano in asincrono rispetto alla parte di I/O dell'utente.

Questo obbliga ad avere file di log nella macchina che sta eseguendo il task asincrono e dover leggere da quello l'esecuzione del processo nel caso io voglia vedere come sta andando il alvoro. Questo non sarebbe un problema se ci fosse solo una macchina che svolgie i processi asincroni ma ce ne sono due sempre in funzione che permettono di alleggarire il carico di lavoro e accellerarlo quanto basta per non creare code di task.

Questo ci porta alla necessità di avere una "dashboard/console/roba" che ci permetta di vedere in tempo reale l'andamento dei processi e, nel caso abbiano errori, identificare quale processo si è interrotto.

_NB_ Questo non è un tutorial completo in quanto non porto un esempio di codice in un linguaggio specifico in quanto può essere implementato con tutti i linguaggi di programmazione e di scripting

# Prima fase: strutturare il db

Come prima fase devo andare su [Firebase](https://firebase.google.com/) e creare un progetto in modo da ottenere così un database in tempo reale su cui è possibile leggere e scrivere.

Una volta ottenuto il db, io creo un file json di prova dove inserisco tutti i tipi di task asincroni che posso lanciare e controllo che non ci siano sovrapposizioni di chiavi, in modo da avere il database ad oggetti diviso in parti corrispondenti ai task o gruppi di task.

Non lo faccio direttamente sul db ma su un file apparte perchè se un elemento di firebase non contiene niente viene eliminato dal db stesso, rendendo così inutilizzabile la struttura del db se ho bisogno di un riferimento al risultato per lo sviluppo.

# Seconda fase: preparare il doppio logger

Sovrascrivo la funzione che utilizzo per fare logging in modo che ogni qualvolta scrive nel file di logging, scrive anche nel campo Firebase associato, ottenendo così un hub di tutti i log dei processi asincroni.

Quindi faccio in modo che, quando il processo termina con sucesso, cancella i dati di quel processo da firebase ottenendo così un elenco di solo processi attivi dentro firebase.

Per come è strutturato il resto del codice, il progetto, se il processo asincrono non va a buon fine, non termina il processo e non cancella la voce dentro firebase. Questo mi permette di recuperare i dati di esecuzione di quella task e di lanciarla su un ambiente controllato dove viene poi fatto il debug del problema.

# Terza fase: costruire la visualizzazione

Con HTML e JS è stato possibile creare una pagina statica che mi visualizza i dati dei task asincroni e del loro avanzamento, dividendoli per categorie e ordinadoli in tempo di avvio. Questo punto si puo' anche saltare in quanto è possibile usare la dashboard di firebase stessa per avere lo stesso risultato con meno personalizzazione.


Spero che questo articolo ti sia stato utile e, se vuoi qualche info in più  ovuoi condividere la tua esperienza, commenta pure
