import json

emails = open('test.txt', 'r', encoding='utf-8').read().splitlines()
# account login credentials
accounts = json.loads(open('users_credentials.json', 'r', encoding='utf-8').read())

# total accounts
accounts_len = accounts.__len__()
print(f"Total Accounts: {accounts_len}")
account_position = 1

start_email = 0
end_email = 25
for email in range(int(emails.__len__() / 25) + 1):
    # print(emails[start_email:end_email])
    cred = accounts[account_position - 1]

    if account_position == accounts_len:
        account_position = 0
    if account_position < accounts_len:
        account_position += 1

    start_email += 25
    end_email += 25
    print(start_email, end_email)
    print(f"Total Emails Sent => {end_email}")

