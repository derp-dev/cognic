import os
import time

system = 'you are a coding agent. you can read and write files. Eg `cat helloworld.txt`, `echo "hello\nworld" > helloworld.txt`
output the next command required to progress your goal. output `DONE` when done.'

def chat(prompt, system=None):
    """It prints the prompt with formatting, then runs the llm chatbot using subprocess and passes the prompt. It captures the response, prints it with formatting, and returns the response string."""
    options = f"-s {system}" if system else "-c" # start with system prompt, or continue
    print(f"\033[0;36m[PROMPT]\033[0m {prompt}")
    response = os.popen(f"llm {options} {prompt}").read()
    print(f"\033[1;33m[RESPONSE]\033[0m {response}")
    return response

response = chat(f"GOAL: {sys.argv[1]}\n\nWHAT IS YOUR OVERALL PLAN?", system)

while True:
    response = input("SHELL COMMAND TO EXECUTE OR `DONE`. NO ADDITIONAL CONTEXT OR EXPLANATION:").strip()
    if response == "DONE":
        break

    time.sleep(3)
    output_array = []
    return_code = os.system(response + " 2>&1") >> 8
    output = "\n".join(output_array)
    response = chat(f"COMMAND COMPLETED WITH RETURN CODE: {return_code}. OUTPUT:\n{output}\n\nWHAT ARE YOUR OBSERVATIONS?")
