class Email:
    def __init__(self):
        self.is_sent = False

    def send_email(self):
        self.is_sent = True

my_email = Email()
print(my_email.is_sent)
my_email.send_email()
print(my_email.is_sent)
