APIMessageStreaming

The goal of this project was to gain a better understanding of how gRPC and Docker are used. 

# Architecture 

![Architecture Diagram](https://imgur.com/HeQRxre)

# App Explanation 

The Server microservice reads the ToTheLighthouse.txt novel line by line, splits the line into individual words and then using gRPC streaming sends each word to the Client microservice. Here each word is analyzed and the results are sent to a redis database. The Web microservice then displays this information using flask.

![Running 1](https://ibb.co/jL4RD9K)

![Running 2](https://ibb.co/s1SBPFZ)
