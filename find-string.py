def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if sub_string in string[i:i+sub_len]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
