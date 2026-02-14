import csv
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

sns.set(style="whitegrid")  # Clean plotting style

# ----------------------------
# Load Data
# ----------------------------
def load_data(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "timestamp": datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S"),
                "power_output_mw": float(row["power_output_mw"]),
                "temperature_c": float(row["temperature_c"]),
                "pressure_bar": float(row["pressure_bar"]),
                "vibration_mm_s": float(row["vibration_mm_s"]),
                "efficiency_percent": float(row["efficiency_percent"])
            })
    return data

# ----------------------------
# Plot Time Series
# ----------------------------
def plot_time_series(data):
    timestamps = [d["timestamp"] for d in data]
    
    # Power Output
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, [d["power_output_mw"] for d in data], label="Power Output (MW)", color='blue')
    plt.xlabel("Time")
    plt.ylabel("MW")
    plt.title("Power Output Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_output_over_time.png")
    plt.show()
    
    # Temperature
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, [d["temperature_c"] for d in data], label="Temperature (°C)", color='red')
    plt.xlabel("Time")
    plt.ylabel("°C")
    plt.title("Turbine Temperature Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("temperature_over_time.png")
    plt.show()
    
    # Efficiency
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, [d["efficiency_percent"] for d in data], label="Efficiency (%)", color='green')
    plt.xlabel("Time")
    plt.ylabel("%")
    plt.title("Efficiency Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("efficiency_over_time.png")
    plt.show()

# ----------------------------
# Distribution Plots
# ----------------------------
def plot_distribution(data):
    plt.figure(figsize=(8, 4))
    sns.histplot([d["power_output_mw"] for d in data], bins=20, kde=True, color='blue')
    plt.title("Distribution of Power Output")
    plt.xlabel("MW")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("power_output_distribution.png")
    plt.show()
    
    plt.figure(figsize=(8, 4))
    sns.histplot([d["efficiency_percent"] for d in data], bins=20, kde=True, color='green')
    plt.title("Distribution of Efficiency")
    plt.xlabel("%")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("efficiency_distribution.png")
    plt.show()

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    dataset = load_data("data/simulated_sensor_data.csv")
    plot_time_series(dataset)
    plot_distribution(dataset)
    print("Visualization completed. Plots saved as PNG files.")
