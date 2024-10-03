from openai import OpenAI
from colorama import init, Fore

# Replace with your API key
client = OpenAI()

init(autoreset=True)

# Initial system message
messages = [{"role": "system", "content": "You are an assistant running in the user's terminal."}]

print("\nAI started!")

try:
    while True:
        user_input = input("\n> ")

        # Exit the loop if the user types 'exit'
        if user_input.lower() == "exit":
            print("\n\n AI finishing!")
            break

        # Add the user's message to the list of messages
        messages.append({"role": "user", "content": user_input})

        # Create a stream for the AI's response
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True,
        )

        # Display the AI's response as chunks are received
        print("\n", end="")
        full_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            print(Fore.GREEN + content, end="")
            full_response += content

        print()  # New line after the full AI response

        # Add the full AI response to the list of messages for context
        messages.append({"role": "assistant", "content": full_response})

except KeyboardInterrupt:
    print(Fore.RED + "\n\nAI finishing!")