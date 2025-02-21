import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier

def banner():
	print("""
 ███▄    █   ██████ ▒██   ██▒ █    ██  ██▓    
 ██ ▀█   █ ▒██    ▒ ▒▒ █ █ ▒░ ██  ▓██▒▓██▒    
▓██  ▀█ ██▒░ ▓██▄   ░░  █   ░▓██  ▒██░▒██░    
▓██▒  ▐▌██▒  ▒   ██▒ ░ █ █ ▒ ▓▓█  ░██░▒██░    
▒██░   ▓██░▒██████▒▒▒██▒ ▒██▒▒▒█████▓ ░██████▒
░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░
░ ░░   ░ ▒░░ ░▒  ░ ░░░   ░▒ ░░░▒░ ░ ░ ░ ░ ▒  ░
   ░   ░ ░ ░  ░  ░   ░    ░   ░░░ ░ ░   ░ ░   
         ░       ░   ░    ░     ░         ░  ░""")
banner()

try:
	text = input("\033[1;41mTips: masukkan nomor dengan kode negara kamu (+62)\033[0m\n\033[1;36m[*] Masukkan nomor: \033[0m")
	if text == "":
		print("\033[1;41mMasukin nomor!\033[0m")
		sys.exit()
			
	Key = "38c1da83c6f64a81aa87cd5179e25491"
	
	check_number = phonenumbers.parse(text)
	number_location = geocoder.description_for_number(check_number, "en")
	print(number_location)
	
	service_provider = phonenumbers.parse(text)
	print(carrier.name_for_number(service_provider, "en"))

	geocoder = OpenCageGeocode(Key)
	
	query = str(number_location)
	results = geocoder.geocode(query)
	
	lat = results[0]['geometry']['lat']
	lng = results[0]['geometry']['lng']
	print(lat, lng)
	
	map_location = folium.Map(location=[lat, lng], zoom_start=9)
	folium.Marker([lat, lng], popup=number_location).add_to(map_location)
	map_location.save("mylocation.html")
	
except KeyboardInterrupt:
	print("\033[1;41mThanks for use!\033[0m")
