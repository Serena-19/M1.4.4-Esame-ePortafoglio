
### ePortafoglio app
##### ITS ICT - Serena Schincaglia


**VERSION : 1.0**

**Authors**  
Serena Schincaglia

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| 0.1 | 29/09/2022 | Serena Schincaglia| Update URS document, Functional Requirements |
| 0.1 | 29/09/2022 | Serena Schincaglia | Tests Classi |
| 0.1 | 29/09/2022 | Serena Schincaglia | Creazione classi e relative funzioni |

# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction

<a name="sp1.1"></a>

### 1.1 Document Scope

Questo documento va ad illustrare gli update e i requisiti del progetto "ePortafoglio App" realizzato su commissione dalla azienda Narizzano SPA.


<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym				| Definition | 
| ------------------------------------- | ----------- | 
| XXXX                                  | XXXX |

<a name="sp1.3"></a>

### 1.3 References 

<a name="p2"></a>

## 2. System Description

<a name="sp2.1"></a>

### 2.1 Context and Motivation

Dopo aver esaminato l'offerta di software dedicati alla creazione e gestioni dei conti correnti, Narizzano SPA ha deciso di commissionare la realizzazione di un software proprietario che offrisse opzioni di scalability per il suo numero sempre crescente di clienti.

<a name="sp2.2"></a>

### 2.2 Project Obectives 

<a name="p3"></a>

Il personale amministrativo Narizzano SPA può creare profili unico per ogni cliente che ha un conto nella medesima azienda. L'amministrazione di Narizzano SPA potrà aggiungere o eliminare conti e le varie operazioni con le quali i clienti si interfacceranno tramite browser o app dedicata. 

I clienti di Narizzano SPA potranno eseguire operazzioni come invio e ricevuta di denaro, dalla stessa azienda o da azienda diversa.

I clienti terzi (o aziende terze) come per i clienti potranno eseguire operazioni di trasferimento di denaro 

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders

#### Utenti
| Gruppo | Ruoli | Obiettivo |
| ----------- | ----------- | ----------- |
|Personale Amministrativo Narizzano SPA | Presidente Narizzano SPA, Direttori Dipartimenti, Responsabile immatricolazione Conti, Direzione commerciale, direzione amministrazione e finanza, direzione controllo e recupero, direzione crediti, direzione operativa| Gestire organizzazione di apertura e chiusura conto, depositi e prestiti |
|Personale Informatico Narizzano SPA | Amministratore di Sistema, Manutentore | Poter verificare e modificare le funzionalità e i permessi del sistema |
|Personale Narizzano SPA | Cassiere | Gestisce i conti |
|Clienti | clienti | Gestisce i propri conti correnti, operazioni di trasferimento denaro in entrata e in uscita |
|Clienti terzi | Clienti terzi, aziende terze | Gestisce i propri conti correnti, operazioni di trasferimento denaro in entrata e in uscita |

#### Regolatori
| Gruppo | Ruoli |
| ----------- | ----------- | 
| Ufficio Legale "SaraY" | Soci ufficio legale |

#### Clienti
| Nome | Descrizione |
| ----------- | ----------- | 
| Narizzano SPA | Committente del progetto |

<a name="sp3.2"></a>
### 3.2 Functional Requirements 

#### 3.2.0 Requisiti Generali
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 0.1.0 | Ogni conto ha un codice univoco |M|
| 0.1.1 | Il sistema deve permettere agli utenti di segnalare errori |M|
| 0.1.3 | Esiste una soglia massima di utilizzo di denaro contante (pari a 999,99 euro) |M|

#### 3.2.1 Requisiti Funzionali Amministrazione

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.1.0 | L'amministrazione crea profili clienti |M| 
| 1.1.1 | L'amministrazione può modificare i dati anagrafici dei clienti |M| 
| 1.1.2 | L'amministrazione può bloccare un conto corrente |M|

#### 3.2.2 Requisiti Funzionali Personale

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 2.1.0 | L'impiegato può entrare , tramite credenziali, nel conto del cliente per eseguire operazioni di trasferimento di denaro sotto sua richiesta scritta |M|
| 2.1.1 | L'impiegato può effettuare richieste di prestiti e mutui sotto richiesta scritta del cliente |M|
| 3.2.1 | L'impiegato può aprire un conto corrente per il cliente sotto sua richiesta scritta  |M|
| 3.2.2 | L'impiegato può chiudere un conto corrente per il cliente sotto sua richiesta scritta |M|
| 3.3.0 | L'impiegato può assegnare un libretto di assegni legato a un conto |M|
| 3.3.1 | L'impiegato può assegnare una carta di credito legata a un conto |M| 

#### 3.2.3 Requisiti Funzionali Cliente
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 3.1.0 | Il cliente può, dopo aver eseguito l'accesso, eseguire operazioni di trasferimento di denaro |M|
| 3.2.0 | Il cliente può richiedere la lista movimenti del suo conto dei 30 giorni precedenti |M|
| 3.3.0 | Il cliente può richiedere l'apertura di un mutuo |M|
| 3.3.1 | Il cliente può richiedere l'apertura di un prestito |M|
| 3.4.0 | Il cliente può richiedere una carta di credito collegata al conto |M|
| 3.4.1 | Il cliente può richiedere un libretto di assegni |M|


<a name="sp3.3"></a>
### 3.2 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| R1 | Il software deve essere compatibile con Windows, MACOS, e Linux |M|
| R2 | Il software deve essere accessibile tramite tutti i browser |M|
| R3 | Il software deve essere accessibile tramite app dedicata (Android e IoS) |D|
| R4 | Il software deve rispettare i dettami del GDPR |M|
| R5 | Il software deve appoggiarsi su un database dedicato |M|
| R6 | Il database deve avere back-up bigiornalieri sia in fisico che in cloud ai fini di una veloce disaster recovery |M|
| R7 | Il software deve essere disponibile anche in Inglese |M|
| R8 | Il software deve essere disponibile anche in Francese |D|
| R9 | Il software deve essere disponibile anche in Spagnolo |D|
| R10 | Il software deve essere disponibile anche in Cinese Mandarino |D|
| R11 | Il software deve essere disponibile anche in Spagnolo |O|
| R12 | Il software deve essere disponibile anche in Tedesco|O|
| R13 | Il software deve essere disponibile anche in Arabo |O|
