import random

# Create a basic arithmetic question
def math_arithmetic():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    op = random.choice(['+', '-', '*'])
    if op == '+':
        return f"{num1} + {num2}", num1 + num2
    elif op == '-':
        return f"{num1} - {num2}", num1 - num2
    else:
        return f"{num1} * {num2}", num1 * num2

# Create an algebra question
def math_algebra():
    x = random.randint(1, 30)
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    c = a * x + b
    return f"Solve for x: {a}x + {b} = {c}", x

# Create a statistics question (mean)
def math_statistics():
    data = [random.randint(1, 30) for _ in range(3)]
    mean = sum(data) // len(data)
    return f"What is the mean of {data}?", mean

# Select question based on topic
def math_question(topic):
    if topic == '1':
        return math_arithmetic()
    elif topic == '2':
        return math_algebra()
    elif topic == '3':
        return math_statistics()
    else:
        return math_arithmetic()

# Ask a question and check answer
def ask_question(player_name, topic):
    question, answer = math_question(topic)
    print(f"\n{player_name}, your question is: {question}")
    try:
        guess = int(input("Your answer: "))
        if guess == answer:
            print("Correct!")
            return True
        else:
            print(f"Incorrect. The correct answer is {answer}.")
            return False
    except ValueError:
        print("Invalid input. You get a wrong answer.")
        return False

# Topic selection menu
def choose_topic():
    print("\nSelect a topic for this game:")
    print("1. Arithmetic (easy)")
    print("2. Algebra (medium)")
    print("3. Statistics (hard)")
    topic = input("Enter 1 / 2 / 3: ").strip()
    return topic if topic in ['1', '2', '3'] else '1'

# Main game
def main():
    print("Welcome to the Math Quiz Challenge!")
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    topic = choose_topic()

    scores = {player1: 0, player2: 0}
    turn = 0
    winner = None

    while not winner:
        current_player = player1 if turn % 2 == 0 else player2
        correct = ask_question(current_player, topic)
        if correct:
            scores[current_player] += 1

        print(f"Current scores - {player1}: {scores[player1]} | {player2}: {scores[player2]}")

        if scores[current_player] >= 3:
            winner = current_player
        turn += 1

    print(f"\n{winner} wins the game! Congratulations!")

if __name__ == "__main__":
    main()
