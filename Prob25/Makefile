EXEC=prob15
CC=c99
CFLAGS= -c -g -Wall
OBJECTS=prob15.o
LIB=-lm

all: $(EXEC)
	make clean
$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXEC) $(LIB)

prob2.o:
	$(CC) $(CFLAGS) prob15.c
clean:
	rm -f *.o
