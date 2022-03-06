# pip install phonenumbers
# Then from phonenumbers import timezone ,geocoder,carrier
# I have created a system using python which take input as number
# shows an detail of that number like country,timezone
# shows whether the enter number is of nationality or not
import phonenumbers
from phonenumbers import timezone, geocoder, carrier



contact = phonenumbers.parse('+919920963764')

timezone = timezone.time_zones_for_number(contact)
sim = carrier.name_for_number(contact, 'en')
country = geocoder.description_for_number(contact, 'en')
check = carrier.safe_display_name(contact, 'en', country)

print(check)
print(contact)
print(timezone)
print(sim)
print(country)
