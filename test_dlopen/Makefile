OBJ = test testlib.so

LDMODULE = -rdynamic
#LDMODULE = -Wl,-E
SHARE = -Wl,-Bsymbolic

all : $(OBJ)

clean:
	rm -f $(OBJ) 

test : main.c
	gcc $(LDMODULE) -g -ldl main.c -o $@

testlib.so : testlib.c
	gcc -fPIC -shared $(SHARE) -g testlib.c -o $@
