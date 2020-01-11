#!/usr/bin/env python3

import mysql.connector
import datetime

class DBConnector:
    def __init__(self, host, database, user, password):
        self.connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database, auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.prepare()

    def prepare(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS records (" +
            "id INT NOT NULL AUTO_INCREMENT," +
            "datetime                   DATETIME UNIQUE," +
            "outside_temperature        DECIMAL(5,1)," +
            "high_out_temperature       DECIMAL(5,1)," +
            "low_out_temperature        DECIMAL(5,1)," +
            "rainfall                   SMALLINT UNSIGNED," +
            "high_rain_rate             SMALLINT UNSIGNED," +
            "barometer                  DECIMAL(5,3) UNSIGNED," +
            "solar_radiation            SMALLINT UNSIGNED," +
            "number_of_wind_samples     SMALLINT UNSIGNED," +
            "inside_temperature         DECIMAL(5,1)," +
            "inside_humidity            TINYINT UNSIGNED," +
            "outside_humidity           TINYINT UNSIGNED," +
            "average_wind_speed         TINYINT UNSIGNED," +
            "high_wind_speed            TINYINT UNSIGNED," +
            "direction_of_hi_wind_speed ENUM('N', 'NNE', 'NE', 'NEE', 'E', 'SEE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'SWW', 'W', 'NWW', 'NW', 'NNW')," +
            "prevailing_wind_direction  ENUM('N', 'NNE', 'NE', 'NEE', 'E', 'SEE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'SWW', 'W', 'NWW', 'NW', 'NNW')," +
            "average_uv                 DECIMAL(3,1) UNSIGNED," +
            "et                         DECIMAL(3,3) UNSIGNED," +
            "high_solar_radiation       SMALLINT UNSIGNED," +
            "high_uv                    TINYINT UNSIGNED," +
            "forecast_rule              TINYINT UNSIGNED," +
            "leaf_temperature1          SMALLINT," +
            "leaf_temperature2          SMALLINT," +
            "leaf_wetnesses1            TINYINT UNSIGNED," + 
            "leaf_wetnesses2            TINYINT UNSIGNED," +
            "soil_temperatures1         SMALLINT," +
            "soil_temperatures2         SMALLINT," +
            "soil_temperatures3         SMALLINT," +
            "soil_temperatures4         SMALLINT," +
            "extra_humidity1            TINYINT UNSIGNED," +
            "extra_humidity2            TINYINT UNSIGNED," +
            "extra_temperature1         SMALLINT," +
            "extra_temperature2         SMALLINT," +
            "extra_temperature3         SMALLINT," +
            "soil_moisture1             TINYINT UNSIGNED," +
            "soil_moisture2             TINYINT UNSIGNED," +
            "soil_moisture3             TINYINT UNSIGNED," +
            "soil_moisture4             TINYINT UNSIGNED," +
            "PRIMARY KEY(id))"
        )

    def destroy(self):
        self.cursor.execute("DROP TABLE IF EXISTS records")

    def get_last_date(self):
        self.cursor.execute("SELECT MAX(datetime) AS last FROM records")
        result = self.cursor.fetchone()
        last = result["last"]
        if last is None:
            return datetime.datetime.strptime("2003-06-06 09:30:00", "%Y-%m-%d %H:%M:%S")
        else:
            return last

    def save_data(self, data):
        allowed_fields = {
                          "datetime": "datetime",
                          "outside_temperature": "outside_temperature",
                          "high_out_temperature": "high_out_temperature",
                          "low_out_temperature": "low_out_temperature",
                          "rainfall": "rainfall",
                          "high_rain_rate": "high_rain_rate",
                          "barometer": "barometer",
                          "solar_radiation": "solar_radiation",
                          "number_of_wind_samples": "number_of_wind_samples",
                          "inside_temperature": "inside_temperature",
                          "inside_humidity": "inside_humidity",
                          "outside_humidity": "outside_humidity",
                          "average_wind_speed": "average_wind_speed",
                          "high_wind_speed": "high_wind_speed",
                          "direction_of_hi_wind_speed": "direction_of_hi_wind_speed",
                          "prevailing_wind_direction": "prevailing_wind_direction",
                          "average_uv": "average_uv",
                          "et": "et",
                          "high_solar_radiation": "high_solar_radiation",
                          "high_uv": "high_uv",
                          "forecast_rule": "forecast_rule",
                          "leaf_temperature1": "leaf_temperature1",
                          "leaf_temperature2": "leaf_temperature2",
                          "leaf_wetnesses1": "leaf_wetnesses1",
                          "leaf_wetnesses2": "leaf_wetnesses2",
                          "soil_temperatures1": "soil_temperatures1",
                          "soil_temperatures2": "soil_temperatures2",
                          "soil_temperatures3": "soil_temperatures3",
                          "soil_temperatures4": "soil_temperatures4",
                          "extra_humidity1": "extra_humidity1",
                          "extra_humidity2": "extra_humidity2",
                          "extra_temperature1": "extra_temperature1",
                          "extra_temperature2": "extra_temperature2",
                          "extra_temperature3": "extra_temperature3",
                          "soil_moisture1": "soil_moisture1",
                          "soil_moisture2": "soil_moisture2",
                          "soil_moisture3": "soil_moisture3",
                          "soil_moisture4": "soil_moisture4",
                         }

        for record in data:
            actual_fields = {}
            for key in record:
                if key in allowed_fields:
                    field = record[key]
                    if type(field) is datetime.datetime:
                        field = field.strftime("%Y-%m-%d %H:%M:%S")
                    if not type(field) is str:
                        field = str(field)
                    actual_fields[allowed_fields[key]] = field

            separator = ','

            fields = list(map(lambda x: "`" + str(x) + "`", actual_fields))
            insert_fields = separator.join(fields)

            values = list(map(lambda x: "'" + actual_fields[x] + "'", actual_fields))
            insert_values = separator.join(values)

            query = "INSERT INTO records(" + insert_fields + ") VALUES (" + insert_values + ")"
            self.cursor.execute(query)
            self.connection.commit()
