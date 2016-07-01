try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json

def sendSms(username, password, to, message, sender, scheduledatetime=""):
    clase = "sms"
    metodo = "sendsms"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&from=" + sender + "&to=" + to + "&sms=" + message + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendSmsFromTemplate(username, password, to, idTemplate, params, scheduledatetime=""):
    clase = "sms"
    metodo = "sendsmsfromtemplate"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendSmsToGroup(username, password, sender, countryCode, idGroup, msg, scheduledatetime=""):
    clase = "sms"
    metodo = "sendsmstogroup"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&from=" + sender + "&countrycode" + countryCode + "&idgroup=" + idGroup + "&sms=" + msg + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendSmsToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime=""):
    clase = "sms"
    metodo = "sendsmstogroupfromtemplate"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendEmail(username, password, subject, to, message, scheduledatetime=""):
    clase = "email"
    metodo = "sendemail"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&subject=" + subject + "&to" + to + "&email=" + message + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendEmailFromTemplate(username, password, to, idTemplate, params, scheduledatetime=""):
    clase = "email"
    metodo = "sendemailfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendEmailToGroup(username, password, subject, idGroup, msg, scheduledatetime=""):
    clase = "email"
    metodo = "sendemailtogroup"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&subject=" + subject + "&idgroup=" + idGroup + "&email=" + msg + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendEmailToGroupFromTemplate(username, password, idGroup, idTemplate, scheduledatetime=""):
    clase = "email"
    metodo = "sendemailtogroupfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&idgroup=" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendVoice(username, password, to, message, lang="", scheduledatetime=""):
    clase = "voice"
    metodo = "sendvoice"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&message=" + message + "&language=" + lang + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendVoiceFromTemplate(username, password, to, idTemplate, params, scheduledatetime=""):
    clase = "voice"
    metodo = "sendvoicefromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendVoiceToGroup(username, password, countryCode, idGroup, msg, scheduledatetime=""):
    clase = "voice"
    metodo = "sendvoicetogroup"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup=" + idGroup + "&message=" + msg + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def sendVoiceToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime=""):
    clase = "voice"
    metodo = "sendvoicetogroupfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup=" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def getDeliveryStatus(username, password, channel, ids):
    clase = channel
    metodo = "getdeliverystatus"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + "&messages=" + ids

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def getBalance(username, password):
    clase = "user"
    metodo = "getbalance"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password

    result = urllib2.urlopen(sUrl).read().decode('utf-8')
    return json.loads(result)


def isUser(username, password):
    res = getBalance(username, password)

    if res["status"] == "ERROR":
        return False
    else:
        return True