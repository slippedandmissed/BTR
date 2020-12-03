# Bypass The Router

Allows you to do "port forwarding" for TCP applications without needing access to your own router's settings.

## Usage:

You require a computer (virtual or otherwise) which can port forward to the general internet.

Clone the repo onto this computer wherever is convenient
```bash
git clone https://github.com/slippedandmissed/BTR
```
Change directory into the repo and run `start_servers.sh` providing two port numbers
```bash
cd BTR
./start_servers.sh {MIKE_PORT} {JASON_PORT}
```
for example:
```bash
./start_servers.sh 8080 9999
```
The MIKE_PORT will be used by the client on your own computer. The JASON_PORT will be used by people trying to access your application. Both must be port forwarded on this machine. If you want to stop the servers running, run `stop_servers.sh`
```bash
./stop_servers.sh
```

On your local machine (the one serving the application on the port you wish to forward), you must also clone the respository
```bash
git clone https://github.com/slippedandmissed/BTR
```
And then run `run_client.sh` providing the host and port of the application (the host is usually localhost if this is indeed the computer on which you are serving the application), as well as the host of the computer on which the server script is running, and the MIKE_PORT
```bash
cd BTR
./run_client.sh {APPLICATION_HOST} {APPLICATION_PORT} {MIKE_HOST} {MIKE_PORT}
```

for example, if your application was a Minecraft server running on port 25565 and the computer in which you are running the servers was at 31.88.5.3,
```bash
cd BTR
./run_client.sh 0.0.0.0 25565 31.88.5.3 8080
```

People can now connect to your application via the IP address of the machine on which you are running the servers, and the JASON_PORT, e.g. `31.88.5.3:9999`

## Notes
This does not currently support HTTP servers, just generic TCP.