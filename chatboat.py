import datetime
import re
import os

def is_valid_list_input(user_input):
    return re.fullmatch(r'\d+(,\s*\d+)*', user_input) is not None

def is_valid_range_input(user_input):
    return re.fullmatch(r'\d+,\s*\d+', user_input) is not None

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def chatbot():
    chat_history = []
    command_count = {}
    print("Chatbot: Hello! I’m your assistant! How can I help you today?")
    chat_history.append("Chatbot: Hello! I’m your assistant! How can I help you today?")
    
    while True:
        user_input = input("User: ").strip().lower()
        chat_history.append(f"User: {user_input}")
        
        if user_input == "hi" or user_input == "hello":
            print("Chatbot: Hi there! How can I help you today?")
            chat_history.append("Chatbot: Hi there! How can I help you today?")
        
        elif  "date" in user_input:
            now = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")
            print(f"Chatbot: {now}")
            chat_history.append(f"Chatbot: {now}")
        
        elif  'time' in user_input:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: {now}")
            chat_history.append(f"Chatbot: {now}")
        
        elif user_input == "list operations":
            print("Chatbot: Please enter a list of integers (comma-separated, integer):")
            chat_history.append("Chatbot: Please enter a list of integers (comma-separated, integer):")
            list_input = input("User: ")
            chat_history.append(f"User: {list_input}")
            
            if not is_valid_list_input(list_input):
                print("Chatbot: Error! The input must be a comma-separated list of integers.")
                chat_history.append("Chatbot: Error! The input must be a comma-separated list of integers.")
                continue
            
            num_list = list(map(int, list_input.split(',')))
            print(f"Chatbot:\n  Sum: {sum(num_list)}\n  Maximum: {max(num_list)}\n  Reversed List: {list(reversed(num_list))}")
            chat_history.append(f"Chatbot:\n  Sum: {sum(num_list)}\n  Maximum: {max(num_list)}\n  Reversed List: {list(reversed(num_list))}")
            
            print("Chatbot: Would you like to remove duplicates? (yes/no)")
            chat_history.append("Chatbot: Would you like to remove duplicates? (yes/no)")
            user_choice = input("User: ")
            chat_history.append(f"User: {user_choice}")
            
            if user_choice == "yes":
                num_list = sorted(set(num_list))
                print(f"Chatbot: Updated List: {num_list}")
                chat_history.append(f"Chatbot: Updated List: {num_list}")
            
        elif user_input == "generate prime":
            print("Chatbot: Enter the range (start and end):")
            chat_history.append("Chatbot: Enter the range (start and end):")
            range_input = input("User: ")
            chat_history.append(f"User: {range_input}")
            
            if not is_valid_range_input(range_input):
                print("Chatbot: Error! The input must be two comma-separated integers.")
                chat_history.append("Chatbot: Error! The input must be two comma-separated integers.")
                continue
            
            start, end = map(int, range_input.split(','))
            primes = generate_primes(start, end)
            print(f"Chatbot: Prime Numbers: {primes}")
            chat_history.append(f"Chatbot: Prime Numbers: {primes}")
            
        elif user_input == "search history":
            print("Chatbot: Enter the keyword to search in chat history:")
            chat_history.append("Chatbot: Enter the keyword to search in chat history:")
            keyword = input("User: ")
            chat_history.append(f"User: {keyword}")
            
            matches = [line for line in chat_history if keyword in line]
            print("Chatbot: Found the following lines:")
            chat_history.append("Chatbot: Found the following lines:")
            for match in matches:
                print(f"  - {match}")
                chat_history.append(f"  - {match}")
            
        elif user_input == "bye":
            print("Chatbot: Here’s a summary of your session:")
            chat_history.append("Chatbot: Here’s a summary of your session:")
            
            command_counts = {}
            for entry in chat_history:
                if "User:" in entry:
                    command = entry.replace("User: ", "").strip()
                    command_counts[command] = command_counts.get(command, 0) + 1
            
            most_frequent_command = max(command_counts, key=command_counts.get, default="None")
            print(f"  - Commands Used: {len(command_counts)}")
            print(f"  - Most Frequent Command: {most_frequent_command}")
            chat_history.append(f"  - Commands Used: {len(command_counts)}")
            chat_history.append(f"  - Most Frequent Command: {most_frequent_command}")
            
            print("Chatbot: Do you want to save this summary? (yes/no)")
            chat_history.append("Chatbot: Do you want to save this summary? (yes/no)")
            save_choice = input("User: ")
            chat_history.append(f"User: {save_choice}")
            
            if save_choice == "yes":
                filename = f"summary_{datetime.datetime.now().strftime('%d%m%Y')}.txt"
                filepath = os.path.join(os.path.expanduser("~"), "Desktop", filename)
                with open(filepath, "w") as file:
                    file.write("\n".join(chat_history))
                print(f"Chatbot: Summary saved to {filename} (saved on Desktop)")
                chat_history.append(f"Chatbot: Summary saved to {filename} (saved on Desktop)")
            
            print("Chatbot: Bye, have a good day!!")
            chat_history.append("Chatbot: Bye, have a good day!!")
            break
        
        else:
            print("Chatbot: Enter correct keyword")
            chat_history.append("Chatbot: Enter correct keyword")

if __name__ == "__main__":
    chatbot()
