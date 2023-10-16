DROP TABLE IF EXISTS dipendenti;

DROP TABLE IF EXISTS clienti;

DROP TABLE IF EXISTS magazzino;

CREATE TABLE dipendenti (
    id_dipendente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    telefono VARCHAR(10) UNIQUE,
    email UNIQUE,
    mansione TEXT,
    stipendio INT
);

CREATE TABLE clienti (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    telefono VARCHAR(10) UNIQUE,
    email UNIQUE,
    data_ultimo_acquisto date,
    citta TEXT
);

CREATE TABLE magazzino (
    id_prodotto INTEGER PRIMARY KEY AUTOINCREMENT,
    prodotto TEXT,
    prezzo FLOAT, 
    produttore TEXT,
    codice_lotto VARCHAR(6)
);

/*
Inserisco valori astratti all'interno del database dell'azienda
*/

INSERT INTO dipendenti (nome, cognome, telefono, email, mansione, stipendio)
VALUES ("Leonardo", "Rossi", "2982303958", "leonardorossi@mail.com", "Magazzino", 1250),
("Alessandro", "Bianchi", "2485603871", "alessandrobianchi@mail.com", "Programmazione", 1500),
("Tommaso", "Verdi", "1004958673", "tommasoverdi@mail.com", "Marketing e design", 1635),
("Sofia", "Gialli", "1452938475", "sofiagialli@mail.com", "Magazzino", 1200),
("Giulia", "Viola", "1002938445", "giuliaviola@mail.com", "Contabilità", 1660),
("Andrea", "Rosa", "1029384756", "andrearosa@mail.com", "Ufficio impiegati", 1430);

INSERT INTO clienti (nome, cognome, telefono, email, data_ultimo_acquisto, citta)
VALUES ("Francesco", "Piazza", "3022938475", "franscescopaizza@mail.com", "2022-04-21", "Milano"),
("Luigi", "Rossi", "2002893442", "luigirossi@mail.com", "2023-09-13", "Milano"),
("Martina", "Bianchi", "1002938495", "martinabianchi@mail.com", "2023-05-05", "Roma"),
("Federico", "Musica", "4405968443", "federicomusica@mail.com", "2023-06-15", "Bergamo"),
("Giorgio", "Tavolo", "2203945678", "giorgiotavolo@mail.com", "2022-01-09", "Pavia"),
("Marco", "Legna", "6659483912", "marcolegna@mail.com", "2022-11-17", "Roma"),
("Gianna", "Erba", "2039485666", "giannierba@mail.com", "2023-10-16", "Genova"),
("Gianluca", "Verdi", "1230495867", "gianlucaverdi@mail.com", "2023-09-11", "Firenze"),
("Anna", "Ferro", "4405962213", "pieraferro@mail.com", "2022-02-28", "Bologna"),
("Francesca", "Roma", "2239485069", "francescaroma@mail.com", "2023-09-30", "Modena"),
("Lorenzo", "Genova", "3221235798", "lorenzogenova@mail.com", "2021-07-19", "Milano");

INSERT INTO magazzino (prodotto, prezzo, produttore, codice_lotto)
VALUES ("Penna a sfera", 3, "Bic", "C34R11"),
("Penna stilografica", 12, "Ferrari", "F56Y78"),
("Gomma da cancellare", 2, "Bic", "D34I87"),
("Temperino", 4, "Bic", "Q11O00"),
("Pennelli", 15, "Faber Castell", "R45Y67"),
("Zaino", 45, "Eastpack", "C32E99");