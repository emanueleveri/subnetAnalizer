def Ipsplit(ip):
    return ip.split('.')

def count(subnet):
    number=0
    for char in subnet:
        if(char=="1"):
            number+=1
    return number 

def Binary(ip):
    toReturn=""
    for i in range(0,4):
        toReturn+=bin(int(Ipsplit(ip)[i]))[2:].zfill(8)
        i+=1
    return toReturn

def check(ip1,ip2,Value):
    for i in range (0, Value):
        if ip1[i] == ip2[i]:
            return True
        else:
            return None
    
print("Subnet Analizer \n")
subnet=Binary(input("Insert a subnet mask "))
subcount=count(subnet)
ip=input("Insert an ip address ")
ip2=input("Insert another ip address ")
ip=Binary(ip)
ip2=Binary(ip2)
same=check(ip,ip2,subcount)
if same == True:
    print (" Two ip addresses are in the same subnet " )
else:
    print(" Two ip addresses are in different subnet " )
    
