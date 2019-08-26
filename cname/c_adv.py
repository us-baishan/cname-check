
import dns.resolver
import threading
import time



resolver = dns.resolver.Resolver()
resolver.lifetime = resolver.timeout = 20.0
