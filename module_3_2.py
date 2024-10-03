def email_com_ru(recipient, sender='university.help@gmail.com'):
    # flag_ = True
    flag_dog = True
    flag_recipient = False
    flag_sender = False

    if "@" not in recipient or "@" not in sender:
        flag_dog = False

    else:
        ru_sender = ((sender[::-1])[:3])[::-1]  # ишем .ru
        ru_sender = ru_sender.lower()

        net_com_sender = ((sender[::-1])[:4])[::-1]
        net_com_sender = net_com_sender.lower()

        ru_recipient = ((recipient[::-1])[:3])[::-1]
        ru_recipient = ru_recipient.lower()

        net_com_recipient = ((recipient[::-1])[:4])[::-1]
        net_com_recipient = net_com_recipient.lower()

        if ru_sender == '.ru' or net_com_sender == '.net' or net_com_sender == '.com':
            flag_sender = True

        if ru_recipient == '.ru' or net_com_recipient == '.net' or net_com_recipient == '.com':
            flag_recipient = True

    if flag_sender and flag_recipient and flag_dog:
        flag_ = True

    else:
        flag_ = False

    if not flag_:
        print(f'Невозможно отправить письмо с адреса,{sender},на адрес,{recipient}')

    return flag_


def send_email(message, recipient,*, sender="university.help@gmail.com"):
    flag_email_com_ru = email_com_ru(recipient, sender)
    flag_self = False
    # message - По условию, "прикрутить" некуда

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        flag_self = True

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса,{sender},на адрес,{recipient}')

    else:
        if flag_email_com_ru and not flag_self:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса,{sender},на адрес,{recipient}')

    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
