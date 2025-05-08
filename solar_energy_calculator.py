import matplotlib.pyplot as plt

# Average sunlight hours per month (example data)
sunlight_hours = [5.5, 6.0, 7.0, 8.5, 9.0, 9.5, 9.0, 8.5, 7.5, 6.0, 5.0, 4.5]

# Get user input
panel_area = float(input("Enter solar panel area (m²): "))
efficiency = float(input("Enter solar panel efficiency (0-1): "))

# Calculate monthly energy (assuming 1kW/m² solar irradiance)
monthly_energy = []
for hours in sunlight_hours:
    energy = panel_area * 1 * efficiency * hours * 30  # 30 days in month
    monthly_energy.append(energy)

# Print energy output
for i, energy in enumerate(monthly_energy):
    print(f"Month {i+1}: Estimated energy = {energy:.2f} kWh")

# Plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.bar(months, monthly_energy)
plt.title('Estimated Solar Energy Production (Monthly)')
plt.xlabel('Month')
plt.ylabel('Energy (kWh)')
plt.savefig('solar_energy_chart.png')
print("Chart saved as 'solar_energy_chart.png'")
plt.show()