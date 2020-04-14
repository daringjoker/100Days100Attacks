import socket
import ssl

context = ssl.create_default_context()
url="www.facebook.com"
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
host=url
header ="""
GET / HTTP/1.1
Host: {}
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: {}
Sec-Fetch-Dest: document
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8


""".format(host,useragent)
# print(header)
# ip=socket.gethostbyname(url)
# handle=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# print(ip)
# handle.connect((url,80))
with socket.create_connection((url, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=url) as ssock:
        ssock.send(header.encode())
        msg=b""
        brkcount=0
        while True:
            print("Going on ...")
            newmsg=ssock.recv(1024)
            print(newmsg, len(newmsg))
            msg=msg+newmsg
            if b'\r\n\r\n' in newmsg: 
                brkcount+=1
            if newmsg=="" or len(newmsg)<1024:
                break
        print(msg)
            
