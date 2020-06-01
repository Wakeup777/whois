def formatDate (data,site="none",i=1):
    dd = []

    try:
        dd.append(data['WhoisRecord']['domainName'])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registrarName'])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registryData']['status'])
    except KeyError:
        dd.append("none")
    try:
        dd.append(data['WhoisRecord']['registryData']['createdDate'][:10])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registryData']['expiresDate'][:10])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registryData']['registrant']['organization'])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registryData']['nameServers']['hostNames'][0])
    except KeyError:
        dd.append("none")

    try:
        dd.append(data['WhoisRecord']['registryData']['nameServers']['hostNames'][1])
    except KeyError:
        dd.append("none")

    text_out = str(i) + " "+ site+": "

    for i in dd:
        text_out = text_out + i + " "



    return text_out


