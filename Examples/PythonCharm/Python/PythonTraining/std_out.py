import sys

stdout_fileno = sys.stdout

sample_input = ['Hi', 'Hello from AskPython', 'exit']

for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')