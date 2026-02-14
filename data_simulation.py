import csv
import random
import os
from datetime import datetime, timedelta


class PowerPlantDataSimulator:
    def __init__(self, start_date, periods, frequency="hourly"):
        """
        start_date : datetime object
        periods    : number of data points
        frequency  : 'hourly' or 'daily'
        """
        self.start_date = start_date
        self.periods = periods
        self.frequency = frequency
        self.data = []

    def _next_timestamp(self, current_time):
        if self.frequency == "hourly":
            return current_time + timedelta(hours=1)
        elif self.frequency == "daily":
            return current_time + timedelta(days=1)
        else:
            raise ValueError("Frequency must be 'hourly' or 'daily'")

    def generate_data(self):
        timestamp = self.start_date

        # Base operating conditions
        power_output = random.uniform(700, 900)
        temperature = random.uniform(450, 520)
        pressure = random.uniform(150, 180)
        vibration = random.uniform(1.0, 2.5)
        efficiency = random.uniform(35, 42)

        for _ in range(self.periods):
            power_output += random.uniform(-5, 5)
            temperature += random.uniform(-2, 2)
            pressure += random.uniform(-1.5, 1.5)
            vibration += random.uniform(-0.05, 0.05)
            efficiency += random.uniform(-0.1, 0.1)

            power_output = max(400, min(1000, power_output))
            temperature = max(250, min(600, temperature))
            pressure = max(100, min(220, pressure))
            vibration = max(0.5, min(5.0, vibration))
            efficiency = max(30, min(45, efficiency))

            self.data.append({
                "timestamp": timestamp,
                "power_output_mw": round(power_output, 2),
                "temperature_c": round(temperature, 2),
                "pressure_bar": round(pressure, 2),
                "vibration_mm_s": round(vibration, 3),
                "efficiency_percent": round(efficiency, 2)
            })

            timestamp = self._next_timestamp(timestamp)

        return self.data

    def export_to_csv(self, file_path):
        if not self.data:
            raise RuntimeError("No data generated. Call generate_data() first.")

        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            for row in self.data:
                writer.writerow(row)

        print(f"Data successfully exported to {file_path}")


# ----------------------------
# Standalone execution
# ----------------------------
if __name__ == "__main__":
    simulator = PowerPlantDataSimulator(
        start_date=datetime(2025, 1, 1, 0, 0),
        periods=168,
        frequency="hourly"
    )

    simulator.generate_data()
    simulator.export_to_csv("data/simulated_sensor_data.csv")
