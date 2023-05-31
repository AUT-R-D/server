import gpt_2_simple as gpt2

"""
# Temporary code for chatGPT...
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

messages = []
system_msg = input("What type of chatbot would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while input != "quit()": 
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
"""

# remember to $ pip3 install openai
openai.api_key = "" #Carl OpenAi API key

def a():
 print("Hi")
 #method here to get the reponse from GPT
completion = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": "What is 4+4"} ]);
print(completion);
    #gptResponse = completion.choices[0].message.content;
gptResponse = completion["choices"][0]["message"]["content"];
print(gptResponse);



if __name__ == '__main__':
    a()