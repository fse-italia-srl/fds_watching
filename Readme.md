Questo scritp in Python consente di lanciare da un server Windows remoto una simulazione FDS (https://pages.nist.gov/fds-smv/downloads.html) e controllare l'output che lo stesso FDS produce. 
Lo script **fds_watching.py** si preoccuperà di inviare un email al destinatario indicato nel file config.ini con l'esito della simulazione.

Il file **config.ini**

<code>
    [SMTP]<br />
    name_server = smtp.yourprovider.com<br />
    port = 587<br />
    username = yourusername<br />
    password = yourpassword<br />
</code><br />
<code>
    [Sender]<br />
    name = INFO FSE ITALIA<br />
    email = your.email@tua-azienda.com<br />
</code><br />
<code>
    [Destination]<br />
    name = Mario Rossi<br />
    email = mario.rossi@tua-azienda.com<br />
</code><br />
<code>
    [File]<br />
    file_name = Test_T2_20_BD_20_02.fds<br />
    num_core = 6<br />
</code><br />

Alla voce *[SMTP]* si imposta il nome del server SMTP, la porta (587 di default) e le credenziali per poter spedire il messaggio di posta

Alla voce *[Sender]* si indica l'intestazione dell'email di provenienza.

Alla voce *[Destination]* si indica l'email del destinatario

Alla voce *[File]* si indica il file (con il suo percorso) e il numero di core da utilizzare per questa simulazione.

**ATTENZIONE**: sul server Windows deve essere installato FDS (https://pages.nist.gov/fds-smv/downloads.html) e Python3 (https://www.python.org/downloads/)