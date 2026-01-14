

def kbc():

  #questions with correct nswer at the end of list
    questions = [
    ["Who is the current president of USA?", "Obama", "Trump", "Biden", "Harris", "Trump"],
    ["Where was the 2022 football World Cup held?", "Nepal", "India", "Qatar", "USA", "Qatar"],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "Mars"],
    ["Which language is primarily used for Android app development?", "Python", "Java", "C++", "Ruby", "Java"],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "Madrid", "Paris"],
    ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Dickens", "Tolkien", "Austen", "Shakespeare"],
    ["What is 9 * 8?", "72", "81", "64", "69", "72"],
    ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "Blue Whale"],
    ["Which is the fastest land animal?", "Cheetah", "Lion", "Tiger", "Leopard", "Cheetah"]
]
    
    prize = 0

    for i in range(0,10):
        print(f"{i+1} {questions[i][0]}") #asking questions one by one
        answer = input().title()
        if answer == questions[i][5]:
            prize+=1000
            print("Correct answer")
        else:
            print(f"Wrong answer")
            break 
    print(f"You have won Rs {prize}")        


kbc()            