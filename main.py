import csv
import os
import blessed

def openConversation(conversationName: str, reverse=True) -> list:
    tempList = []
    with open(f"./conversations/{conversationName}.csv", newline='', encoding="UTF-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tempList.append([row[0],row[1],row[2]])
    if reverse: tempList.reverse()
    return tempList

def displayConversations(term: blessed.Terminal, convos: list) -> None:
    lettersAmount = len(convos)
    counter = 0
    newline_raw_literal = '\\n'
    newline = '\n'
    for context, authour, date in convos:
        counter+=1
        clearTerminal()
        with term.location(0,0) and term.cbreak():
            print(f"{context.replace(newline_raw_literal, newline)}\n\n- {authour} : {date}", end="")
            print("\n\nPress ENTER to go to next letter..." if counter < lettersAmount else "\n\nYou have reached the end, press ENTER to exit...")
            val = term.inkey(timeout=2)
            while val.code != 343:
                val = term.inkey(timeout=2)
                pass
    clearTerminal()

def getConversations() -> list:
    return [i.replace(".csv", "") for i in os.listdir("./conversations")]

def getConversationChoice(conversationList: list) -> int:
    index = 1
    for i in conversationList:
        print(f"{index}. {i}")
        index+=1
    while True:
        try:
            userInput = int(input("Enter the number of conversation you want to display: "))
            if userInput > 0 and userInput < len(conversationList)+1:
                return userInput-1
            else:
                print("Invalid input. ",end="")
        except ValueError:
            print("Invalid input. ",end="")

def printFromStart(term: blessed.Terminal, content: str, end="\n", clear=True) -> None:
    if clear: clearTerminal()
    with term.location(0,0):
        print(content, end=end)

def clearTerminal() -> None:
    os.system("cls")

def main():
    terminal = blessed.Terminal()
    printFromStart(terminal, "Hello")
    conversations = getConversations()
    convoIndex = getConversationChoice(conversations)
    data = openConversation(conversations[convoIndex])
    displayConversations(terminal, data)

if __name__ == "__main__":
    main()