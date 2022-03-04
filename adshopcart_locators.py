from faker import Faker
fake = Faker(locale='en_CA')

adshopcart_url = 'https://advantageonlineshopping.com/#/'
new_username = fake.user_name()
new_password = fake.password()
new_email = fake.email()
new_firstname = fake.first_name()
new_lastname = fake.last_name()
full_name = f'{new_firstname }{" "}{new_lastname}'
phone = fake.phone_number()
city = fake.city()
address = fake.street_address().replace('\n', ' ')
postal_code = fake.postcode()
sentence = fake.sentence(nb_words=50)

