import phonenumbers
from phonenumbers import geocoder

# Verificador de Telefone 
phone = input('Digite o telefone no formato: +5592994727249')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

