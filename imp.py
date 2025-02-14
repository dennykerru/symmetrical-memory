import matplotlib.pyplot as diagram  # Renamed plt to diagram

# Function to generate Fibonacci sequence up to 'n' terms
def fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Function to display the Fibonacci sequence
def display_fibonacci(sequence):
    print("Fibonacci Numbers:", sequence)

# Function to visualize the Fibonacci sequence
def visualize_fibonacci(sequence):
    diagram.plot(sequence, marker='s', color='green', linestyle='--', markersize=6)
    diagram.title('Fibonacci Visualization')
    diagram.xlabel('Index')
    diagram.ylabel('Value')
    diagram.grid(True)
    diagram.show()

# Main function
def main():
    num = 12  # Change this to generate more or fewer numbers
    fib_numbers = fibonacci_sequence(num)
    
    display_fibonacci(fib_numbers)
    visualize_fibonacci(fib_numbers)

if __name__ == "__main__":
    main()