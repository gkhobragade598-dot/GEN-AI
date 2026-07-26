# 6. Advance Prompt Engineering

def create_stepwise_prompt(context):
    step1_prompt = f"Summarize this text:{context}"

    # Generate an AI summary (this is hypothetical code for an API)

    ai_summary = "This is a summary of the context." # placeholder for the actual API

    step2_prompt = f"Based on the summary: '{ai_summary}', answer the following questions"

    return step1_prompt,step2_prompt

context = "Artificial intelligence has become a pivotal technology in the 21st century"
step1, step2 = create_stepwise_prompt(context)

print("step 1 prompt:" , step1)
print("step 2 prompt:", step2)