from src.calc_missing import calc_missing

if __name__ == "__main__":
    readings = []

    # Open and read the file
    with open('data/input002.txt', 'r') as file:
        readings_count = int(file.readline().strip())
        for _ in range(readings_count):
            readings_item = file.readline().strip()
            readings.append(readings_item)

    calc_missing(readings)
