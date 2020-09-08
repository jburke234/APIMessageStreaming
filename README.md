APIMessageStreaming

The goal of this project was to gain a better understanding of how gRPC and Docker are used. 

# Architecture 

![](https://i.ibb.co/N308QTP/arch-Diagram.png)

# App Explanation 

The Server microservice reads the ToTheLighthouse.txt novel line by line, splits the line into individual words and then using gRPC streaming sends each word to the Client microservice. Here each word is analyzed and the results are sent to a redis database. The Web microservice then displays this information using flask.


# Streaming 

![](https://i.ibb.co/km6fZxM/running3.png)


# Webpage

![](https://i.ibb.co/9qYtWmX/running1.png)

![](https://i.ibb.co/bvhf3rk/running2.png)
