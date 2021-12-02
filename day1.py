"""
Measure how many measurenents are larger than the previous day measurement.
"""

def main():

    with open("day1_input.txt", "r") as measurements:
        input_measurements = [int(measurement) for measurement in measurements.readlines()]

    count = 0
    for next_idx, curr_measurement in enumerate(input_measurements, start=1):
        if next_idx == 2000:
            break
        next_measurement = input_measurements[next_idx]
        if next_measurement - curr_measurement > 0:
            count += 1

    print(f"Number of increased measurements is: {count} ")


if __name__ == "__main__":
    main()


