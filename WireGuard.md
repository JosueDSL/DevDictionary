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
apt install wireguard iptables net-tools
```

WireGuard installation will create a directory /etc/wireguard. To set the default file creation permission to 600, navigate to /etc/wireguard and change the umask to 077.

```bash
cd /etc/wireguard
umask 077
```

# Configure Wireguard Server
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

REPLACE *etho* with your net run: ip a

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.0.0.0/24 -o eth0 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o eth0 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.0.0.0/24 -o eth0 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o eth0 -j ACCEPT

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

PostUp = iptables -I INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -I POSTROUTING 1 -s 10.0.0.0/24 -o eth0 -j MASQUERADE; iptables -I INPUT 1 -i wg0 -j ACCEPT; iptables -I FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -I FORWARD 1 -i wg0 -o eth0 -j ACCEPT

PostDown = iptables -D INPUT -p udp --dport 51820 -j ACCEPT; iptables -t nat -D POSTROUTING 1 -s 10.0.0.0/24 -o eth0 -j MASQUERADE; iptables -D INPUT 1 -i wg0 -j ACCEPT; iptables -D FORWARD 1 -i eth0 -o wg0 -j ACCEPT; iptables -D FORWARD 1 -i wg0 -o eth0 -j ACCEPT

[Peer]
PublicKey =
AllowedIPs = 10.16.0.2/32

[Peer]
PublicKey =
AllowedIPs = 10.16.0.3/32
```