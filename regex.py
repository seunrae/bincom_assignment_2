import re;

url = open("baby2008.html", "r", encoding="utf-8")
names = url.read();
baby_names = re.findall('<td>([a-zA-Z]+)</td>', names);

for name in baby_names:
	print(name);




