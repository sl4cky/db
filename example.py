import dns.resolver

#instead of a file this data will be taken from the database 
subdomains = ['vpn','dev','dev2','login','mail','media','a','b','www']

def findsub(domain):
    for subdomain in subdomains:
        dom = subdomain + "." + domain  
        subs = set()
        try: 
            answers = dns.resolver.query(dom, 'A')
            for rdata in answers:
                print dom 
        except dns.resolver.NXDOMAIN: 
            continue 
        
def main():
    # give the findsub function a domain to brute force subdomains 
    findsub('vg.no')

if __name__ == '__main__':
    main()
