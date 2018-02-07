---
title: "Jupyter Notebook Pelican Combo"
tags: ["pelican", "jupyter", "notebook"]
date: "2017-02-14"
slug: "jupyter-notebook-pelican-combo"
categories: ["dev"]
description: "Come ho combinato Jupyter con questo blog in Pelican"
aliases: ["/dev/jupyter-notebook-pelican-combo/"]
---


Si sta avvicinando il **Pycon 8** e io ci parteciperò. Questo vuol dire che ho raccolto i soldi e sto preparando la strumentazione necessaria per quest' anno.
Visto quello che è successo l'anno scorso ho deciso di preinstallate Jupyter e essere pronto a fare degli appunti direttamente in notebook. Per questo ho cercato un sistema per convertirli in markdown, così da usarli anche nel blog, o farli leggere direttamente da Pelican e ho fatto una stupenda scoperta: esiste già questo plugin.
<!--more-->

Per rendererizzare i file _.ipynb_ è necessario aver installato il plugin _pelican-ipynb_ e settato i metadati del _.ipynb_ coi i metadata corretti:

* _Title_ titolo del post
* _Slug_ indirizzo del post
* _Date_ data di publicazione del post
* _Category_ categoria del post
* _Tags_ tag del post
* _Author_ autore del post
* _Summary_ riassunto del post

e settare i tipi di markup supportato con

{{< highlight python "hl_lines=8 15-17" >}}
MARKUP = ('md', 'ipynb')
{{< / highlight >}}


facendoli vedere così i file _.ipynb_ come file da eseguire e visualizzare come post.

L'unico difetto di questo plugin è che che non supporta, _per ora_, il metadata _Status_.

# E quindi funziona?
E si arriva alla domanda fondamentale: "Funziona?" La risposta è si, funziona.


```python
print('Hello world!')
```

    Hello world!


Come vedete nel blocco di codice sopra è funzionante e permette di fare tutto quello che normalmente faresti con Jupyter.


```python
columnA = ['Temporary','Intermittant','Partial','Redundant','Total',
	'Multiplexed','Inherent','Duplicated','Dual-Homed','Synchronous',
	'Bidirectional','Serial','Asynchronous','Multiple','Replicated',
	'Non-Replicated','Unregistered','Non-Specific','Generic','Migrated',
	'Localised','Resignalled','Dereferenced','Nullified','Aborted','Serious',
	'Minor','Major','Extraneous','Illegal','Insufficient','Viral',
	'Unsupported','Outmoded','Legacy','Permanent','Invalid','Deprecated',
	'Virtual','Unreportable','Undetermined','Undiagnosable','Unfiltered',
	'Static','Dynamic','Delayed','Immediate','Nonfatal','Fatal','Non-Valid',
	'Unvalidated','Non-Static','Unreplicatable','Non-Serious']
columnB = ['Array','Systems','Hardware','Software','Firmware','Backplane',
	'Logic-Subsystem','Integrity','Subsystem','Memory','Comms','Integrity',
	'Checksum','Protocol','Parity','Bus','Timing','Synchronisation','Topology',
	'Transmission','Reception','Stack','Framing','Code','Programming',
	'Peripheral','Environmental','Loading','Operation','Parameter','Syntax',
	'Initialisation','Execution','Resource','Encryption','Decryption','File',
	'Precondition','Authentication','Paging','Swapfile','Service','Gateway',
	'Request','Proxy','Media','Registry','Configuration','Metadata',
	'Streaming','Retrieval','Installation','Library','Handler']
columnC = ['Interruption','Destabilisation','Destruction','Desynchronisation',
	'Failure','Dereferencing','Overflow','Underflow','NMI','Interrupt',
	'Corruption','Anomaly','Seizure','Override','Reclock','Rejection',
	'Invalidation','Halt','Exhaustion','Infection','Incompatibility',
	'Timeout','Expiry','Unavailability','Bug','Condition','Crash','Dump',
	'Crashdump','Stackdump','Problem','Lockout']
columnD = ['Error','Problem','Warning','Signal','Flag']
```


```python
from random import randint

bofhExcuse = columnA[randint(0,len(columnA)-1)]+' '
bofhExcuse += columnB[randint(0,len(columnB)-1)]+' '
bofhExcuse += columnC[randint(0,len(columnC)-1)]+' '
if(randint(0,100) > 80):
	bofhExcuse += columnD[randint(0,len(columnD)-1)]
print 'Today\'s issue is: '+bofhExcuse
```

    Today's issue is: Duplicated Proxy Overflow
