#TODO: write docs and comments 

# import pkg_resources
import sys
import subprocess
import json
import os
import platform
import shutil
from meta_ai_api import MetaAI
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from threading import Thread
from rich.status import Status
from rich.spinner import Spinner
import time
from rich.syntax import Syntax
from rich.console import Console
import importlib.resources as resources


# Initialize the rich console
console = Console()

def get_system_info():
    info = {}
    
    # Get model name
    try:
        system = platform.system()
        if system == "Darwin":
            info['model'] = subprocess.check_output(["sysctl", "-n", "hw.model"]).decode("utf-8").strip()
        elif system == "Linux":
            info['model'] = subprocess.check_output(["cat", "/sys/devices/virtual/dmi/id/product_name"]).decode("utf-8").strip()
        elif system == "Windows":
            info['model'] = subprocess.check_output("wmic csproduct get name").decode("utf-8").split("\n")[1].strip()
        else:
            info['model'] = "Unknown"
    except:
        info['model'] = platform.machine()

    # Get processor information
    try:
        info['processor'] = platform.processor()
        if info['processor'] == "":
            info['processor'] = platform.machine()
    except:
        info['processor'] = "Unknown"

    # Get storage information
    try:
        total, used, free = shutil.disk_usage('/')
        info['storage_left'] = f"{free // (2**30)} GB"
    except:
        info['storage_left'] = "Unknown"

    # Get current directory
    try:
        info['current_dir'] = os.getcwd()
    except:
        info['current_dir'] = "Unknown"

    return info

def print_introduction():
    system_info = get_system_info()
    
    # Create the intro text
    intro_text = Text(justify="left")
    intro_text.append(f"Model: {system_info['model']}\n", style="bold white")
    intro_text.append(f"Processor: {system_info['processor']}\n", style="bold white")
    intro_text.append(f"Storage Left: {system_info['storage_left']}\n", style="bold white")

    # Create the panel with a title and border styling
    intro_panel = Panel(
        Align.center(intro_text, vertical="middle"),
        title="comandi v0.0.2",
        border_style="bold #ffffff",
        style="bold white"
    )

    # Print the panel to the console
    console.print(intro_panel)



def load_prompt():
    try:
        #before: prompt_path = pkg_resources.resource_filename('comandi','prompt.json')
        prompt_path = resources.path('comandi', 'prompt.json')
        with open(prompt_path, 'r') as file:
            data = json.load(file)
            return data['prompt_template']
    except FileNotFoundError:
        console.print("[bold #ffffff]Error:[/bold #ffffff] prompt.json file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        console.print("[bold #ffffff]Error:[/bold #ffffff] Invalid JSON in prompt.json file.")
        sys.exit(1)
    except KeyError:
        console.print("[bold #ffffff]Error:[/bold #ffffff] 'prompt_template' key not found in prompt.json.")
        sys.exit(1)



def execute_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        return output.strip() if process.returncode == 0 else f"Error: {error.strip()}"
    except Exception as e:
        return f"An error occur while executing the command: {str(e)}"



# the following funcstions are self explanatory im not documenting this now
def parse_ai_response(response):
    """Parse AI response."""
    lines = response.split('\n')
    result = {}
    example_lines = []
    in_example = False

    for line in lines:
        if line.startswith('COMMAND:'):
            result['type'] = 'command'
            result['command'] = line.split('COMMAND:')[1].strip()
        elif line.startswith('DESCRIPTION:'):
            result['description'] = line.split('DESCRIPTION:')[1].strip()
        elif line.startswith('HINT:'):
            result['type'] = 'hint'
            result['hint'] = line.split('HINT:')[1].strip()
        elif line.startswith('EXAMPLE:'):
            in_example = True
            continue
        elif in_example:
            example_lines.append(line)
        elif line.startswith(('SUMMARY:', 'IMPROVEMENTS:', 'DEBUGGING TIPS:', 'CODE FIXES:')):
            section = line.split(':')[0].strip()
            result[section] = []
        elif any(key in result for key in ['SUMMARY', 'IMPROVEMENTS', 'DEBUGGING TIPS', 'CODE FIXES']):
            for key in ['SUMMARY', 'IMPROVEMENTS', 'DEBUGGING TIPS', 'CODE FIXES']:
                if key in result:
                    result[key].append(line.strip())
                    break

    if example_lines:
        result['example'] = '\n'.join(example_lines).strip()

    return result

def read_file_contents(file_path, line_numbers=None):
    """Read and return the contents of a file. Optionally read only specified line numbers."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if line_numbers:
                selected_lines = [lines[i-1] for i in line_numbers if 0 <= i-1 < len(lines)]
                return ''.join(selected_lines)
            else:
                return ''.join(lines)
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"


def analyze_file(file_path, analysis_type, line_range=None):
    """Analyze file contents based on the analysis type and specific line numbers."""
    content = read_file_contents(file_path, line_numbers=line_range)
    if content.startswith("Error:"):
        return content

    prompt_template = load_prompt()
    
    if analysis_type == "understand":
        prompt = f"{prompt_template}\nAnalyze and summarize the following file contents:\n\n{content}\n\nProvide a brief summary and improvement tips."
    elif analysis_type == "debug":
        prompt = f"{prompt_template}\nAnalyze the following code for potential bugs and provide debugging tips:\n\n{content}"
    elif analysis_type == "fix":
        prompt = f"{prompt_template}\nAnalyze the following code, identify errors, and suggest fixes:\n\n{content}"
    else:
        return "Invalid analysis type."

    return get_ai_response(prompt, prompt_template)


def display_file_analysis(analysis_result):
    """Display file analysis results using Rich panels."""
    for section, content in analysis_result.items():
        if isinstance(content, list) and content:
            panel = Panel(
                Text('\n'.join(content), style="bold white"),
                title=f"📊 {section}:",
                border_style="bold #ffffff",
                style="bold white"
            )
            console.print(panel)


def parse_ranges(range_str):
    """Parse a string of line ranges (e.g., '10-20,25-29') into a list of line numbers."""
    ranges = range_str.split(',')
    line_numbers = []
    for r in ranges:
        start_line, end_line = map(int, r.split('-'))
        line_numbers.extend(range(start_line, end_line + 1))
    return line_numbers



'''
This function handles file-related commands by determining the type of analysis requested (understand, debug, or fix) and then calling analyze_file() to perform the analysis. If the file does not exist, it prints an error message. If the analysis is successful, it uses display_file_analysis() to show the results to the user. This function serves as a central hub for managing file-related tasks within the program.
'''
from rich.syntax import Syntax
from rich.panel import Panel

def display_example_code(code_example, language="python"):
    """Display example code with syntax highlighting inside a panel."""
    syntax = Syntax(code_example, language, theme="github-dark", line_numbers=True)
    panel = Panel(syntax, title="Example", border_style="bold #ffffff", title_align="left")
    console.print(panel)

def handle_file_command(command, file_path_and_lines):
    """Handle file-related commands with optional line range."""
    if ':' in file_path_and_lines:
        file_path, line_range_str = file_path_and_lines.split(':')
        line_numbers = parse_ranges(line_range_str)
        analysis_type = command.split()[0]
        analysis_result = analyze_file(file_path, analysis_type, line_range=line_numbers)
    else:
        file_path = file_path_and_lines
        analysis_type = command.split()[0]
        analysis_result = analyze_file(file_path, analysis_type)

    if isinstance(analysis_result, str) and analysis_result.startswith("Error:"):
        console.print(f"[bold #ffffff]{analysis_result}[/bold #ffffff]")
    else:
        display_file_analysis(analysis_result)

        # Check if the analysis result has an example
        if 'example' in analysis_result:
            display_example_code(analysis_result['example'])


def get_ai_response(user_input, prompt_template):
    meta = MetaAI()
    full_prompt = f"{prompt_template}\n\nUser input: {user_input}\n\nResponse:"
    
    response = None
    
    def ai_request():
        nonlocal response
        response = meta.prompt(message=full_prompt)
    
    thread = Thread(target=ai_request)
    thread.start()
    
    with console.status("[bold white]Processing...", spinner="bouncingBar", spinner_style="bold #ffffff"):
        while thread.is_alive():
            time.sleep(0.1)
    
    thread.join()
    
    if response:
        parsed_response = parse_ai_response(response['message'].strip())
        # If there's an example, show it inside a panel with syntax highlighting
        if 'example' in parsed_response:
            display_example_code(parsed_response['example'])
        return parsed_response
    else:
        return "No response received from AI."


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-run':
        prompt_template = load_prompt()
        print_introduction()

        try:
            while True:
                user_input = Prompt.ask(Text("::", style="bold #ffffff"))

                if user_input.lower() in ['quit', 'exit']:
                    console.print(Text("Goodbye! See you soon!", style="bold #ffffff"))
                    break

                if user_input.lower() == 'help':
                    display_help()
                    continue

                if user_input.startswith(('understand ', 'debug ', 'fix ')):
                    command, file_path_and_lines = user_input.split(maxsplit=1)
                    handle_file_command(command, file_path_and_lines)
                else:
                    try:
                        ai_response = get_ai_response(user_input, prompt_template)

                        if ai_response['type'] == 'hint':
                            hint_panel = Panel(
                                Text(ai_response['hint'], style="bold white"),
                                title="Explanation",
                                border_style="bold #ffffff",
                                style="bold white"
                            )
                            console.print(hint_panel)
                            
                            '''if 'example' in ai_response:
                                example_panel = Panel(
                                    Text(ai_response['example'], style="bold white"),
                                    title="Example",
                                    border_style="bold #ffffff",
                                    style="bold white"
                                )
                                console.print(example_panel)'''

                        elif ai_response['type'] == 'command':
                            if ai_response.get('command') == 'UNABLE_TO_PROCESS':
                                console.print(Text(ai_response.get('description', 'Unable to process the request.'), style="bold #ffffff"))
                            else:
                                command_panel = Panel(
                                    Text(ai_response.get('command', 'No command provided.'), style="bold white"),
                                    title="🛠️ Command:",
                                    border_style="bold #ffffff",
                                    style="bold white"
                                )
                                console.print(command_panel)
                                
                                description_panel = Panel(
                                    Text(ai_response.get('description', 'No description provided.'), style="bold white"),
                                    title="Description",
                                    border_style="bold #ffffff",
                                    style="bold white"
                                )
                                console.print(description_panel)

                                execute_choice = Prompt.ask(Text(" Execute this command? (y/n): ", style="spring_green1")).lower()

                                if execute_choice == 'y':
                                    command_output = execute_command(ai_response['command'])
                                    output_panel = Panel(
                                        Text(command_output, style="bold white"),
                                        title="Command Output",
                                        border_style="spring_green1",
                                        style="bold white"
                                    )
                                    console.print(output_panel)

                        console.print()  # Add a blank line for readability

                    except Exception as e:
                        console.print(Panel(Text(f"❌ An error occur#ffffff: {str(e)}", style="bold #ffffff"), border_style="bold #ffffff"))

        except KeyboardInterrupt:
            console.print(Panel(Text("🔚 Session ended by user.", style="bold cyan"), border_style="bold cyan"))
            sys.exit(0)
    else:
        print("Usage: comandi -run")
        sys.exit(1)

def display_help():
    help_text = Text()
    help_text.append("Comandi Help:\n\n", style="bold")
    help_text.append("• Type natural language queries to get command suggestions or programming help\n")
    help_text.append("• Use 'understand', 'debug', or 'fix' followed by a file path for file analysis\n")
    help_text.append("• Type 'quit' or 'exit' to end the session\n")
    
    help_panel = Panel(
        help_text,
        title="Help",
        border_style="bold #ffffff",
        expand=False
    )
    console.print(help_panel)

def cli_main():
    main()

if __name__ == "__main__":
    cli_main()
