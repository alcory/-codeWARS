def open_or_senior(data):
    outputList = []
    for i in data:
        if i[0] >= 55:
            if i[1] > 7:
                outputList.append("Senior")
            else:
                outputList.append("Open")
        else:
            outputList.append("Open")
    return outputList
