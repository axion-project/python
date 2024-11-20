# Author: Michael Morales

import openai

# Set up your API key
openai.api_key = "your_openai_api_key"

def query_openai(prompt, model="gpt-4", max_tokens=150):
    """
    Function to interact with OpenAI's API using the specified model.
    
    Args:
        prompt (str): The input prompt for the model.
        model (str): The OpenAI model to use (default: "gpt-4").
        max_tokens (int): The maximum number of tokens to generate (default: 150).

    Returns:
        str: The generated response from the model.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the LLM interaction script!")
    while True:
        user_input = input("\nEnter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = query_openai(user_input)
        print(f"\nLLM Response:\n{response}")
