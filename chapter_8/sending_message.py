def send_messages(unsent_messages, sent_messages):
    """Prints messages in a list, then moves them to a list
    To record they were sent"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(current_message)
        sent_messages.append(current_message)

unsent_messages = ["Aloha, whitey.", "Kiss my ass!", "Nice hat, really."]
sent_messages = []

# send_messages(unsent_messages, sent_messages)
# print(unsent_messages)
# print(sent_messages)

send_messages(unsent_messages[:], sent_messages)
print(unsent_messages)
print(sent_messages)