# -*- coding: utf-8 -*-
#sort ip 
import re
ip = "192.168.10.34 3.3.3.3 127.0.0.1 105.70.11.55"

#Firstly, complete ip with 0 so that they are equal length
ip = re.sub(r"(\d+)" , r"00\1" , ip)

#Secondly, save 3 useful number in every segment
ip = re.sub(r"0*(\d{3})",r"\1",ip)

#Thirdly, split ip into list element then do sorting
ip = re.split(' +',ip)
ip.sort()
ip_sorted= " ".join(ip)

#Finally return to the original form
ip_result = re.sub(r"0*(\d+)",r"\1",ip_sorted)
print(ip_result)
