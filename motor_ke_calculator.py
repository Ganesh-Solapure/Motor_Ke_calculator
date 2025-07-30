def calculate_rpm_and_ke():
    try:

        freq = float(input("Enter frequency observed in DSO (Hz): "))
        poles = int(input("Enter number of motor poles: "))
        vrms = float(input("Enter Vrms from DSO (V): "))

        rpm = (120 * freq) / poles

        ke = (vrms * 1000) / rpm

        print("\n--- Calculated Results ---")
        print(f"Motor RPM: {rpm:.2f} RPM")
        print(f"Back EMF Constant Ke: {ke:.2f} V/krpm")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_rpm_and_ke()
