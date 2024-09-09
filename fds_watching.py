import subprocess
import smtplib
import configparser
import socket

## Trovo l'indirizzo IP della macchina
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])

config = configparser.ConfigParser()
 
# Read the configuration file
config.read('config.ini')

# Access values from the configuration file
name_server = config.get('SMTP', 'name_server')
port = config.get('SMTP', 'port')
username = config.get('SMTP', 'username')
password = config.get('SMTP', 'password')
sender = config.get('Sender', 'name')
email_sender = config.get('Sender', 'email')
dest = config.get('Destination', 'name')
email = config.get('Destination', 'email')
nome_server = s.getsockname()[0]
nome_file = config.get('File', 'file_name')
num_core = config.get('File', 'num_core')

## Imposta alcune variabili per l'invio della email
sent_subject = f"Questa e-mail ti consente di sapere come sta andando la tua simulazione su {nome_server}!"
sent_from = f"{sender} <{email_sender}>"
sent_to = [email]


# Esegui il comando FDS e cattura l'output
myprocess = subprocess.run(
    [r"fds_local.bat", "-p", num_core, "-o", "1", "-Y", nome_file],
    text=True
)

# Intercetta l'output e l'errore
output = myprocess.stdout
errors = myprocess.stderr

# Stampa a video l'output e gli eventuali errori
print("Output:")
print(output)
print("Errors:")
print(errors)



## Queste istruzioni consentono di intercettare la risposta dell'output di FDS
if str(output).find("STOP: FDS completed successfully"):
    print("FDS completed successfully!")
    msg = "FDS completed successfully!"
elif str(output).find("ERROR: Numerical Instability - FDS stopped"):
    print("Numerical Instability!")
    msg = "Numerical Instability!"
elif str(output).find("STOP: FDS stopped by user"):
    print("FDS stopped by user!")
    msg = "FDS stopped by user!"
elif str(output).find("ERROR: FDS was improperly set-up - FDS stopped"):
    print("FDS was improperly set-up - FDS stopped!")
    msg = "FDS was improperly set-up - FDS stopped!"    
elif str(output).find("STOP: Set-up only"):
    print("Set-up only!")
    msg = "Set-up only!"      
elif str(output).find("STOP: FDS was stopped by KILL control function and completed successfully"):
    print("FDS was stopped by KILL control function and completed successfully!")
    msg = "FDS was stopped by KILL control function and completed successfully!"   
elif str(output).find("STOP: FDS performed a TGA analysis only and finished successfully"):
    print("FDS performed a TGA analysis only and finished successfully!")
    msg = "FDS performed a TGA analysis only and finished successfully!"   
elif str(output).find("STOP: FDS performed a level set analysis only and finished successfully"):
    print("FDS performed a level set analysis only and finished successfully!")
    msg = "FDS performed a level set analysis only and finished successfully!"   
elif str(output).find("ERROR: Unrealizable mass density - FDS stopped"):
    print("Unrealizable mass density!")
    msg = "Unrealizable mass density!"                   
else:
    print("Errore nell'esecuzione del programma!")
    msg = "Errore nell'esecuzione del programma!"


## Questo è il testo dell'e-mail
email_text = """\
From: %s
To: %s
Subject: %s

Ciao %s\nSpero che tu stia bene!\n
Ti comunico l'esito della tua simulazione FDS di %s,\n
[%s]\n
Lo Staff di\n FSE Italia Srl\n
""" % (sent_from, ", ".join(sent_to), sent_subject, dest, nome_file, msg)




server = smtplib.SMTP(name_server, int(port))
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.set_debuglevel(1)  ## Questa istruzione consente di visualizzare l'esito dell'invio dell'e-mail

## Questa istruzione invia l'email a fine lavoro e il metodo 'quite()' chiude la connessione al server di posta in uscita
server.sendmail(sent_from, sent_to, email_text)
server.quit()