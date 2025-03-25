import random

def guessingGame():
    decision = input("Would you like to play a number guessing game (y/n)?: ")

    if decision.lower() in ["y", "yes"]:
        username = input("What is your username?: ")
        print("Here are the rules of the game:")
        print("Difficulty Levels: Easy (0 to 10), Intermediate (0 to 15), or Difficult (0 to 20)")
        print("Try to guess the correct number to gain points!")

        while True:
            difficultyChoice = input("What difficulty level would you like (Easy, Intermediate, or Difficult)?: ").lower()
            if difficultyChoice == "easy":
                difficulty = 0
                rangeEnd = 10
                break
            elif difficultyChoice == "intermediate":
                difficulty = 1
                rangeEnd = 15
                break
            elif difficultyChoice == "difficult":
                difficulty = 2
                rangeEnd = 20
                break
            else:
                print("Please use a valid difficulty level.")

        multiplier = [10000, 15000, 20000]
        correctAnswers = 0

        while True:
            numberToGuess = random.randrange(0, rangeEnd)
            guess = int(input(f"What is your guess (0 to {rangeEnd})?: "))

            if numberToGuess == guess:
                correctAnswers += 1
                decision = input("Congrats you win! Would you like to play again (y/n)?: ")
            else:
                decision = input(f"I'm sorry you lost, the answer was: {numberToGuess}. Would you like to play again (y/n)?: ")

            if decision.lower() not in ["y", "yes"]:
                score = correctAnswers * multiplier[difficulty]
                print(f"Thank you for playing {username}! Your score is {score}.")
                
                try:
                    with open("Leaderboard.txt", "r") as file:
                        entries = [line.strip() for line in file if line.strip()]
                except FileNotFoundError:
                    entries = []
                
                updated = False
                newEntries = []
                for entry in entries:
                    parts = entry.split(", ")
                    entryUsername = parts[0].split(": ")[1]
                    oldScore = int(parts[1].split(": ")[1])
                    if entryUsername.lower() == username.lower():
                        if oldScore > score:
                            newEntries.append(entry)
                        else: 
                            newEntries.append(f"Username: {username}, Score: {score}")
                        updated = True
                    else:
                        newEntries.append(entry)
                
                if not updated:
                    newEntries.append(f"Username: {username}, Score: {score}")
                
                with open("Leaderboard.txt", "w") as file:
                    file.write("\n".join(newEntries) + "\n")
                
                sortLeaderboard()
                break

def sortLeaderboard():
    try:
        with open("Leaderboard.txt", "r") as file:
            entries = [line.strip() for line in file if line.strip()]
        
        leaderboard = []
        for entry in entries:
            parts = entry.split(", ")
            username = parts[0].split(": ")[1]
            score = parts[1].split(": ")[1]
            leaderboard.append({
                'username': username,
                'score': int(score),
                'raw': entry
            })
        
        leaderboard.sort(key=lambda x: x['username'].lower())
        
        with open("Leaderboard.txt", "w") as file:
            for entry in leaderboard:
                file.write(entry['raw'] + "\n")
                
    except FileNotFoundError:
        print("Leaderboard file not found. Creating a new one.")
        open("Leaderboard.txt", "w").close()

guessingGame()