# echo-server

Assumptions made:
1. "Callable from command line" means able to execute the script from the command line
2. "Log messages to a file" means to write received messages to a local file from the server side
3. "Socket location and log file location determined by configuration file" means default settings should be loaded
in from a configuration file, although environment variables can be used to override defaults

Process I used to test these scripts:
1. Navigate to the directory containing these files (primarily echo-server.py and echo-client.py).
2. Open two new terminal windows and run 'python echo-server.py' and 'python echo-client.py' respectively.
3. Type messages into the client window and watch messages be printed and logged on the server side.
