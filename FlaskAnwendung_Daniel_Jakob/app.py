from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rechner/", methods=['POST'])
def rechner():

    ersteEingabe = request.form['ersteZahl']
    zweiteEingabe = request.form['zweiteZahl']
    rechenoperator = request.form['rechenOperator']

    try:
        ersteZahl = float(ersteEingabe)
        zweiteZahl = float(zweiteEingabe)

        if rechenoperator == "addition":
            ergebnis = ersteZahl + zweiteZahl
        
        elif rechenoperator == "subtraktion":
            ergebnis = ersteZahl - zweiteZahl

        elif rechenoperator == "multiplikation":
            ergebnis = ersteZahl * zweiteZahl

        elif rechenoperator == "division":
            ergebnis = ersteZahl / zweiteZahl

        return render_template(
            'index.html',
            ergebnis=ergebnis,
            rechen_erfolg=True                   
        )
    
    except ZeroDivisionError:

        return render_template(
        'index.html',
        ergebnis="Unmögliche Rechnung",
        rechen_erfolg=False,
        fehler="Es ist nicht möglich durch null zu teilen!"
    )

    except ValueError:

        return render_template(
        'index.html',
        ergebnis="Unmögliche Rechnung",
        rechen_erfolg=False,
        fehler="Die Rechnung ist nicht mit den gegebenen Werten machbar!"
    )

if __name__ == '__main__':
    app.run(debug=True)