with open('SampleData.csv', mode='r') as file:
    processed_data = []

    for line in file:
        # print(repr(line))
        row = line.strip()
        print(row)
