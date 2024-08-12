import sys
import subprocess
import json
from meta_ai_api import MetaAI
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

# Initialize the rich console
console = Console()

def load_prompt():
    """Load the prompt template from the JSON file."""
    try:
        with open('prompt.json', 'r') as file:
            data = json.load(file)
            return data['prompt_template']
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] prompt.json file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        console.print("[bold red]Error:[/bold red] Invalid JSON in prompt.json file.")
        sys.exit(1)
    except KeyError:
        console.print("[bold red]Error:[/bold red] 'prompt_template' key not found in prompt.json.")
        sys.exit(1)

def print_introduction():
    intro_text = Text(justify="center")
    intro_text.append("COMANDI v0.0.1\n\n", style="bold spring_green2")
    
    intro_text.append("📋 ")
    intro_text.append("Guidelines\n", style="bold white")
    
    intro_text.append("Type your request for command-line equivalents\n", style="white")
    intro_text.append("Ask programming questions for hints and examples\n", style="white")
    intro_text.append("Type 'quit' or 'exit' to end the session\n\n", style="white")
    
    #intro_text.append("An active INTERNET connection is required.\n\n", style="bold red1")

    # Create a panel with centered text
    intro_panel = Panel(
        Align.center(intro_text, vertical="middle")
        #border_style="bold red"
    )

    console.print(intro_panel)

def execute_command(command):
    """Execute shell commands."""
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        return output.strip() if process.returncode == 0 else f"Error: {error.strip()}"
    except Exception as e:
        return f"An error occurred while executing the command: {str(e)}"

def get_ai_response(user_input, prompt_template):
    """Get AI response for user input."""
    meta = MetaAI()
    full_prompt = f"{prompt_template}\n\nUser input: {user_input}\n\nResponse:"
    response = meta.prompt(message=full_prompt)
    return parse_ai_response(response['message'].strip())

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

    if example_lines:
        result['example'] = '\n'.join(example_lines).strip()

    return result

def main():
    """Main function to run the CLI interface."""
    prompt_template = load_prompt()

    print_introduction()

    try:
        while True:
            user_input = Prompt.ask(Text("::", style="green1"))

            if user_input.lower() in ['quit', 'exit']:
                console.print(Text("🚀 Goodbye! 👋 See you soon!", style="bold green1"))
                break

            try:
                ai_response = get_ai_response(user_input, prompt_template)

                if ai_response['type'] == 'hint':
                    # Print hint inside a bordered panel with white text
                    hint_panel = Panel(
                        Text(ai_response['hint'], style="white"),
                        title="💡 Programming Hint:",
                        border_style="bold spring_green1",
                        style="white"
                    )
                    console.print(hint_panel)
                    
                    if 'example' in ai_response:
                        # Print example inside a bordered panel
                        example_panel = Panel(
                            Text(ai_response['example'], style="white"),
                            title="📚 Example:",
                            border_style="bold deep_pink3",
                            style="white"
                        )
                        console.print(example_panel)

                elif ai_response['type'] == 'command':
                    if ai_response.get('command') == 'UNABLE_TO_PROCESS':
                        console.print(Text(ai_response.get('description', 'Unable to process the request.'), style="yellow"))
                    else:
                        # Print command inside a bordered panel
                        command_panel = Panel(
                            Text(ai_response.get('command', 'No command provided.'), style="white"),
                            title="🛠️ Command:",
                            border_style="bold deep_pink3",
                            style="white"
                        )
                        console.print(command_panel)
                        
                        # Print description inside a bordered panel
                        description_panel = Panel(
                            Text(ai_response.get('description', 'No description provided.'), style="white"),
                            title="📄 Description:",
                            border_style="spring_green1",
                            style="white"
                        )
                        console.print(description_panel)

                        execute_choice = Prompt.ask(Text(" Execute this command? (y/n): ", style="spring_green1")).lower()

                        if execute_choice == 'y':
                            command_output = execute_command(ai_response['command'])
                            # Print command output inside a bordered panel
                            output_panel = Panel(
                                Text(command_output, style="white"),
                                title="🔍 Command Output:",
                                border_style="spring_green1",
                                style="white"
                            )
                            console.print(output_panel)

                console.print()  # Add a blank line for readability

            except Exception as e:
                console.print(Panel(Text(f"❌ An error occurred: {str(e)}", style="bold red"), border_style="bold red"))

    except KeyboardInterrupt:
        console.print(Panel(Text("🔚 Session ended by user.", style="bold cyan"), border_style="bold cyan"))
        sys.exit(0)


if __name__ == "__main__":
    main()
