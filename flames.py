#....Flames App....

import json
from urllib.request import urlopen
from banner import banner
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
banner()

your_name = str(input(colored('ENTER YOUR NAME:', 'yellow')))
partner_name = str(input(colored('ENTER YOUR PARTNER NAME:', 'yellow')))
your_name = your_name.lower()
partner_name = partner_name.lower()
names = []
names.append(your_name)
names.append(partner_name)

API_KEY = "ck9EcFVFWJR5fnlntLEBTceHpkMsAlzHgHHU"

#........Gender API...............to Find The Gender.......

for name in names:
	req = "https://gender-api.com/get?key=" + API_KEY + "&name="+ name
	res = urlopen(req)
	data = res.read().decode('utf-8')
	dec = json.loads(data)
	print(Fore.GREEN+name+" is a "+dec['gender'])


#..........Spliting The Name's..............

def split(x):
	return list(x)

your_name_lst = split(your_name)
partner_name_lst = split(partner_name)


partner_len = len(partner_name_lst)

#..................Eliminating Same Character's.....................

for i in your_name_lst[:]:
		if i in partner_name_lst:
			your_name_lst.remove(i)
			partner_name_lst.remove(i)



len_your_name = len(your_name_lst)
len_partner_name = len(partner_name_lst)

count = len_partner_name+len_your_name

flames = ['Friends','Love','Affection','Marriage','Enemies','Siblings']

#................Performing Flames...........................

while len(flames) > 1:
	splitIndex = (count % len(flames) - 1)  
	if splitIndex >= 0:
		right = flames[splitIndex + 1:]
		left = flames[ :splitIndex]  
		flames = right+left  
	else :  
	    flames = flames[ : len(flames)-1]  


if flames[0] == 'Friends':
	print(Fore.WHITE+'You both are Friends')
elif flames[0] == 'Love':
	print(Fore.BLUE+'Your both are in Love')
elif flames[0] == 'Affection':
	print(Fore.LIGHTYELLOW_EX+'Its just an Affection')
elif flames[0] == 'Marriage':
	print(Fore.LIGHTCYAN_EX+'You both get Married soon ;)')
elif flames[0] == 'Enemies':
	print(Fore.RED+'Ho no you both are Enemies :|')
elif flames[0] == 'Siblings':
	print(Fore.LIGHTBLUE_EX+'You both are best Siblings :)')

print("Relationship Status :", flames[0])  



