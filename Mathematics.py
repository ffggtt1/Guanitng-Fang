import random

# easy question
def math_arithmetic():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    symbol = random.choice(['+', '-', '*'])
    if symbol == '+':
        return f"{num1} + {num2}", num1 + num2
    elif symbol == '-':
        return f"{num1} - {num2}", num1 - num2
    else:
        return f"{num1} * {num2}", num1 * num2

# medium question
def math_algebra():
    x = random.randint(1, 30)
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    c = a * x + b
    return f"Solve for x: {a}x + {b} = {c}", x

# difficulty question
def math_statistics():
    data = [random.randint(1, 30) for _ in range(3)]
    mean = round(sum(data) / len(data))
    return f"What is the mean of {data}?", mean

# select question based on topic
def math_question(topic):
    if topic == '1':
        return math_arithmetic()
    elif topic == '2':
        return math_algebra()
    elif topic == '3':
        return math_statistics()
    else:
        return math_arithmetic()

# ask a question and check answer
def ask_question(player_name, topic):
    question, answer = math_question(topic)
    print(f"\n{player_name}, your question is:\n{question}")
    try:
        guess = int(input("Your answer: "))
        if guess == answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong. The correct answer is {answer}.")
    except:
        print("Invalid input. That counts as wrong.")
    return False

# topic selection
def choose_topic():
    print("\nChoose a topic:")
    print("1. Arithmetic (easy)")
    print("2. Algebra (medium)")
    print("3. Statistics (hard)")
    topic = input("Enter 1 / 2 / 3: ").strip()
    if topic not in ['1', '2', '3']:
        print("Invalid choice. Using default: Arithmetic.")
        topic = '1'
    return topic

# main game
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
