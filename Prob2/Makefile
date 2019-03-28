EXEC=prob2
CC=c99
CFLAGS= -c -g -Wall
OBJECTS=prob2.o

all: $(EXEC)
	make clean
$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXEC) $(LIB)

prob2.o:
	$(CC) $(CFLAGS) prob2.c
clean:
	rm -f *.o
