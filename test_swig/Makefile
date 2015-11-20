all:_test.so

test.o:test.c test.h
	gcc -fPIC -c $<

test_wrap.o:test.i test.o
	swig -python $<
	gcc -fPIC -c test_wrap.c -I/home/spider/Python/2.7.8/include/python2.7/

_test.so:test_wrap.o test.o
	gcc -shared $^ -o $@ #-lpython2.7 -L/home/spider/Python/2.7.8/lib/

.PHONY:clean
clean:
	@rm -f test.py*
	@rm -f _test.so test_wrap.* test.o
