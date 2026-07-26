# 5. Generate Multiple prompts Dynamically Using Lists and Strings

def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"Explain {item} in sample terms."
        prompts.append(prompt)
    return prompts

# Sample data list (e.g., topics to explain )
data_list = ["quantum computing", "machine learning", "climate change"]

# Generatee prompts
prompt = generate_prompts_from_data(data_list)

# print each prompt
for prompt in prompt:
    print(prompt)