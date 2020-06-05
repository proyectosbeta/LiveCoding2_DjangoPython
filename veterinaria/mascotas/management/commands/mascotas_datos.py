from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from mascotas.models import Mascota, Vacuna
from pytz import UTC

DATETIME_FORMAT = '%m/%d/%Y %H:%M'

NOMBRES_VACUNAS = [
    'Parvo canino',
    'Moquillo canino',
    'Rabia canina',
    'Leptospira canina',
    'Herpes felina Virus 1',
    'Rabia felina',
    'Leucemia felina'
]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Cargando datos desde mascotas_datos.csv..."

    def handle(self, *args, **options):
        if Vacuna.objects.exists() or Mascota.objects.exists():
            print('Datos ya están...existiendo.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creando datos de vacunas")
        for nombre_vacuna in NOMBRES_VACUNAS:
            vac = Vacuna(nombre=nombre_vacuna)
            vac.save()
        print("Cargando datos de mascotas")
        for row in DictReader(open('./mascotas_datos.csv')):
            pet = Mascota()
            pet.nombre = row['Nombre']
            pet.doctor = row['Doctor']
            pet.especie = row['Especie']
            pet.raza = row['Raza']
            pet.descripcion = row['Descripcion']
            pet.sexo = row['Sexo']
            pet.edad = row['Edad']
            raw_fecha = row['Fecha']
            fecha = UTC.localize(
                datetime.strptime(raw_fecha, DATETIME_FORMAT))
            pet.fecha = fecha
            pet.save()
            raw_vacunas = row['Vacunas']
            nombre_vacunas = [name for name in raw_vacunas.split('| ') if name]
            for vac_name in nombre_vacunas:
                vac = Vacuna.objects.get(nombre=vac_name)
                pet.vacunas.add(vac)
            pet.save()
