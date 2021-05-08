# -*- coding: utf-8 -*-
# Using Python 3.x

"""
Sending email with smtplib and EmailMessage
Enviando email com smtplib and EmailMessage
** Usado com Gmail
** Liberar - apps menos seguros - para acessar a conta
"""
__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "19-nov-2020"
__version__ = "0.1"
__status__ = ""

import smtplib as smail
from email.message import EmailMessage
from string import Template
from pathlib import Path


def send(receiver):
    receiver_name = receiver[0]
    receiver_email = receiver[1]
    sender_name = "Name"
    sender_email = "email@gmail.com"
    sender_psswd = "p4ssw0rd"

    html = Template(Path("py_email.html").read_text())
    d = dict(name=receiver_name, email=receiver_email)

    email = EmailMessage()
    email["from"] = sender_name
    email["to"] = receiver_email
    email["subject"] = "Email Python"
    email.set_content(html.substitute(d), "html")

    try:
        with smail.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender_email, sender_psswd)
            smtp.send_message(email)
            print("Success!!! Email =>", receiver_email)
    except Exception as e:
        print(e)


def main():
    receivers = (
        ("name_dest1", "dest_1@email.com"),
        ("name_dest2", "dest_2@email.com"),
        ("name_dest3", "dest_3@email.com"),
    )
    for receiver in receivers:
        send(receiver)


if __name__ == "__main__":
    main()
