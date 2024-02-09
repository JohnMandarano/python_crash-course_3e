prompt = "Please tell me a topping you would like on your pizza."
prompt += "\nOnce you are done adding toppings, please enter 'quit'."

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")