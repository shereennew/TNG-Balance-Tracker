PIN_FILE = "pin.txt"

def set_pin():
    pin = input("Set a 4-digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        with open(PIN_FILE, "w") as f:
            f.write(pin)
        print("✅ PIN has been set successfully.")
    else:
        print("❌ Invalid PIN. Must be exactly 4 digits.")

def verify_pin():
    try:
        with open(PIN_FILE, "r") as f:
            saved_pin = f.read().strip()
    except FileNotFoundError:
        print("⚠️ No PIN set. Please set one first.")
        return False

    entered_pin = input("Enter your PIN: ")
    if entered_pin == saved_pin:
        print("✅ PIN verified.")
        return True
    else:
        print("❌ Incorrect PIN.")
        return False

def change_pin():
    # First check the old PIN
    try:
        with open(PIN_FILE, "r") as f:
            saved_pin = f.read().strip()
    except FileNotFoundError:
        print("⚠️ No PIN set. Please set one first with set_pin().")
        return

    old_pin = input("Enter your current PIN: ")
    if old_pin != saved_pin:
        print("❌ Incorrect PIN. Cannot change.")
        return

    new_pin = input("Enter new 4-digit PIN: ")
    if new_pin.isdigit() and len(new_pin) == 4:
        with open(PIN_FILE, "w") as f:
            f.write(new_pin)
        print("✅ PIN has been changed successfully.")
    else:
        print("❌ Invalid PIN. Must be exactly 4 digits.")
