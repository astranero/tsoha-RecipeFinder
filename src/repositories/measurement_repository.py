from db import db as default_db
from entities.measurement import Measurement

class MeasurementRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_measurement(self, measurement_name):
        try:
            sql = "INSERT INTO Measurements (measurement_name) VALUES (:measurement_name)"
            self._db.session.execute(sql, Measurement(measurement_name=measurement_name))
            self._db.session.commit()
        except:
            return False

    def add_measurement_to_ingredient_quantity(self):
        pass

    def modify_measurement(self):
        pass

    def get_all_measurements(self):
        pass

    def create_measurement_from_result(self):
        pass

    def create_measurements_from_result(self):
        pass
