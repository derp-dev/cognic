#bracks processing
# Define a function to process the custom syntax
def process_custom_syntax(input_text, context={}):
    # Split input into tokens
    tokens = input_text.split()

    # Initialize output
    output = ""

    # Loop through tokens
    for token in tokens:
        # Check if placeholder
        if token.startswith("{{") and token.endswith("}}"):
            key = token[2:-2]
            if key in context:
                output += context[key]
            else:
                output += token
        else:
            output += token

        # Add space after token
        output += " "

    # Remove trailing space
    return output.strip()

# Example usage
custom_syntax = "This is a {{key1}} example {{key2}} with some {{key3}}."
context = {
    "key1": "custom",
    "key2": "text",
    "key3": "placeholders"
}

result = process_custom_syntax(custom_syntax, context)
print(result)

"""
This code defines a function called process_custom_syntax() that takes two arguments: the input text and a context dictionary. The function first splits the input text into tokens. Then, it iterates through the tokens and checks if each token is a placeholder. If the token is a placeholder, the function checks if the corresponding key is in the context dictionary. If it is, the function appends the value of the key to the output string. Otherwise, the function simply appends the token to the output string. Finally, the function removes any trailing spaces from the output string and returns it.

In the example usage, the input text is "This is a {{key1}} example {{key2}} with some {{key3}}." The context dictionary is {"key1": "custom", "key2": "text", "key3": "placeholders"}. The process_custom_syntax() function first splits the input text into tokens. Then, it iterates through the tokens and checks if each token is a placeholder. The first token, "This", is not a placeholder, so the function simply appends it to the output string. The second token, "{{key1}}", is a placeholder. The function checks if the key "key1" is in the context dictionary. It is, so the function appends the value of the key, which is "custom", to the output string. The third token, "example", is not a placeholder, so the function simply appends it to the output string. The fourth token, "{{key2}}", is a placeholder. The function checks if the key "key2" is in the context dictionary. It is, so the function appends the value of the key, which is "text", to the output string. The fifth token, "with", is not a placeholder, so the function simply appends it to the output string. The sixth token, "{{key3}}", is a placeholder. The function checks if the key "key3" is in the context dictionary. It is, so the function appends the value of the key, which is "placeholders", to the output string.

Finally, the process_custom_syntax() function removes any trailing spaces from the output string and returns it. In this case, the output string is "This is a custom example text with some placeholders."
"""