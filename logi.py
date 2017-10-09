import jwt


encoded="bjfgjktghuinkjlgntirjgkltrnrj"

well=jwt.decode(encoded, 'secret')

print(well)