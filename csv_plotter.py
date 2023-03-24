import csv
import matplotlib.pyplot as plt

def plot_data(filename):
    x_values = []
    y_values = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip header row
        for row in reader:
            try:
                x = float(row[0])
                y = float(row[1])
                x_values.append(x)
                y_values.append(y)
            except:
                pass

    plt.plot(x_values, y_values)
    plt.title('Data Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    filename = input("Enter CSV file name: ")
    plot_data(filename)
