import sys
from collections import defaultdict
from datetime import datetime

def scan_file(filename: str, user_dict: defaultdict) -> defaultdict:
    # Read file with user name and timestamp with comma delimiter
    with open(filename, "r") as infile:
        for line in infile:
            name, timestamp = line.split(',')
            user_dict[name].append(timestamp.strip()) # strip to remove newline char
    return user_dict


def check_consecutive_days(user_dict: defaultdict) -> list:
    # Holds users that visited on distinct days
    users = []
    
    for user in user_dict:
        if check_day_list(user_dict[user]):
            users.append(user)

    return users


def check_day_list(logins: list) -> bool:
    # Holds unique days user visited
    days = set()
    for login in logins:
        # Breaks down date timestamps to datetime object
        date = datetime.strptime(login, "%Y-%m-%d %H:%M:%S.%f")
        days.add(date.day)
    
    if len(days) >= 2:
        return True
    
    return False


if __name__ == '__main__':
    try:
        file_1 = sys.argv[1]
        file_2 = sys.argv[2]
    except:
        print("You must provide two log files to analyze")
        exit()

    userMap = defaultdict(list)
    scan_file(file_1, userMap)
    scan_file(file_2, userMap)
    print(check_consecutive_days(userMap))