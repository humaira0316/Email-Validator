def validate(str):
    PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._@'
    PERMITS2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    np = '._'
    count = 0
    l = len(str)
    a = str[0]
    b = str[l - 1]
    pos_rate = str.find("@")
    pos = str.rfind(".")
    slice_of_string = str[pos_rate - 1:pos]
    l1 = len(slice_of_string)
    for i in str:
        if i == "@":
            count += 1

        if i not in PERMITS:
            return False

            
    for j in slice_of_string:
        if (l1 >= 3 and l1 <= 12):
            if j in PERMITS2:
                boo_ft = 1
    if i in PERMITS:
        if (a not in np) and (b not in np):
            if count == 1 and (pos_rate >= 3 and pos_rate <= 24) and boo_ft == 1:
                return True

            else:
                return False
        else:
            return False
    else:
        return False


