# 0MQ_PubSub C/Python
A simple snippet sample of ZeroMQ Publisher/Subscriber for C and Python.  
  
  
Python:  
./serv_pub.py 9997 TOPIC_1 &  
./serv_pub.py 9998 TOPIC_21 TOPIC_22 &  
./serv_pub.py 9999 TOPIC_3 &  
./client_sub.py localhost 9997 TOPIC_1 &  
./client_sub.py localhost 9998 TOPIC_21 TOPIC_22 &  
./client_sub.py localhost 9998 TOPIC_2 &  
./client_sub.py localhost 9997 TOPIC_1 localhost 9999 TOPIC_3 &  
