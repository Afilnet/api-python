try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def sendSms(username, password, to, message, sender, scheduledatetime = "", output = ""):
    clase = "sms"
    metodo = "sendsms"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&from=" + sender + "&to=" + to + "&sms=" + message + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendSmsFromTemplate(username, password, to, idTemplate, params, scheduledatetime = "", output = ""):
    clase = "sms"
    metodo = "sendsmsfromtemplate"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendSmsToGroup(username, password, sender, countryCode, idGroup, msg, scheduledatetime = "", output = ""):
    clase = "sms"
    metodo = "sendsmstogroup"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&from=" + sender + "&countrycode" + countryCode + "&idgroup=" + idGroup + "&sms=" + msg + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendSmsToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime = "", output = ""):
    clase = "sms"
    metodo = "sendsmstogroupfromtemplate"
    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendEmail(username, password, subject, to, message, scheduledatetime = "", output = ""):
    clase = "email"
    metodo = "sendemail"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&subject=" + subject + "&to" + to + "&email=" + message + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendEmailFromTemplate(username, password, to, idTemplate, params, scheduledatetime = "", output = ""):
    clase = "email"
    metodo = "sendemailfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendEmailToGroup(username, password, subject, idGroup, msg, scheduledatetime = "", output = ""):
    clase = "email"
    metodo = "sendemailtogroup"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&subject=" + subject + "&idgroup=" + idGroup + "&email=" + msg + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendEmailToGroupFromTemplate(username, password, idGroup, idTemplate, scheduledatetime = "", output = ""):
    clase = "email"
    metodo = "sendemailtogroupfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&idgroup=" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendVoice(username, password, to, message, lang = "", scheduledatetime = "", output = ""):
    clase = "voice"
    metodo = "sendvoice"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&message=" + message + "&language=" + lang + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendVoiceFromTemplate(username, password, to, idTemplate, params, scheduledatetime = "", output = ""):
    clase = "voice"
    metodo = "sendvoicefromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&to=" + to + "&idtemplate=" + idTemplate + "&params=" + params + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendVoiceToGroup(username, password, countryCode, idGroup, msg, scheduledatetime = "", output = ""):
    clase = "voice"
    metodo = "sendvoicetogroup"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup=" + idGroup + "&message=" + msg + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def sendVoiceToGroupFromTemplate(username, password, countryCode, idGroup, idTemplate, scheduledatetime = "", output = ""):
    clase = "voice"
    metodo = "sendvoicetogroupfromtemplate"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + \
           "&countrycode=" + countryCode + "&idgroup=" + idGroup + "&idtemplate=" + idTemplate + \
           "&scheduledatetime=" + scheduledatetime + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def getDeliveryStatus (username, password, channel, ids, output = ""):
    clase = channel
    metodo = "getdeliverystatus"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password + "&messages=" + ids + "&output=" + output

    result = urllib2.urlopen(sUrl).read()
    return result


def getBalance(username, password):
    clase = "user"
    metodo = "getbalance"

    sUrl = "http://www.afilnet.com/api/http/?class=" + clase + "&method=" + metodo + "&user=" + username + \
           "&password=" + password

    result = urllib2.urlopen(sUrl).read()
    return result


def isUser(username, password):
    res = getBalance(username, password)

    if res.status == "ERROR":
        return False
    else:
        return True


def joke():
    return ('yoqse tio, no soi 100tifiko.')
