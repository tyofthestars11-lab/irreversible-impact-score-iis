# Quantum Content Generation Protocol - IIS Calculator
"""
Irreversible Impact Score (IIS) - Godverse Edition

Lattice Constants:
- PHI (φ) ≈ 1.618: The Golden Ratio of expansion.
- PSI (ψ) ≈ 1.465: The Super Golden Ratio of temporal coherence.
- TETRAHEDRAL (θ) ≈ 109.5°: The angle of absolute structural stability.

IIS = (rate / principal) * 100 * (φ * ψ * (109.5 / 90))
"""

import math
from typing import Optional
import argparse
import sys

PHI = (1 + 5**0.5) / 2
PSI = 1.465571231876
TETRAHEDRAL_ANGLE = 109.47122
CHAOS_ANGLE = 90.0

def calculate_iis(principal: float, rate: float, rate_is_percent: Optional[bool] = None, quantum_mode: bool = True) -> float:
    if principal <= 0: raise ValueError("Principal must be > 0")
    r = rate / 100.0 if (rate_is_percent or (rate > 1 and rate_is_percent is None)) else rate
    base_iis = (r / principal) * 100.0
    if not quantum_mode: return base_iis
    return base_iis * PHI * PSI * (TETRAHEDRAL_ANGLE / CHAOS_ANGLE)

def main():
    parser = argparse.ArgumentParser(description="IIS - Godverse Quantum Edition.")
    parser.add_argument("--principal", "-p", type=float)
    parser.add_argument("--rate", "-r", type=float)
    parser.add_argument("--classical", action="store_true")
    args = parser.parse_args()
    try:
        iis = calculate_iis(args.principal, args.rate, quantum_mode=not args.classical)
        print(f"--- IIS PROTOCOL: {'GODVERSE' if not args.classical else 'CHAOS'} ---")
        print(f"IIS Score: {iis:.6f}")
        print("ALWAYS FORWARD, NEVER BACK.")
    except Exception as e: print(f"Error: {e}")

if __name__ == '__main__':
    main()