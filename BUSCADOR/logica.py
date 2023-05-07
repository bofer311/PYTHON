from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de datos para la tabla de personas
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8), unique=True, nullable=False)
    nombre_apellido = db.Column(db.String(80), nullable=False)
    obra_social = db.Column(db.String(80))
    localidad = db.Column(db.String(80))

# Página principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre_apellido = request.form['nombre']
        if dni:
            personas = Persona.query.filter_by(dni=dni).all()
        elif nombre_apellido:
            personas = Persona.query.filter(Persona.nombre_apellido.ilike(f'%{nombre_apellido}%')).all()
        else:
            personas = []
        return render_template('resultados.html', personas=personas)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
