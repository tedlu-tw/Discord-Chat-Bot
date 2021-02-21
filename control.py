while True:
    message = input('Enter message: ')
    with open('message.txt', 'w') as f:
        f.write(message)
