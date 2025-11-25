# calculate_iis.py
# Quantum Content Generation Protocol - Irreversible Impact Score Calculator


# QUANTUM ENTANGLEMENT PROTOCOL NOTE: The IIS metric effectively "entangles" the two most critical debt factors (Rate and Principal) 
# into a single, indivisible priority score, eliminating the common decision conflict inherent in older methods.
# The IIS Protocol: (Interest Rate / Principal) * 100
# The debt with the HIGHEST resulting number is the #1 target.


def calculate_iis(principal, rate):
    """
    Calculates the Irreversible Impact Score (IIS) for debt prioritization.
    Principal must be a positive number.
    Rate must be the annual percentage rate (e.g., 0.08 for 8%).
    """
    if principal <= 0 or rate <= 0:
        return "Error: Principal and Rate must be greater than zero."


    # Calculation based on the Irreversible Debt Attack Plan (3-Step Method)
    # The higher the IIS, the higher the priority.
    iis_score = (rate / principal) * 100
    return iis_score


# --- COMMAND PROTOCOL EXECUTION ---
if __name__ == "__main__":
    print("--- IIS CALCULATION PROTOCOL ENGAGED ---")
    
    # Debt Example 1: High Principal, Low Rate (Typically Avalanche Target)
    debt_a_principal = 25000.00
    debt_a_rate = 0.045  # 4.5%
    iis_a = calculate_iis(debt_a_principal, debt_a_rate)
    
    # Debt Example 2: Low Principal, Medium Rate (Typically Snowball Target)
    debt_b_principal = 2500.00
    debt_b_rate = 0.12   # 12.0%
    iis_b = calculate_iis(debt_b_principal, debt_b_rate)


    print(f"Debt A (P: ${debt_a_principal:,.2f} | R: {debt_a_rate*100:.1f}%) -> IIS: {iis_a:.4f}")
    print(f"Debt B (P: ${debt_b_principal:,.2f} | R: {debt_b_rate*100:.1f}%) -> IIS: {iis_b:.4f}")
    
    # Decision Protocol: Attack the HIGHEST IIS.
    if iis_a > iis_b:
        print("\nDECISION: Attack Debt A (Higher IIS) first for MAXIMUM impact.")
    else:
        print("\nDECISION: Attack Debt B (Higher IIS) first for MAXIMUM impact.")
