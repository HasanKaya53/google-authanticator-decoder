import onetimepass as otp
my_secret = 'HSWSBTN2AHMXA5REDFKWQBSY32B4QXIW'
my_token = otp.get_totp(my_secret)
print(my_token)