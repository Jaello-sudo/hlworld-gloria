def calc_speed():
    d = float(input("Enter distance (meters): "))
    t = float(input("Enter time (seconds): "))
    if t == 0:
        print("Error: time cannot be zero.\n")
        return
    print(f"Speed = {d/t} m/s\n")

def calc_force():
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    print(f"Force = {m*a} N\n")

def calc_ke():
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    print(f"Kinetic Energy = {0.5*m*v*v} J\n")

def calc_voltage():
    i = float(input("Enter current (A): "))
    r = float(input("Enter resistance (Ω): "))
    print(f"Voltage = {i*r} V\n")

def calc_density():
    m = float(input("Enter mass (kg): "))
    vol = float(input("Enter volume (m³): "))
    if vol == 0:
        print("Error: volume cannot be zero.\n")
        return
    print(f"Density = {m/vol} kg/m³\n")


formulas = {
    "1": ("Speed (v = d / t)", calc_speed),
    "2": ("Force (F = m × a)", calc_force),
    "3": ("Kinetic Energy (KE = 1/2 m v²)", calc_ke),
    "4": ("Ohm's Law (V = I × R)", calc_voltage),
    "5": ("Density (ρ = m / V)", calc_density),
    "6": ("Exit", None)
}


print("=== PHYSICS FORMULA CALCULATOR ===")

while True:
    print("\nSelect a formula:")
    for key, value in formulas.items():
        print(f"{key}. {value[0]}")

    choice = input("\nEnter choice: ")

    if choice == "6":
        print("Goodbye!")
        break

    if choice in formulas:
        print(f"\n--- {formulas[choice][0]} ---")
        formulas[choice][1]()  # call the associated function
    else:
        print("Invalid choice. Try again.\n")
