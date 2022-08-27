import phonenumbers
from phonenumbers import geocoder

phoneNumber = input('Digite o telefone no formato: +551140028922\n')

phone_numbers = phonenumbers.parse(phoneNumber)

print(geocoder.description_for_number(phone_numbers, 'pt'))

