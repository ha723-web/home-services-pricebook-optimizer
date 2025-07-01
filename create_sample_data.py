import pandas as pd

data = [
    ["Furnace Repair", "HVAC", 120, 60, 250],
    ["Air Conditioner Installation", "HVAC", 200, 180, 520],
    ["Thermostat Replacement", "HVAC", 50, 60, 145],
    ["Leak Detection", "Plumbing", 90, 30, 180],
    ["Water Heater Replacement", "Plumbing", 160, 100, 380],
    ["Toilet Repair", "Plumbing", 60, 25, 140],
    ["Garbage Disposal Installation", "Plumbing", 80, 55, 180],
    ["Electrical Panel Upgrade", "Electrical", 180, 90, 400],
    ["Ceiling Fan Installation", "Electrical", 70, 40, 150],
    ["Light Fixture Installation", "Electrical", 65, 35, 130],
]

df = pd.DataFrame(data, columns=["Service", "Category", "Labor Cost", "Material Cost", "Price"])
df.to_csv("data/home_services_data.csv", index=False)
print("✅ Dataset created successfully!")
