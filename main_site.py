from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dipendenti")
def dipendenti():
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    dipendenti = connection.execute("SELECT * FROM dipendenti").fetchall()
    connection.close()
    return render_template("dipendenti.html", dipendenti=dipendenti)

@app.route("/dipendenti/<int:id_dipendente>/delete", methods=("POST",))
def dipendenti_delete(id_dipendente):
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    connection.execute("DELETE FROM dipendenti WHERE id_dipendente=?", (id_dipendente,))
    connection.commit()
    connection.close()
    return redirect("/dipendenti")

@app.route("/clienti")
def clienti():
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    clienti = connection.execute("SELECT * FROM clienti").fetchall()
    connection.close()
    return render_template("clienti.html", clienti=clienti)

@app.route("/clienti/<int:id_cliente>/delete", methods=("POST",))
def clienti_delete(id_cliente):
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    connection.execute("DELETE FROM clienti WHERE id_cliente=?", (id_cliente,))
    connection.commit()
    connection.close()
    return redirect("/clienti")

@app.route("/magazzino")
def magazzino():
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    magazzino = connection.execute("SELECT * FROM magazzino").fetchall()
    connection.close()
    return render_template("magazzino.html", magazzino=magazzino)

@app.route("/magazzino/<int:id_prodotto>/delete", methods=("POST",))
def magazzino_delete(id_prodotto):
    connection = sqlite3.connect("database_azienda.db")
    connection.row_factory = sqlite3.Row
    connection.execute("DELETE FROM magazzino WHERE id_prodotto=?", (id_prodotto,))
    connection.commit()
    connection.close()
    return redirect("/magazzino")

@app.route("/dipendenti_aggiungi", methods=("POST","GET"))
def dipendenti_aggiungi():
    if request.method == "POST":
        nome = request.form['nome']
        cognome = request.form['cognome']
        telefono = request.form['telefono']
        email = request.form['email']
        mansione = request.form['mansione']
        stipendio = request.form['stipendio']
        connection = sqlite3.connect("database_azienda.db")
        connection.row_factory = sqlite3.Row
        connection.execute("INSERT INTO dipendenti (nome, cognome, telefono, email, mansione, stipendio) VALUES (?, ?, ?, ?, ?, ?)", (nome, cognome, telefono, email, mansione, stipendio))
        connection.commit()
        connection.close()
        return redirect("/dipendenti")
    return render_template("dipendenti_aggiungi.html")

@app.route("/clienti_aggiungi", methods=("POST","GET"))
def clienti_aggiungi():
    if request.method == "POST":
        nome = request.form['nome']
        cognome = request.form['cognome']
        telefono = request.form['telefono']
        email = request.form['email']
        data_ultimo_acquisto = request.form['data_ultimo_acquisto']
        citta = request.form['citta']
        connection = sqlite3.connect("database_azienda.db")
        connection.row_factory = sqlite3.Row
        connection.execute("INSERT INTO clienti (nome, cognome, telefono, email, data_ultimo_acquisto, citta) VALUES (?, ?, ?, ?, ?, ?)", (nome, cognome, telefono, email, data_ultimo_acquisto, citta))
        connection.commit()
        connection.close()
        return redirect("/clienti")
    return render_template("clienti_aggiungi.html")

@app.route("/magazzino_aggiungi", methods=("POST","GET"))
def magazzino_aggiungi():
    if request.method == "POST":
        prodotto = request.form['prodotto']
        prezzo = request.form['prezzo']
        produttore = request.form['produttore']
        codice_lotto = request.form['codice_lotto']
        connection = sqlite3.connect("database_azienda.db")
        connection.row_factory = sqlite3.Row
        connection.execute("INSERT INTO magazzino (prodotto, prezzo, produttore, codice_lotto) VALUES (?, ?, ?, ?)", (prodotto, prezzo, produttore, codice_lotto))
        connection.commit()
        connection.close()
        return redirect("/magazzino")
    return render_template("magazzino_aggiungi.html")

app.run("0.0.0.0", port=80)