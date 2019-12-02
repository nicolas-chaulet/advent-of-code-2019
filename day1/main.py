import numpy as np

MODULES=np.loadtxt('input.txt')

def get_fuel(mass):
    return np.max(np.floor(mass / 3) -2 , 0)

def get_total_fuel(module_mass):
    total_fuel = 0
    additional_fuel = get_fuel(module_mass)
    while additional_fuel > 0:
        total_fuel += additional_fuel
        additional_fuel = get_fuel(additional_fuel)
    return total_fuel

def main():
    aggr = 0
    for module in MODULES:
        aggr += get_total_fuel(module)
    print(aggr)


if __name__ == "__main__":
    main()