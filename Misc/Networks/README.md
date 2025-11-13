TCP - Transmission Control Protocol is considered connection oriented  
Utilizes three-way handshake  

Before a connection SYN and ACK packets need to be sent and received  

Client sends a SYN packet.  
Server sends a SYN, ACK packet  
Client sends ACK - positive aknowledgemenet system  

Window size - amount of information that can be send before a response is necessary. If no ACK is returned then the previous information is considered lost and is resent - RETRANSMISSION. They contain a PACKET NUMBER to track if anything is missing.  

Useful for unreliable or congested networks  

UDP - User Datagram Protocol - when reliable delivery isn't necessary - no aknowledgements and no protection  
connectionless  
UDP is far faster than TCP  
VOIP and streaming  

Layer 4 - Transport - uses a 16-bit number = port to facilitate endpoint communication  

TCP and UDP both open using ports  
Application open a port and wait for an incoming connection - referred to as listening  
80 - HTTP  
443 - HTTPS  

Well-known ports are <1024  
Ephemeral >1024 - Short-term communication by clients  

Specify source and destination port  
0 to 65535 - 16 bit number  

TCP cant use port 0 becauae it is reserved  

Source port is optional  
0 means none is used  

Binding an internet socket - per host a single binding on a port and IP combination  

Port already in use - means the application already has a binding in use  

Firewalls, Routers and Switches use ports  

Firewalls use ports to allow connections, recognize types of traffic via ports  
Routers and switches use ports for QoS - elevate traffic through network - help prioritize certain tasks  

Data Link and Network - Layers 2 and 3  
Data Link refers to communication on a common switched network  
Eacg devices used a Media Access Control address - 6 groups of 2 hexadecimal digits, usually sweparated by colons or hyphens. This layer deals only with switching so frames dont care about the encapsulated IP addresses they're transferring  

Layer 3: Sends info via IP addressing = Routers and routing  

Разпределени архитектурни модели  
Клиент сървър - задачите се разпределят межуд доставчици и консуматори  
Peer to peer - задачите се разпределят равномерно, всеки участник е едновременно и клиент и сървър  

# Видове клиенти

## Според функционалността
Rich & Thin

## Според семантиката(протокола)
Web - Browsers  
Mail - POP/SMTP  
FTP - File Transfer Protocol - Filezilla  
...

## Видове сървъри
File server  
DB server  
Mail server  
Name server - DNS  
FTP server  
Print server  
Game server  
Web server  
Application server  

# Client-server
## Предимства
Висока сигурност - Контролът за достъп до данни се осъществява на едно място - сървъра  
Консистентност на данни - Всички клиенти в даден момент достъпват едни и същи данни  
Промени в данните се разпространяват много бързо - при първо извикване от клиент към сървър  

## Недостатъци
Single Point of Failure - ако сървърът е down, никой в мрежата не може да комуникира  
Увеличаване на броя на клиентите води до намаляване на производителността  
70-95% от времето, през което работи сървърът е idle  

# Peer-to-peer
## Предимства
No single point of failure  
Няма намаляване на производителността при увеличаване на броя клиенти  

## Недостатъци
Проблеми със сигурността - има копия на данните из цялата мрежа
Риск от умишлена промяна на съдържанието и различни мерсии в различни възли  
Липса на контрол върху съдържанието и възможност за загуба на съдържание  
Трудна поддръжка  

![image](https://github.com/user-attachments/assets/a5be5338-ef3e-4545-a30f-113e80017e3a)

![image](https://github.com/user-attachments/assets/981f422b-e8e9-48bd-9315-6cd703471e4b)

## Network & Data link  
Network adapters  
IP address - Internet protocol  

## Transport layer
TCP
UDP

## Application layer
HTTPS  
FTP  

## Network adapter

Осъществява връзка между компютърна система и мрежа  
Физически или софтуерни  
Може да има повече от един физически и/или софтуерен мрежови адаптер  

## IP address
Всеки компютър има логически адрес  
IPv4 - 32bit IPv6 - 128bit  

![image](https://github.com/user-attachments/assets/1194d32e-e4a9-472f-bae7-65779f99ba4c)

1 компютър има 1 физически порт - по тази връзка се изпращат и получават фанни от/за всички приложения

![image](https://github.com/user-attachments/assets/61191023-de8a-4108-ac79-bcb647dd4da5)

## Sockets
UDP & TCP се имплементират чрез sockets  
Сокетите са крайните точки на двупосочна мрежова връзка (connection) между две приложения  
Всеки сокет се идентифицира чрез комбинация от IP адрес и номер на порт  

## UDP protocol
Позволява на пеиложенията да си разменят съобщения наречени датаграми чрез прост, connectionless модел на комуникация  
Съобщенията се нацепват на пакети. При УДП няма гаранция, че ще ги получите в същия ред  
Динамичен граф  
send/receive  
DNS  

## TCP Protocol 
Надгражда IP protocol (TCP/IP = TCP over IP)  

Запазва реда на пакетите, предава ги по надежден начин
