all: clean
	cc -o client_sub client_sub.c -Wall -lzmq
	cc -o serv_pub  serv_pub.c -Wall -lzmq

clean:
	-rm -f serv_pub client_sub
