prompt = """
# Initialize the GPT-3 5 Turbo API
    gpt_3_5_turbo = GPT_3_5_Turbo(
        system='''
        You are a chatbot agent with language processing functionality.
        You are given a conversation and a specified work.
        You must clean and tokenize the conversation and perform the specified work.
        You must return a boolean indicating success and a message string.
        ''')

    # Initialize the success and message variables
    success = True
    message = ""

    # Loop through each conversation
    for conversation in conversations:
        # Loop through each agent
        for agent in agents:
            # Generate the initial prompt for the agent
            prompt = initial_prompt + agent['language_processing'] + conversation

            # Generate the response using the GPT-3 5 Turbo API
            response = gpt_3_5_turbo(prompt)

            # Check if the response contains the specified work
            if specified_work in response:
                # Set the success boolean to True and break out of the loop
                success = True
                break
            else:
                # Set the success boolean to False and continue to the next agent
                success = False

        # Check if the success boolean is False
        if not success:
            # Set the message string and break out of the loop
            message = "Failed to perform specified work on conversation: " + conversation
            break

    # Check if the success boolean is True
    if success:
        # Set the message string
        message = "Successfully performed specified work on all conversations"

    # Return the success boolean and message string as a dictionary
    return {"success": success, "message": message}
"""
