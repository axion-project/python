from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_name = "gpt-4"  # Replace with your desired Hugging Face model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize the pipeline
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Few-shot Prompting Example
def few_shot_prompting():
    prompt = (
        "Translate the following English sentences to French:\n"
        "1. Hello, how are you?\n"
        "2. What is your name?\n"
        "3. I love programming.\n"
        "4. Please translate: Where is the nearest train station?"
    )
    output = text_generator(prompt, max_length=100, num_return_sequences=1)
    print("Few-Shot Prompting Output:")
    print(output[0]['generated_text'])

# Zero-shot Prompting Example
def zero_shot_prompting():
    prompt = "Summarize the following text:\n\n'Artificial intelligence is transforming industries by automating tasks and providing insights.'"
    output = text_generator(prompt, max_length=50, num_return_sequences=1)
    print("\nZero-Shot Prompting Output:")
    print(output[0]['generated_text'])

# Chain-of-Thought Prompting Example
def chain_of_thought_prompting():
    prompt = (
        "Solve this math problem step-by-step:\n"
        "If a train travels 60 miles per hour for 2 hours, how far does it travel?"
    )
    output = text_generator(prompt, max_length=100, num_return_sequences=1)
    print("\nChain-of-Thought Prompting Output:")
    print(output[0]['generated_text'])

# Main Execution
if __name__ == "__main__":
    print("Running Few-Shot Prompting...")
    few_shot_prompting()

    print("\nRunning Zero-Shot Prompting...")
    zero_shot_prompting()

    print("\nRunning Chain-of-Thought Prompting...")
    chain_of_thought_prompting()
