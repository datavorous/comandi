# COMANDI v0.0.1 🚀

COMANDI is an AI-powered command-line interface (CLI) tool designed to assist users in converting human instructions into command-line instructions and providing brief hints for programming questions all **WITHOUT ANY API KEY!** 🔑❌

---
<div align="center"> 
<img src="https://raw.githubusercontent.com/datavorous/comandi/main/demo1.gif" alt="demo">
</div>

## ✨ Demo Showcase

### Command-line Instruction Conversion 🌟
COMANDI translates natural language into precise command-line instructions.

<p float="left">
  <img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/1.PNG" width="48%" />
  <img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/4.PNG" width="48%" /> 
</p>

### Programming Hints and Examples 🌟
Get concise programming hints and code snippets for various languages and concepts.

<p float="left">
  <img src="" width="48%" />
  <img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/2.PNG" width="48%" /> 
</p>

## Features 🌟

- 🖥️ **Command-line Instruction Conversion:** Translates human language into precise command-line instructions with descriptions.
- 💡 **Programming Hints:** Provides concise hints for programming problems, along with example code snippets.
- 🎨 **Interactive Interface:** Engages users with an interactive CLI powered by the `rich` library, featuring styled panels and prompts.
- ⚡ **Command Execution:** Offers the ability to execute shell commands directly from the interface and view the output in real-time.
- 🔧 **Configurable Prompt Template:** The prompt template is stored in a JSON file, making it easy to modify and extend.

## Installation 📦

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

## How It Works 🛠️

COMANDI operates in an interactive session where the user inputs either a command-line request or a programming question. The program processes this input through the following steps:

1. **Loading the Prompt Template:**  
   The program reads a prompt template from a `prompt.json` file. This template guides the AI in formulating responses.
2. **User Input Processing:**  
   The user is prompted to enter a request. The input is then passed to the `MetaAI` API using the [meta-ai-api](https://github.com/Strvm/meta-ai-api) library, which generates a response based on the prompt template.
3. **Response Parsing:**  
   The AI response is parsed into different components, including commands, descriptions, hints, and examples. These are then presented to the user in a structured and visually appealing manner.
4. **Command Execution (Optional):**  
   If the AI response includes a command, the user is given the option to execute it directly from the interface. The output is displayed in real-time.

## Usage 🚀

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

## Example Session 💻

```
:: Create a new directory and navigate into it.
🛠️ Command:
mkdir new_directory && cd new_directory
📄 Description:
Creates a new directory named 'new_directory' and then navigates into it.
```

## Technical Details 🔧

- **Language:** Python 3.x
- **Libraries Used:**
  - `rich` for creating a styled CLI interface.
  - `subprocess` for executing shell commands.
  - `json` for handling the prompt template.
  - `meta-ai-api` for AI response generation.

## Prompt Analysis 🔍

The `prompt.json` file contains a crucial template that guides the AI's responses. Let's break it down:

1. **Dual Functionality:** The prompt defines two main tasks for the AI:
   - Converting human instructions to command-line instructions
   - Providing brief hints for programming questions

2. **Response Format:**
   - For command-line instructions:
     ```
     COMMAND: <command-line instruction>
     DESCRIPTION: <brief description of what the command does>
     ```
   - For programming hints:
     ```
     HINT: <one-line programming hint>
     EXAMPLE: <A code snippet showing an implementation of the given problem.>
     ```

3. **Contextual Understanding:** The AI is instructed to determine whether the input is a command-line request or a programming question based on context.

4. **Fallback Mechanism:** If unable to process a command-line instruction, it responds with:
   ```
   COMMAND: UNABLE_TO_PROCESS
   DESCRIPTION: I couldn't generate a command-line instruction for that request.
   ```

5. **Conciseness:** The prompt emphasizes brevity, especially for programming hints, requesting "one-line" tips.

This structured prompt ensures consistent, targeted responses from the AI, enhancing the user experience and maintaining the tool's focus.

## Roadmap 🗺️

Here's our planned roadmap for future COMANDI development:

1. **User Preferences** 🎛️
   - Implement user-specific settings (e.g., preferred shell, programming language)

2. **Command History** 📜
   - Add a feature to save and recall previous commands and responses

3. **Interactive Tutorials** 📚
   - Develop interactive CLI tutorials for various programming concepts and tools

4. **Integration with Version Control Systems** 🔄
    - Add features to interact with git and other VCS directly from COMANDI

## Contributing 🤝

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to this project.

## License 📄

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to [meta-ai-api](https://github.com/Strvm/meta-ai-api) library by [Roméo](https://github.com/Strvm)!
- Special thanks to the creators of the `rich` library for making CLI development visually stunning and accessible.



We're excited about the future of COMANDI and welcome community input on these plans!
