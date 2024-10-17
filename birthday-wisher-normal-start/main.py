##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "thiagoassisdecarvalho@gmail.com"
MY_PASSWORD = "aeznagajenhajsho"

today = dt.datetime.now()
now = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if now in birthdays_dict:
    birthday_person = birthdays_dict[now]
    letter = random.randint(1,3)
    with open(f"letter_templates/letter_{letter}.txt") as letter:
        carta = letter.read()
        new_letter = carta.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



