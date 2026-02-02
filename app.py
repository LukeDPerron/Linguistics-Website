from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Word Formation Processes
@app.route("/processes")
def processes():
    return render_template("processes.html")

@app.route("/processes/affixation")
def affixation():
    return render_template("affixation.html")

@app.route("/processes/blending")
def blending():
    return render_template("blending.html")

@app.route("/processes/compounding")
def compounding():
    return render_template("compounding.html")

@app.route("/processes/conversion")
def conversion():
    return render_template("conversion.html")

@app.route("/processes/metaphor-metonymy")
def metaphor_metonymy():
    return render_template("metaphor-metonymy.html")

@app.route("/processes/reduplication")
def reduplication():
    return render_template("reduplication.html")

@app.route("/processes/eponymy")
def eponymy():
    return render_template("eponymy.html")

@app.route("/processes/pure-coinage")
def pure_coinage():
    return render_template("pure-coinage.html")

# Working Data Pages
@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/data/affixation")
def affixation_data():
    return render_template("affixation-data.html")

@app.route("/data/blending")
def blending_data():
    return render_template("blending-data.html")

@app.route("/data/compounding")
def compounding_data():
    return render_template("compounding-data.html")

@app.route("/data/conversion")
def conversion_data():
    return render_template("conversion-data.html")

@app.route("/data/metaphor-metonymy")
def metaphor_metonymy_data():
    return render_template("metaphor-metonymy-data.html")

@app.route("/data/reduplication")
def reduplication_data():
    return render_template("reduplication-data.html")

@app.route("/data/eponymy")
def eponymy_data():
    return render_template("eponymy-data.html")

@app.route("/data/pure-coinage")
def pure_coinage_data():
    return render_template("pure-coinage-data.html")

# Theory Page
@app.route("/theory")
def theory():
    return render_template("theory.html")

# Run the App
if __name__ == "__main__":
    app.run(debug=True)
