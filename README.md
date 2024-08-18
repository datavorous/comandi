<div align="center">

# COMANDI v0.0.2 

Free AI-powered CLI for Programming Support,  
Error Debugging and Automated Instruction Translations. 

<a href="https://app.commanddash.io/agent/github_datavorous_comandi"><img src="https://img.shields.io/badge/AI-Code%20Agent-EB9FDA"></a>
![Python version](https://img.shields.io/badge/python-3.10%2B-blue)
</div>

## ✨ Demo Showcase

<div align="center"> 

<img src="https://raw.githubusercontent.com/datavorous/comandi/main/imgs/syntax.gif" alt="demo" width="80%">  <br>
   <b>⚡ Get syntax highlighted code and debug your files!</b><br><br>

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
Here's the modified part of the installation section with instructions for locally building and installing the package:

---

## Installation 📦

To install and run COMANDI, ensure you have Python 3.x installed, then follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/datavorous/comandi.git
   cd comandi
   ```

2. **Build the Package**

   Use `setuptools` to build your package:

   1. **Install necessary tools:**
      ```bash
      pip install setuptools wheel 
      ```

   2. **Build the source distribution and wheel:**
      ```bash
      python setup.py sdist bdist_wheel
      ```

      This will generate distribution archives in the `dist/` directory.

3. **Install the Package**

   Use `pip` to install the package globally:
   ```bash
   pip install .
   ```
4. **Run from anywhere**  
   Use ```comandi -run``` to run it from anywhere.
   ```bash
   comandi -run
   ```
   
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
     understand path/to/your/file.py:10-15,27-48
     debug path/to/your/file.py
     fix path/to/your/file.py
     ```
     **What happens next:**  
     COMANDI will analyze the file based on your request, providing a summary, potential improvements, debugging tips, and code fixes, as applicable. By mentioning the line ranges you can specify the only required lines which need to be checked.

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
