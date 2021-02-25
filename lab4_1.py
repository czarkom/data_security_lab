from passlib.hash import des_crypt
import string


target = "nr.Pp2GTcHqMc"
salt = "nr"
# print(des_crypt.hash("haslo",salt="Fb"))

for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            pw = a + b + c
            hs = des_crypt.hash(pw, salt=salt)
            if hs == target:
                print(f"Password is {pw}")
    print(f"Checking {a}...")
# password = sys.argv[1]
#
# salt = ''.join(random.sample(string.ascii_letters, 2))
#
# protected_password = crypt.crypt(password, salt)
# print( protected_password )