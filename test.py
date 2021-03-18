states = ['CA', 'PA', 'MA', 'NJ']

with open('new.csv', 'w') as csv_file:
    for state in states:
        csv_file.write(state + '\n')