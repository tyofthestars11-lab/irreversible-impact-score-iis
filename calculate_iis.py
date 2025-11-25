# Quantum Content Generation Protocol - Irreversible Impact Score Calculator
"""
Irreversible Impact Score (IIS)

IIS = (rate / principal) * 100

Notes:
- principal: positive number (dollars)
- rate: either a decimal (e.g. 0.08 for 8%) or a percentage value (e.g. 8 for 8%).
  The function will assume a value > 1 is a percent and normalize it (divide by 100).
  You can override this behavior via the rate_is_percent parameter.
- The higher the IIS, the higher the priority according to this metric.
- If your goal is to minimize absolute interest paid fastest, consider using
  annual interest = principal * rate (this ranks by dollars of interest per year).
"""

from typing import Optional
import argparse
import sys


def _normalize_rate(rate: float) -> float:
    """Normalize rate so it is a decimal (e.g., 0.08 for 8%)."""
    if rate < 0:
        raise ValueError("Rate must be non-negative.")
    # Heuristic: if rate > 1, assume it's given as a percentage (e.g., 8)
    if rate > 1:
        return rate / 100.0
    return rate


def calculate_iis(principal: float, rate: float, rate_is_percent: Optional[bool] = None) -> float:
    """
    Calculate the Irreversible Impact Score (IIS).

    Args:
        principal: principal amount (must be > 0).
        rate: interest rate, either decimal (0.08) or percent (8).
        rate_is_percent: if True, treat `rate` as percent and divide by 100;
                         if False, treat `rate` as decimal;
                         if None (default), use heuristic to normalize.

    Returns:
        IIS as a float.

    Raises:
        ValueError for invalid inputs.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if rate <= 0:
        raise ValueError("Rate must be greater than zero.")

    if rate_is_percent is True:
        r = rate / 100.0
    elif rate_is_percent is False:
        r = rate
    else:
        r = _normalize_rate(rate)

    # IIS definition (keeps your original formula)
    iis_score = (r / principal) * 100.0
    return iis_score


def _format_currency(amount: float) -> str:
    return f"${amount:,.2f}"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculate Irreversible Impact Score (IIS) for debts.")
    parser.add_argument("--principal", "-p", type=float, required=False, help="Principal amount (e.g. 25000)")
    parser.add_argument("--rate", "-r", type=float, required=False, help="Interest rate (decimal 0.08 or percent 8)")
    parser.add_argument("--percent", action="store_true",
                        help="Interpret the provided rate as a percent (e.g. 8 for 8%). If omitted, heuristic is used.")
    parser.add_argument("--examples", action="store_true", help="Run built-in debt examples and exit.")
    args = parser.parse_args(argv)

    try:
        if args.examples:
            # Built-in examples
            debt_a_principal = 25000.00
            debt_a_rate = 0.045  # 4.5% decimal
            debt_b_principal = 2500.00
            debt_b_rate = 0.12   # 12% decimal

            iis_a = calculate_iis(debt_a_principal, debt_a_rate)
            iis_b = calculate_iis(debt_b_principal, debt_b_rate)

            print("--- IIS CALCULATION PROTOCOL ENGAGED (EXAMPLES) ---")
            print(f"Debt A (P: {_format_currency(debt_a_principal)} | R: {debt_a_rate*100:.2f}%) -> IIS: {iis_a:.6f}")
            print(f"Debt B (P: {_format_currency(debt_b_principal)} | R: {debt_b_rate*100:.2f}%) -> IIS: {iis_b:.6f}")

            if iis_a > iis_b:
                print("\nDECISION: Attack Debt A (Higher IIS) first for MAXIMUM impact.")
            else:
                print("\nDECISION: Attack Debt B (Higher IIS) first for MAXIMUM impact.")
            return 0

        if args.principal is None or args.rate is None:
            parser.error("Either --examples or both --principal and --rate must be provided.")

        iis = calculate_iis(args.principal, args.rate, rate_is_percent=args.percent)
        print("--- IIS CALCULATION PROTOCOL ENGAGED ---")
        print(f"Debt (P: {_format_currency(args.principal)} | R: {args.rate}{'%' if args.percent else ''}) -> IIS: {iis:.6f}")
        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
