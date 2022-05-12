import sys

import dns.resolver

try:
    arguments_list = sys.argv
    target = arguments_list[1]
except:
    print('Enter target IP or link.')
    exit(0)

wordlist = open('./wordlist.txt', 'r')
subdomains = wordlist.read().splitlines()
resolv = dns.resolver.Resolver()

for subdomain in subdomains:
    try:
        sub_target = f'{subdomain}.{target}'
        result = resolv.resolve(sub_target, 'A')
        for ip in result:
            print(sub_target, '->', ip)
    except:
        pass
