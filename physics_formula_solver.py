def physics_calculator():
    while True:
        print("\n" + "=" * 35)
        print("      PHYSICS FORMULA SOLVER")
        print("=" * 35)
        print("1. Momentum (p = m × v)")
        print("2. Work Done (W = F × d)")
        print("3. Power (P = W / t)")
        print("4. Wave Speed (v = f × λ)")
        print("5. Pressure (P = F / A)")
        
        choice = input("\nSelect a formula (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Calculating Momentum (p = m × v) ---")
            m = float(input("Enter mass (m in kg): "))
            v = float(input("Enter velocity (v in m/s): "))
            p = m * v
            print(f"Result: Momentum = {p:.2f} kg·m/s")
            
        elif choice == '2':
            print("\n--- Calculating Work Done (W = F × d) ---")
            f = float(input("Enter force (F in Newtons): "))
            d = float(input("Enter distance (d in meters): "))
            w = f * d
            print(f"Result: Work Done = {w:.2f} Joules")
            
        elif choice == '3':
            print("\n--- Calculating Power (P = W / t) ---")
            w = float(input("Enter work done (W in Joules): "))
            t = float(input("Enter time (t in seconds): "))
            if t == 0:
                print("Error: Time cannot be zero.")
            else:
                p_val = w / t
                print(f"Result: Power = {p_val:.2f} Watts")
                
        elif choice == '4':
            print("\n--- Calculating Wave Speed (v = f × λ) ---")
            f_freq = float(input("Enter frequency (f in Hz): "))
            lam = float(input("Enter wavelength (λ in meters): "))
            v_wave = f_freq * lam
            print(f"Result: Wave Speed = {v_wave:.2f} m/s")
            
        elif choice == '5':
            print("\n--- Calculating Pressure (P = F / A) ---")
            f_force = float(input("Enter force (F in Newtons): "))
            a = float(input("Enter area (A in m²): "))
            if a == 0:
                print("Error: Area cannot be zero.")
            else:
                pressure = f_force / a
                print(f"Result: Pressure = {pressure:.2f} Pascals")
                
        else:
            print("Invalid choice! Please select a number between 1 and 5.")
            
        # Prompt to continue or exit
        cont = input("\nDo you want to continue? (y/n): ").strip().lower()
        if cont not in ['y', 'yes']:
            print("\nExiting program. Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    physics_calculator()
