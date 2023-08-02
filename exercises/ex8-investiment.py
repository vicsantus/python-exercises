def final_value(initial_cap, fees, time_in_mounths):
    decimal_fees_tax = fees / 100
    final_value = initial_cap * (1 + decimal_fees_tax) ** time_in_mounths
    return final_value


def make_investiment():
    try:
        initial_cap = float(input("Enter the starting capital: $"))
        fees = float(input("Enter the interest rate (%): "))
        time_in_mounths = int(input("Enter investment time in months: "))

        value = final_value(initial_cap, fees, time_in_mounths)

        print(f"The final investment amount will be: ${value:.2f}")
    except ValueError:
        print("Error: Please enter valid numerical values.")


if __name__ == "__main__":
    make_investiment()
