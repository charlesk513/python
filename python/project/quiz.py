score = 0
print("\nWelcome to Kc computer science quiz.\n")

name = input("Enter your name, please  ")

print("1. Python programming language was created by?")
print("A. Charles Babbage")
print("B. Guido Van Rossum")
print("C. Ada B Loverace")
print("D. Dennis Ricchie\n")
answer = input("Enter your answer: ")
correct = 'B'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")
    
print("2. Which level of programming language is python?")
print("A. Low level")
print("B. Mid level")
print("C. High level")
print("D. None of the above\n")
answer = input("Enter your answer: ")
correct = 'C'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")

print("3. What is the memory hierachy in ascending order of speed?")
print("A. Main memory, cache, secondary memory, registers")
print("B. cache, main memory, registers, secondary memory")
print("C. register, cache, main memory, secondary memory")
print("D. secondary memory, main memory, cache, registers\n")
answer = input("Enter your answer: ")
correct = 'C'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")
    
print("4. Who among the personnel of political economy invented capitalism?")
print("A. Karl Marx")
print("B. Adam Smith")
print("C. Maynard Keynes")
print("D. John Stuart Mills\n")
answer = input("Enter your answer: ")
correct = 'B'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")

print("5. What is the order of Kotlers communication model?")
print("A. Sender, Decoder, media, Encoder, Receiver")
print("B. Sender, media, Encoder, Receiver, Decoder")
print("C. Encoder, Sender, media, Receiver, Decoder")
print("D. Sender, Encoder, media, Decoder, Receiver\n")
answer = input("Enter your answer: ")
correct = 'D'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")
    
print("6. What are the different ways of proving expressions in discrete?")
print("A. Counterexample, Direct, contrapositive, induction")
print("B. Direct, counterexample, Probability, approximation")
print("C. Probability, Direct, Contradiction, Counterexample")
print("D. Approximation, Induction, Counterexample, Probability\n")
answer = input("Enter your answer: ")
correct = 'A'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")

print("7. What in of the following python containers represent a list?")
print("A. { 1:'age', 3.6:'Float', 'Joy':name}")
print("B. ( 1, 3.6, 'Joy', (1, 5), 'Name')")
print("C. { 1, 3.6, 'Joy', (1, 5), 'Name'}")
print("D. [ 1, 3.6, 'Joy', (1, 5), 'Name']\n")
answer = input("Enter your answer: ")
correct = 'D'
if answer.upper() == correct:
    print("Correct!")
    score += 1
else:
    print(f"Wrong option!, the correct answer is {correct}")
    
mark = round((score/7)*100, 2)
print(f"The overall mark scored by {name} is {score}/7, which is {mark}%. Congs")

