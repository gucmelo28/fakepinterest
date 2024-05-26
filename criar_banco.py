from fakepint import database, app
from fakepint.models import Usuario, Foto

with app.app_context():
    database.create_all()