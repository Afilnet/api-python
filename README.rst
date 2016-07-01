Afilnet Cloud Marketing
=======================

This package is designed to be an easy way to use Afilnet API services. You can send SMS, email and voice notifications using your Afilnet account.

You only need an Afilnet account with enought credits.
If you do not have an account, you can `create it <http://afilnet.us/client/register.php/>`_ in a few minutes.


Installation
------------
You can use pip to install this package.
Go to your terminal and run: pip install afilnet


Easy to use
~~~~~~~~~~~

You only need to call the module ``urls.py`` + service:

.. code-block:: python

    res = afilnet.sendSMS("MyAfilnetUsername", "MyAfilnetPassword", "To", "This is a test message", "From")


Then you will receive the result in json.


Available Services
------------------
There are 4 channels availables:
- General
- SMS
- Email
- Voice

This library use the structure:

.. code-block:: python

    res = afilnet.service(params)

General has two services:
- getBalance (Get balance of your account)
- isUser (Return if user is valid or not) *This service return a boolean*

SMS, Email and Voice have the same services:
- send (Send to a single user)
- sendFromTemplate (Send to a single user using a template)
- sendToGroup (Send to a defined group)
- sendToGroupFromTemplate (Send to a defined group using a template)
- getDeliveryStatus (Get delivery status of a message)

## SMS
~~~~~~
- sendSms(username, password, to, message, sender, scheduledatetime="")
- sendSmsFromTemplate(username, password, to, idTemplate, params, scheduledatetime="")
- sendSmsToGroup(username, password, sender, countryCode, idGroup, msg, scheduledatetime="")
- sendSmsToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime="")

## Email
~~~~~~~~
- sendEmail(username, password, subject, to, message, scheduledatetime=""):
- sendEmailFromTemplate(username, password, to, idTemplate, params, scheduledatetime="")
- sendEmailToGroup(username, password, subject, idGroup, msg, scheduledatetime="")
- sendEmailToGroupFromTemplate(username, password, idGroup, idTemplate, scheduledatetime="")

## Voice
~~~~~~~~
- sendVoice(username, password, to, message, lang="", scheduledatetime="")
- sendVoiceFromTemplate(username, password, to, idTemplate, params, scheduledatetime="")
- sendVoiceToGroup(username, password, countryCode, idGroup, msg, scheduledatetime="")
- sendVoiceToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime="")

## User
~~~~~~~
- getBalance(username, password)
- isUser(username, password)