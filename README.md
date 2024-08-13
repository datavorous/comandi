<div align="center">

<img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/favicon.png" alt="Logo" width="128" height="128">  

# COMANDI v0.0.2 🚀

Free API-Keyless AI-powered CLI for Programming Support, Error Debugging and Automated Instruction Translations. 

![Python version](https://img.shields.io/badge/python-3.10%2B-blue)
</div>

## ✨ Demo Showcase

<div align="center"> 
   
<img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/pair_programming.gif" alt="debugging code using it" width="80%">  <br>
   <b>👨‍💻 Fix your code and understand the errors, from the comfort of your terminal!</b><br><br>
   
<img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/cmd_ins.gif" alt="running cmds from terminal" width="80%"><br>
   <b>🐸 Execute command line instructions without remembering any of those!</b><br>

</div>


## Features 🌟

- 🖥️ **Command-line Instruction Conversion:** Translates human language into precise command-line instructions with descriptions.
- 👨‍💻 **Bug Fixer/Debugger:** Provides to the point solutions to bugs and vulnerabilities by analyzing your program file.
- 💡 **Programming Hints:** Provides concise hints for programming problems, along with example code snippets.
- 🎨 **Interactive Interface:** Engages users with an interactive CLI powered by the `rich` library, featuring styled panels and prompts.
- ⚡ **Command Execution:** Offers the ability to execute shell commands directly from the interface and view the output in real-time.
- 🔧 **Configurable Prompt Template:** The prompt template is stored in a JSON file, making it easy to modify and extend.
- 🛠️ **File Analysis:** Understands, debugs, and fixes code by analyzing file contents, providing summaries, debugging tips, and code fixes.

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

COMANDI offers a range of functionalities to assist with command-line operations, programming hints, and file analysis. Below is a step-by-step guide to using these capabilities:

### 1. **Command-line Instruction:**
   - **Purpose:** Convert natural language instructions into executable command-line commands.
   - **Example:**  
     You can input a request like:
     ```
     Create a new directory and navigate into it.
     ```
     **What happens next:**  
     COMANDI will generate the corresponding command and a brief description explaining its function.

   - **Execution:**  
     After the command is generated, you'll have the option to execute it directly from the interface. Simply respond with `y` when prompted, and the command will run, with the output displayed in the terminal.

### 2. **Programming Hint:**
   - **Purpose:** Get quick tips and example code snippets for programming questions.
   - **Example:**  
     You might ask:
     ```
     How do I sort a list in Python?
     ```
     **What happens next:**  
     COMANDI will provide a one-line hint and an example code snippet, including comments explaining each step of the implementation.

### 3. **File Analysis:**
   - **Purpose:** Analyze file contents for understanding, debugging, or fixing code.
   - **How to use:**  
     You can request analysis by specifying the desired action and the file path. For example:
     ```
     understand path/to/your/file.py
     debug path/to/your/file.py
     fix path/to/your/file.py
     ```
     **What happens next:**  
     COMANDI will analyze the file based on your request, providing a summary, potential improvements, debugging tips, and code fixes, as applicable.

### 4. **Exiting the Program:**
   - **Purpose:** End your COMANDI session.
   - **How to exit:**  
     Type `quit` or `exit` to close the program.

## Technical Details 🔧

- **Language:** Python 3.x
- **Libraries Used:**
  - `rich` for creating a styled CLI interface.
  - `subprocess` for executing shell commands.
  - `json` for handling the prompt template.
  - `meta-ai-api` for AI response generation.

## Prompt Analysis 🔍

The `prompt.json` file is the backbone of the AI's functionality, defining how it processes different types of user inputs. Here's an in-depth look:

1. **Triple Functionality:** The AI is equipped to handle three primary tasks:
   - **Command-Line Conversion:** Translating human instructions into command-line commands.
   - **Programming Hints:** Offering concise tips with example code snippets.
   - **File Analysis:** Understanding, debugging, and fixing code files based on user input.

2. **Response Format:**
   - **For Command-Line Instructions:**
     ```
     COMMAND: <command-line instruction>
     DESCRIPTION: <brief description of what the command does>
     ```
     - **Fallback:** If the AI is unable to generate a command, it replies with:
     ```
     COMMAND: UNABLE_TO_PROCESS
     DESCRIPTION: I couldn't generate a command-line instruction for that request.
     ```
   - **For Programming Hints:**
     ```
     HINT: <one-line programming hint>
     EXAMPLE: <A code snippet showing an implementation of the given problem.>
     ```
   - **For File Analysis:**
     ```
     SUMMARY: <Brief summary of the file contents>
     IMPROVEMENTS: <Point-wise list of improvement suggestions, including fixing vulnerabilities.>
     DEBUGGING TIPS: <Suggestions for debugging, if relevant.>
     CODE FIXES: <Specific line-by-line code fixes, if needed.>
     ```

3. **Contextual Awareness:** The AI determines whether the input pertains to command-line instructions, programming questions, or file analysis based on the context provided.

4. **Emphasis on Brevity:** The AI is designed to provide concise, focused responses, especially in the case of programming hints, ensuring that the output is both clear and actionable.

## Roadmap 🗺️

Here's our planned roadmap for future COMANDI development:

1. **User Preferences** 🎛️ : Implement user-specific settings (e.g., preferred shell, programming language)

2. **Command History** 📜 : Add a feature to save and recall previous commands and responses

3. **Integration with Version Control Systems** 🔄: Add features to interact with git and other VCS directly from COMANDI

## Contributing 🤝

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to this project.

## License 📄

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to [meta-ai-api](https://github.com/Strvm/meta-ai-api) library by [Roméo](https://github.com/Strvm)!
- Special thanks to the creators of the `rich` library for making CLI development visually stunning and accessible.

We're excited about the future of COMANDI and welcome community input on these plans!
