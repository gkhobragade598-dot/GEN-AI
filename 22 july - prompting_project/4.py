# 4. Create prompt using templates

def create_summery_prompt(text):
    prompt_template = "Summarize the following text: {text}"
    return prompt_template.format(text=text)

# example of using the template
input_text ="AI is rapidly changing the way we work , communicate, and solve problem"
summary_prompt = create_summery_prompt(input_text)
print ("Generated Summary Prompt:",summary_prompt)