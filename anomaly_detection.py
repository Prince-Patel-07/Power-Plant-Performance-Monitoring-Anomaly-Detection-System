import csv
from statistics import mean, stdev


class AnomalyDetector:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.anomalies = []

    def load_data(self, file_path):
        data = []
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({
                    "timestamp": row["timestamp"],
                    "power_output_mw": float(row["power_output_mw"]),
                    "temperature_c": float(row["temperature_c"]),
                    "pressure_bar": float(row["pressure_bar"]),
                    "vibration_mm_s": float(row["vibration_mm_s"]),
                    "efficiency_percent": float(row["efficiency_percent"])
                })
        return data

    def moving_average(self, values, index):
        if index < self.window_size:
            return mean(values[:index + 1])
        return mean(values[index - self.window_size + 1:index + 1])

    def detect_anomalies(self, data):
        temperatures = [d["temperature_c"] for d in data]
        vibrations = [d["vibration_mm_s"] for d in data]
        efficiencies = [d["efficiency_percent"] for d in data]

        for i, record in enumerate(data):
            temp_ma = self.moving_average(temperatures, i)
            vib_ma = self.moving_average(vibrations, i)

            # ---------- Threshold-based detection ----------
            if record["temperature_c"] > 550:
                self.anomalies.append({
                    "timestamp": record["timestamp"],
                    "parameter": "temperature",
                    "value": record["temperature_c"],
                    "reason": "Temperature exceeded safe threshold"
                })

            if record["vibration_mm_s"] > 3.5:
                self.anomalies.append({
                    "timestamp": record["timestamp"],
                    "parameter": "vibration",
                    "value": record["vibration_mm_s"],
                    "reason": "High vibration level"
                })

            if record["efficiency_percent"] < 32:
                self.anomalies.append({
                    "timestamp": record["timestamp"],
                    "parameter": "efficiency",
                    "value": record["efficiency_percent"],
                    "reason": "Efficiency below expected minimum"
                })

            # ---------- Trend deviation ----------
            if record["temperature_c"] - temp_ma > 15:
                self.anomalies.append({
                    "timestamp": record["timestamp"],
                    "parameter": "temperature",
                    "value": record["temperature_c"],
                    "reason": "Temperature deviating upward from moving average"
                })

            if record["vibration_mm_s"] - vib_ma > 0.5:
                self.anomalies.append({
                    "timestamp": record["timestamp"],
                    "parameter": "vibration",
                    "value": record["vibration_mm_s"],
                    "reason": "Vibration deviating from normal trend"
                })

        # ---------- Standard deviation-based detection ----------
        if len(temperatures) >= 2:
            temp_std = stdev(temperatures)
            temp_avg = mean(temperatures)

            for record in data:
                if abs(record["temperature_c"] - temp_avg) > 2 * temp_std:
                    self.anomalies.append({
                        "timestamp": record["timestamp"],
                        "parameter": "temperature",
                        "value": record["temperature_c"],
                        "reason": "Temperature statistical outlier"
                    })

        return self.anomalies


# ----------------------------
# Standalone execution
# ----------------------------
if __name__ == "__main__":
    detector = AnomalyDetector(window_size=5)

    dataset = detector.load_data("data/simulated_sensor_data.csv")
    anomalies = detector.detect_anomalies(dataset)

    print(f"Total anomalies detected: {len(anomalies)}")
    for a in anomalies[:10]:
        print(a)
