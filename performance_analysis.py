import csv
from statistics import mean, variance


class PerformanceAnalyzer:
    def load_data(self, file_path):
        data = []
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({
                    "timestamp": row["timestamp"],
                    "power_output_mw": float(row["power_output_mw"]),
                    "efficiency_percent": float(row["efficiency_percent"])
                })
        return data

    def average_power_output(self, data):
        values = [d["power_output_mw"] for d in data]
        return mean(values)

    def capacity_utilization(self, data, max_capacity_mw=1000):
        avg_output = self.average_power_output(data)
        return (avg_output / max_capacity_mw) * 100

    def average_efficiency(self, data):
        efficiencies = [d["efficiency_percent"] for d in data]
        return mean(efficiencies)

    def efficiency_trend(self, data):
        """
        Simple trend:
        Compare first 25% vs last 25% of dataset
        """
        n = len(data)
        if n < 4:
            return 0.0

        early = mean(d["efficiency_percent"] for d in data[: n // 4])
        late = mean(d["efficiency_percent"] for d in data[-n // 4 :])
        return late - early

    def output_variance(self, data):
        values = [d["power_output_mw"] for d in data]
        return variance(values)


# ----------------------------
# Standalone execution
# ----------------------------
if __name__ == "__main__":
    analyzer = PerformanceAnalyzer()

    dataset = analyzer.load_data("data/simulated_sensor_data.csv")

    avg_power = analyzer.average_power_output(dataset)
    capacity = analyzer.capacity_utilization(dataset)
    avg_eff = analyzer.average_efficiency(dataset)
    eff_trend = analyzer.efficiency_trend(dataset)
    stability = analyzer.output_variance(dataset)

    print("----- Performance Summary -----")
    print(f"Average Power Output: {avg_power:.2f} MW")
    print(f"Capacity Utilization: {capacity:.2f} %")
    print(f"Average Efficiency: {avg_eff:.2f} %")

    if eff_trend < 0:
        print(f"Efficiency Trend: {eff_trend:.2f} % (Degrading)")
    else:
        print(f"Efficiency Trend: +{eff_trend:.2f} % (Improving/Stable)")

    print(f"Output Variance (Stability Indicator): {stability:.2f}")
