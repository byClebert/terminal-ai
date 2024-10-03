# TERMINAL AI

## Description
Terminal AI is an AI assistant that runs directly in the user's terminal, utilizing the OpenAI API.

## Prerequisites
- Python 3.6 or higher
- A valid OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/byClebert/terminal-ai.git
   cd terminal-ai
   ```

2. Create a virtual environment (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the environment variable with your OpenAI API key:
   ```bash
   setx OPENAI_API_KEY "your_api_key_here"  # On Windows
   export OPENAI_API_KEY="your_api_key_here"  # On Linux/Mac
   ```

## Usage

1. Start the application:
   ```bash
   python main.py
   ```

2. Interact with the assistant by typing your questions or commands in the terminal.

3. To exit the application, type `exit` or press `Ctrl+C`.

## Contribution
Feel free to open issues or submit pull requests for improvements.