# Simple and explained TCP server and client
### Info
+ Standard server config binds to 127.0.0.1:43210.
+ Standard client config connects to 127.0.0.1:43210.
+ Both sends and receives data.

### Example output:

#### From server
###### Waiting connection...
###### Connection from ->  ('127.0.0.1', 63355)
###### Data received: Hello, server
###### Data sent: Hello, client

#### From client
###### Connected to: 127.0.0.1 43210
###### Data sent: Hello, server
###### Data received: Hello, client
