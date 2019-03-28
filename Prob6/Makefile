EXEC=prob6
CC=c99
CFLAGS= -c -g -Wall
OBJECTS=prob6.o

all: $(EXEC)
	make clean
$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXEC) $(LIB)

prob2.o:
	$(CC) $(CFLAGS) prob6.c
clean:
	rm -f *.o
