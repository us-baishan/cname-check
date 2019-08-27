import dns.resolver

import socket
import ipwhois
# from ipwhois import IPWhois

#
# a=input('loop file')

# lines = [line.rstrip('\n') for line in open(a)]


def que(wee):
    try:
        answers = dns.resolver.query(wee, 'CNAME')
        print(' query qname:', answers.qname, ' num ans.', len(answers))
        for rdata in answers:
            print(' cname target address:', rdata.target)
            san = str(rdata.target)
            ll= san.split('.')
    except:
        print(wee + '  no cname found')

        ll=[]

    return ll
def dii(ff):
    with open(ff, "r") as ins:
        array1 = []
        dic = {}

        for line in ins:
            line = line.rstrip()

            s = line.split(' ')
            array1.append(s)

        for each in array1:
            dada = each[1]
            everyword = dada.split(',')
            for every in everyword:
                dic[every] = each[0]

    return dic





    # print(dic)




def main():
    import os
    cwd = os.getcwd()
    print(cwd)
    shh=cwd+'/wb_sample.txt'
    add=cwd+'/websites.txt'
    # a=input('input websites file:')

    dic = dii(shh)
    with open(add, "r") as webs:
        for web in webs:
            web = web.rstrip()
            shenmeweb= que(web)
            for ba in shenmeweb:
                for key in dic:
                    if key in ba:
                        print(' cdn provider:' + dic[key])
                    # else:
                    #     print('no provider shown ')






    # print(dic)

    bab = que(add)



main()



            # / Users / macuser / PycharmProjects / cname / wb_sample.txt




# myAnswers = dns.resolver.query("www.tmall.com", "A")
#
# for a in myAnswers:
#     print(a)
#     print(socket.getfqdn(str(a)))
#
# myAnswer = dns.resolver.query("www.tmall.com")
#
#
# for a in myAnswer:
#     print(a)
#
#     b=socket.getfqdn(str(a))
#
#     print(socket.getfqdn("47.246.22.236"))
#     print(b)
#
#

# def _test_server(self, server):
#         resolver = dns.resolver.Resolver()
#         resolver.lifetime = resolver.timeout = 20.0
#         try:
#             resolver.nameservers = [server]
#             answers = resolver.query('public-dns-a.baidu.com')  # test lookup a existed domain
#             if answers[0].address != '180.76.76.76':
#                 raise Exception('incorrect DNS response')
#             try:
#                 resolver.query('test.bad.dns.lijiejie.com')  # Non-existed domain test
#                 with open('bad_dns_servers.txt', 'a') as f:
#                     f.write(server + '\n')
#                 self.msg_queue.put('[+] Bad DNS Server found %s' % server)
#             except:
#                 self.dns_servers.append(server)
#             self.msg_queue.put('[+] Check DNS Server %s < OK >   Found %s' % (server.ljust(16), len(self.dns_servers)))
#         except:
#             self.msg_queue.put('[+] Check DNS Server %s <Fail>   Found %s' % (server.ljust(16), len(self.dns_servers)))