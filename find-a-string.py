def count_substring(string, sub_string):
    l = list(string)
    str_count = 0
    for i in range(0, len(string)):
        str_count += string.find(sub_string)
        string.lstrip(l[i])
    return str_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)