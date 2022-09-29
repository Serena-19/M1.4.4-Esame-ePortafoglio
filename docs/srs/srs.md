### ePortafoglio app
##### ITS ICT - Serena Schincaglia

**VERSION : 1.0**

**Authors**  
Serena Schincaglia


**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
|1.0| 29/09 | Serena Schincaglia | Update lista funzionalità e scenario|
|1.0| 27/09 | Serena Schincaglia | Update Diagramma UML |
|1.0| 25/09 | Serena Schincaglia | Update lista funzionalità e scenario|
|1.0| 22/09 | Serena Schincaglia | Creazione documento srs, update lista attori|

# Table of Contents

1. [User Case](#p1)
	1. [Diagramma](#sp1.1)
	2. [Attori](#sp1.2) 
	3. [Lista Funzionalità](#sp1.3)
2. [Scenari](#p2)
	1. [Login](#sp2.1)
	1.1 [Autenticazione](#sp2.1.1)
	2. [Creare profili clienti](#sp2.2)
	3. [Aprire conto corrente](#sp2.3)
	4. [Chiudere conto corrente](#sp2.4)
	5. [](#sp2.5)
	6. [](#sp2.6)
	7. [](#sp2.7)
	8. [](#sp2.8)
	9. [](#sp2.9)
	10. [](#sp2.10)
	11. [](#sp2.11)
	12. [](#sp2.12)
	13. [](#sp2.13)
	14. [](#sp2.14)
	15. [](#sp2.15)
	16. [](#sp2.16)
	17. [](#sp2.17)
	18. [](#sp2.18)
	19. [](#sp2.19)
	20. [](#sp2.20)
	21. [](#sp2.21)
	22. [](#sp2.22)

<a name="p1"></a>

## 1. User Case

<a name="sp1.1"></a>

### 1.1 Diagramma

![Diagramma UML] https://github.com/Serena-19/M1.4.4-Esame-ePortafoglio/blob/main/docs/srs/imgs/ePortafoglio%20-%20Esame.png

<a name="sp1.2"></a>

### 1.2 Attori

| Nome | Descrizione |
| ----------- | ----------- | 
|Cliente| Utente con un conto corrente presso Narizzano SPA |
|Cliente Terzo| Utente che ha operazioni di trasferimento di denaro con un cliente di Narizzano SPA |
|Impiegato| Utente che crea, cancella e blocca conti correnti e può eseguire operazioni |
|Amministrazione| Utente generale dell'amministrazione che crea conti correnti, gestisce i profili degl altri utenti e ne gestisce le info uniche |

<a name="sp1.3"></a>

### 1.3 Lista e Funzionalità 
| ID | Nome | Descrizione |
| ----------- | ----------- | ----------- | 
| 1 | Login | L'utente accede con credenziali valide al sistema |
| 1.1 | Autenticazione | L'utente riceve un certificato |
| 2 | Creare profili clienti  |
| 3 |  Aprire conto corrente  |
| 4 | Chiudere conto corrente |
| 5 | Bloccare conto corrente | 
| 6 | Modificare dati anagrafici cliente |
| 7 |  | 
| 8 |  |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |
| 17 |  |
| 18 |  |
| 19 |  |
| 20 |  |
| 21 |  |
| 22 |  |  

<a name="p2"></a>

## Scenari

<a name="sp2.1"></a>

### 2.1 Login

| ID: 1 | <u>Login</u> |
| ----------- | ----------- | 
| Attore | Cliente, Impiegato , Amministrazione |
| Tipo | Primario | 
| Precondizione | L'utente ha delle credenziali uniche e personali valide per il sistema |
| Scenario Principale | |
| 1. | L'utente inserisce la sua ID |
| 2. | L'utente inserisce la password |
| 3. | Il Sistema conferma che che la combinazione delle credenziali è valida e corrisponde ad un utente | 
| 4. | Il sistema scarica o aggiorna il certificato di autenticazione |
| Postcondizione: | L'utente ha accesso al sistema |
| 3a | Scenario Alternativo: Autneticazione non valida |
| 1. | Il sistema segnala che non esiste un account per l'ID inserito |
| 2. | Il sistema suggerisce di contattare l'Amministrazione per la creazione di un account |
| 3. | Il sistema ritorna al punto 1 principale |
| 3b | Scenario Alternativo: L'utente inserisce la password non corretta < 3 volte |
| 1. | Il sistema notifica che la password non è valida e invita a digitarla di nuovo |
| 2. | Il sistema incrementa il counter dei fallimenti |
| 3. | Il sistema torna al punto 2 principale |
| 3c | Scenario Alternativo: L'utente inserisce la password non valide per la terza volta |
| 1. | Il sistema notifica che la password è errata per la terza volta |
| 2. | Il sistema blocca l'account e invia una mail di sblocco all'utente |
| 3. | Il sistema invita l'utente ad aggiornare la password dalla mail |

<a name ="sp2.1.1"></a>

| ID: 1.1 | Autenticazione |
| ----------- | ----------- | 
| Attore | Cliente, Impiegato e Amministratore (Principale) |
| Tipo | Primario | 
| Precondizione | avere un certificato valido |
| Scenario Principale | |
| 1. | Il sistema controlla che la password ed ID siano valide e corrispondano ad un utente |
| 2. | Il sistema autentica le credenziali |
| 3. | Il sistema rilascia o aggiorna il certificato di autenticazione |
| Postcondizione: | L'utente è autentificato |
|| Scenario Alternativo: Certificato Scaduto |
|| Scenario Alternativo: Certificato Non Valido |


<a name="sp2.2"></a>

### 2.2 Creare profili clienti

| ID: 2 | <b> creare profili clienti</b> |
| ----------- | ----------- | 
| Attore | Amministrazione, cliente (secondario) |
| Tipo | primario  |
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai conti |
| Scenario Principale | |
| 1. | L'utente sceglie l'opzione "crea nuovo profilo" |
| 2. | L'utente inserisce i dati nel form apparso |
| 3. | L'utente salva le informazioni |
| 4. | Il Sistema notifica la creazione del profilo |
| 5. | Il Sistema invia una messaggio al cliente proprietario del profilo |
| Postcondizione | Il cliente ha un profilo |

<a name="sp2.3"></a>

### 2.3 Aprire conto corrente

| ID: 3 | <b> aprire un conto corrente</b> |
| ----------- | ----------- | 
| Attore | Amministrazione, cliente , impiegato  |
| Tipo | primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai conti |
| Scenario Principale | |
| 1. | L'utente sceglie l'opzione "crea nuovo conto" |
| 2. | L'utente seleziona il profilo del cliente |
| 3. | L'utente salva le informazioni |
| 4. | Il sistema genera un codice univoco |
| 5. | Il Sistema notifica la creazione del conto |
| 6. | Il Sistema invia una messaggio al cliente proprietario del conto |
| Postcondizione | Il conto è stato creato |

<a name="sp2.4"></a>

### 2.4 Chiudere conto corrente

| ID: 4 | <b> Chiudere conto corrente</b> |
| ----------- | ----------- | 
| Attore | Amministrazione, cliente, impiegato  |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai conti |
| Scenario Principale | |
| 1. | L'utente sceglie l'opzione "elimina conto" |
| 2. | L'utente seleziona il conto del cliente |
| 3. | L'utente salva le informazioni |
| 4. | Il Sistema notifica l'eliminazione del conto |
| 5. | Il Sistema invia una messaggio al cliente proprietario del conto |
| Postcondizione | Il conto è stato eliminato |

<a name="sp2.5"></a>

### 2.5 Bloccare conto corrente 

| ID: 5 | <b> bloccare conto corrente </b> |
| ----------- | ----------- | 
| Attore | amministrazione, impiegato  |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai conti |
| Scenario Principale | |
| 1. | L'utente sceglie l'opzione "blocca conto" |
| 2. | L'utente seleziona il conto del cliente |
| 3. | L'utente salva le informazioni |
| 4. | Il Sistema notifica l'eliminazione del conto |
| 5. | Il Sistema invia una messaggio al cliente proprietario del conto |
| Postcondizione | Il conto è stato eliminato |



<a name="sp2.6"></a>

### 2.6 

<a name="sp2.7"></a>

### 2.7 

<a name="sp2.8"></a>

### 2.8

<a name="sp2.9"></a>

### 2.9 

<a name="sp2.10"></a>

### 2.10 

<a name="sp2.11"></a>

### 2.11

<a name="sp2.12"></a>

### 2.12 

<a name="sp2.13"></a>

### 2.13 

<a name="sp2.14"></a>

### 2.14 
<a name="sp2.15"></a>

### 2.15 
<a name="sp2.16"></a>

### 2.16 

<a name="sp2.17"></a>

### 2.17

<a name="p2.17"></a>

### 2.18 

<a name="p2.18"></a>

### 2.19

<a name="p2.19"></a>

### 2.20 

<a name="p2.20"></a>