# WireGuard

# Pre-requisites

## Access
Access as the root user by running:
```bash
sudo su
```

## Install:
Run
```bash
apt update 
apt install wireguard iptables net-tools qrencode
```

WireGuard installation will create a directory /etc/wireguard. To set the default file creation permission to 600, navigate to /etc/wireguard and change the umask to 077.

```bash
cd /etc/wireguard
umask 077
```

# Wireguard Server Setup

Next generate public and private key pair for the WireGuard server.
```bash
wg genkey | tee server-privatekey | wg pubkey > server-publickey
```
Get the content of the two files, by running the following command
```bash
tail -n +1 server-privatekey server-publickey
```
Store the output of the command in a place handy for copy and paste, as you will need to use it later. E.g output:

```bash
==> server-privatekey <==
GK+wX0XxaUY9rlQOHCdF3teRZttWXADMVZ5eLfQa80c=

==> server-publickey <==
vaXI0PRL35MNjlfZSQSrTBVzmJZhGtPv9OmeFZW0hF0=
```

Next create wg0.conf file. This file will be your WireGurad server configuration file. You can create the file by executing the following command.
```bash
nano wg0.conf
```

Next paste the following configuration settings in to the wg0.conf file. Make sure to replace the “PrivateKey” value with the private key you generated earlier.
```bash
[Interface]
Address = 10.16.0.1/32
ListenPort = 51820
PrivateKey = GK+wX0XxaUY9rlQOHCdF3teRZttWXADMVZ5eLfQa80c=
```

You can go ahead save the changes and close the wg0.conf file (Ctrl-x press Y press Enter). Then you can go ahead and add the WireGuard service to systemd so it starts automatically on boot. Start the WireGuard service and check its status to make sure it is running.
```bash
systemctl enable wg-quick@wg0
systemctl start wg-quick@wg0
systemctl status wg-quick@wg0
```

If everything is working you should get a message like this:
```bash
● wg-quick@wg0.service - WireGuard via wg-quick(8) for wg0
     Loaded: loaded (/lib/systemd/system/wg-quick@.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 2023-03-13 04:02:58 UTC; 13ms ago
       Docs: man:wg-quick(8)
             man:wg(8)
             https://www.wireguard.com/
             https://www.wireguard.com/quickstart/
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8
    Process: 2662 ExecStart=/usr/bin/wg-quick up wg0 (code=exited, status=0/SUCCESS)
   Main PID: 2662 (code=exited, status=0/SUCCESS)
        CPU: 31ms
```

## General structure of a full WireGuard Server configuration file:
```bash
[Interface]
Address = 10.16.0.1/32
ListenPort = 51820  [***Default-Open-Port-At-VM***]
PrivateKey = IMOqV+g9o [***Server-Private-Key***] Of/DKpbLH2E=

PreUp = sysctl -w net.ipv4.ip_forward=1

!!!!!!!!!!!!!  =================    REPLACE *etho* with your net run: ip link  =============== !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o eth0 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o eth0 -j ACCEPT

Client 1:
[Peer]
PublicKey = lZGzk07P2y9Otd [***CLIENT-PUBLIC-KEY***] iznMxPRGPlqXt9aGo=
AllowedIPs = 10.16.0.2/32 [***WARNING-SET-AT-/32-IN-SERVER***] # At /24 in client

Client 2:
[Peer]
PublicKey = 
AllowedIPs = 10.16.0.3/32
```

## Server Blueprint:
```bash
Address = 10.16.0.1/32
ListenPort = 51820
PrivateKey = Server-Priv-key
PreUp = sysctl -w net.ipv4.ip_forward=1

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o eth0 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o eth0 -j ACCEPT

[Peer]
PublicKey =
AllowedIPs = 10.16.0.2/32

[Peer]
PublicKey =
AllowedIPs = 10.16.0.3/32
```

# Client Setup

Once you have confirmed that WireGuard service is up and running. It is time to set up the first client. Start by creating a directory named after the client, and generating private and public key pair for the client. You can do it by running the following commands.

```bash
mkdir /etc/wireguard/[Client-Name]
cd /etc/wireguard/[Client-Name]
wg genkey | tee [Client-Name]-privatekey | wg pubkey > [Client-Name]-publickey
```
Copy and replace the " * " char with your client name:
```bash
mkdir /etc/wireguard/*
cd /etc/wireguard/*
wg genkey | tee *-privatekey | wg pubkey > *-publickey
```

Same as you did with the server’s key pair get the content of the two files and put it in a place handy for copy and paste, as you will need to use it later.

```bash
tail -n +1 *-privatekey *-publickey
```
Create client configuration file wg0-*.conf

```bash
nano wg0-*.conf
```

Copy and paste the following configuration settings in to the wg0-mac.conf file. Make sure to replace the “PrivateKey” value with the client’s private key you generated in the previous step, and the “PublicKey” under [Peer] with the server’s public key you generated earlier, also replace the value of “Endpoint” under [Peer] with your server’s public IP or domain name. Your wg0-mac.conf file should look similar to this

```bash
[Interface]
PrivateKey = CLIENT-PRIV-KEY                                        
Address = 10.16.0.2/24
DNS = 1.1.1.1, 8.8.8.8

[Peer]
PublicKey =  SERVER-PUB-KEY
AllowedIPs = 0.0.0.0/0
Endpoint = SERVER-PUB-IP:51820
```

Add the client configuration to the **Server Configuration**

```bash
nano /etc/wireguard/wg0.conf
```

Add the following configuration to the wg0.conf file, make sure to replace “PublicKey” with your client’s public key.
AllowedIPs = Place the same ip as the one in the client, replace the /24 for /32 as in the example bellow:

```bash
[Peer]
PublicKey = CL-PUB-KEY 
AllowedIPs = 10.16.0.2/32
```
At this point your wg0.conf configuration file should look similar to this

```bash
Address = 10.16.0.1/32
ListenPort = 51820
PrivateKey = Server-Priv-key
PreUp = sysctl -w net.ipv4.ip_forward=1

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o eth0 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.16.0.0/24 -o eth0 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o eth0 -j ACCEPT

[Peer]
PublicKey = Client-Public-Key
AllowedIPs = 10.16.0.2/32

```
Next, restart your WireGuard service and take a look at it with “wg” command.

```bash
systemctl restart wg-quick@wg0
wg
```
You should see an output similar to the one below. You can see that your server has wg0 interface that is listening on port 51820, and you are allowing connections to one client with public key and IP that should match the public key and IP of your client.
```bash
interface: wg0
  public key: vaXI0PRL35MNjlfZSQSrTBVzmJZhGtPv9OmeFZW0hF0=
  private key: (hidden)
  listening port: 51820

peer: S/rtqRg8TSscZfgLluwOcidGH8iKjtZEVjj68QtiCkM=
  allowed ips: 10.16.0.2/32
```

**Repeat the same steps for every user you add**

# Firewall Rules Configuration - References
**The network was setup as part of the content already added in the server setup part just for quick setup.**

After you confirm that you have iptables you will need to collect the name of your public facing network interface. You can do it by running the command below

`ip link`

As you can see from the output below I have loopback interface “lo”, and WireGuard interface the “wg0”, which leaves me with “enp0s3” to be my public facing interface. If you have left more than one interface after you rule out “lo” and “wg0” you will need to do some more digging, but if you are like me and only have three, whichever is left is most likely your public facing interface. Take a note of it as you will need it in the next step.
```bash
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 02:00:17:09:39:e8 brd ff:ff:ff:ff:ff:ff
5: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 8920 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/none 
```

Now that you have confirmed that iptables is installed, and you have the name of you public facing interface. Go ahead, open your server configuration file wg0.conf and enter the following configuration in the [Interface] section of the file. Make sure to replace every occurrence of “enp0s3” with the name of your public facing interface (“enp0s3” appears six times in the lines below).
```bash
PreUp = sysctl -w net.ipv4.ip_forward=1

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.16.0.0/24 -o enp0s3 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i enp0s3 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o enp0s3 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.16.0.0/24 -o enp0s3 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i enp0s3 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o enp0s3 -j ACCEPT
```
This configuration will allow IP forwarding, it will open UDP port 51820, make sure all outgoing packets are translated via the VPN, it will allow all traffic on wg0 interface, and allow packets to forward between the public Interface and the WireGuard every time WireGuard service is started as well as it will reverse everything mentioned above when WireGuard service is stopped.

At this point your wg0.conf file should be complete and it should look similar to this

```bash
[Interface]
Address = 10.16.0.1/32
ListenPort = 51820
PrivateKey = GK+wX0XxaUY9rlQOHCdF3teRZttWXADMVZ5eLfQa80c=

PreUp = sysctl -w net.ipv4.ip_forward=1

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.16.0.0/24 -o enp0s3 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i enp0s3 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o enp0s3 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.16.0.0/24 -o enp0s3 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i enp0s3 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o enp0s3 -j ACCEPT

[Peer]
PublicKey = S/rtqRg8TSscZfgLluwOcidGH8iKjtZEVjj68QtiCkM= 
AllowedIPs = 10.16.0.2/32
```

Next restart WireGuard service to apply all the changes, and if you don’t get any errors you are ready to test your VPN server by connecting to it with your client.
```bash
systemctl restart wg-quick@wg0
```

# Client Configuration on Mobile Device
In addition to creating an empty tunnel and pasting all the configuration in it Like we did earlier, or downloading the configuration file, mobile devices have the option to set up a new tunnel by scanning a QR code. To get a tool that will allow you to generate client configuration QR code run the following commands

Assuming you have installed the required qrencode you can use your client’s configuration file to generate QR code by running the following command.

```bash
qrencode -t ansiutf8 -l L < /etc/wireguard/mac/wg0-mac.conf
```