def prompt_user():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print(user_input)

# Call the function
prompt_user()

