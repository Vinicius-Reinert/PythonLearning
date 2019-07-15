import dns.resolver #import the module
myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
myAnswers = myResolver.query("google.com", "A") #Lookup the 'A' record(s) for google.com
for rdata in myAnswers: #for each response
    print rdata #print the data