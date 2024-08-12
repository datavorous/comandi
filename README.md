<div align="center"> 
   
# COMANDI v0.0.1

</div>

COMANDI is an AI powered command-line interface (CLI) tool designed to assist users in converting human instructions into command-line instructions and providing brief hints for programming questions all **WITHOUT ANY API KEY!**

---

<div align="center"> 
<img src="https://raw.githubusercontent.com/datavorous/comandi/main/demo1.gif" alt="demo">
</div>

## Features

- **Command-line Instruction Conversion:** Translates human language into precise command-line instructions with descriptions.
- **Programming Hints:** Provides concise hints for programming problems, along with example code snippets.
- **Interactive Interface:** Engages users with an interactive CLI powered by the `rich` library, featuring styled panels and prompts.
- **Command Execution:** Offers the ability to execute shell commands directly from the interface and view the output in real-time.
- **Configurable Prompt Template:** The prompt template is stored in a JSON file, making it easy to modify and extend.

## Installation

To install and run COMANDI, ensure you have Python 3.x installed, then follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/datavorous/comandi.git
   cd comandi
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## How It Works

COMANDI operates in an interactive session where the user inputs either a command-line request or a programming question. The program processes this input through the following steps:

1. **Loading the Prompt Template:**  
   The program reads a prompt template from a `prompt.json` file. This template guides the AI in formulating responses.

2. **User Input Processing:**  
   The user is prompted to enter a request. The input is then passed to the `MetaAI` API using the [meta-ai-api](https://github.com/Strvm/meta-ai-api) library, which generates a response based on the prompt template.

3. **Response Parsing:**  
   The AI response is parsed into different components, including commands, descriptions, hints, and examples. These are then presented to the user in a structured and visually appealing manner.

4. **Command Execution (Optional):**  
   If the AI response includes a command, the user is given the option to execute it directly from the interface. The output is displayed in real-time.

## Usage

- **Command-line Instruction:**  
  Enter a request like:
  ```
  Create a new directory and navigate into it.
  ```
  The program will generate the corresponding command and description.

- **Programming Hint:**  
  Ask a programming question, such as:
  ```
  How do I sort a list in Python?
  ```
  COMANDI will provide a brief hint and a code snippet.

- **Exiting the Program:**  
  Type `quit` or `exit` to end the session.

## Example Session

```
:: Create a new directory and navigate into it.
🛠️ Command:
mkdir new_directory && cd new_directory

📄 Description:
Creates a new directory named 'new_directory' and then navigates into it.
```

## Technical Details

- **Language:** Python 3.x
- **Libraries Used:**
  - `rich` for creating a styled CLI interface.
  - `subprocess` for executing shell commands.
  - `json` for handling the prompt template.
  - `meta-ai-api` for AI response generation.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to this project.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [meta-ai-api](https://github.com/Strvm/meta-ai-api) library by [Roméo](https://github.com/Strvm)!
- Special thanks to the creators of the `rich` library for making CLI development visually stunning and accessible. 
