import scapy.all as scapy
import csv

def scan(ip): # Create a function for getting the mac address of the target
    arp_request=scapy.ARP(psdt=ip) #  Creating  ARP request
    '''set destination mac to broadcast mac'''
    broadcast=scapy.Either(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request  # till now we created a ARP  request now by this we are making  a ARP packet
    # scapy has an option to collect only responded packets for more details please refer previous tutorial
    answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered_list
def output(data,option):
    list=[]
    for element in data:
        data_dic = {"IP":element[1].psrc,"Mac Address":element[1].hwsrc}
        if option == 1:
            print(f"[+] data_dic")
        list.append(data_dic)
    if option==2:
        csv_file(data=list)
def csv_file(data):
    # my data rows as dictionary objects
    mydict =data
    # field names
    fields = ["IP", 'Mac Address']
    # name of csv file
    filename = "newtworkscan"
    # writing to csv file
    
    with open(f"filename.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(mydict)

ip=input("[+] Enter the IP range to scan")
print('[+] Enter the below option for output')
while True:

    print("\t1.cmd\t\t2.CSV")
    option=input(int("select one :  "))
    if option ==1 or option ==2:
        output(data=scan(ip=ip),option=option)
        break
