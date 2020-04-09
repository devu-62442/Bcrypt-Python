import bcrypt
import time

passwd = input("Enter the data you want to Hash:")
iterations = int(input("Enter the number of rounds (less than 20):"))
start = time.time() 
salt = bcrypt.gensalt(rounds=iterations)
hashed = bcrypt.hashpw(passwd.encode('utf8'),salt)
print("Salt Value:", salt)
print("Hashed Value:", hashed)
end = time.time()

print("Time Taken:", end-start)

checkpasswd = input("Enter the data to check whether it matches the hash or not:")
if bcrypt.checkpw(checkpasswd.encode('utf8'),hashed):
	print("Data entered is correct. It Matched")
else:
	print("Does not match")

