#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <assert.h>

typedef void (*Func)(void);

int abc = -1;
void func() {
	printf("hello func in main\n");
}

int main(int argc, char *argv[]) {
	if(argc < 2 ) {
		fprintf(stderr, "Usage: %s ./lib.so\n", argv[0]);
		return 1;
	}
	void * testlib;
	Func testing_call;
	fprintf(stderr, "abc = %d\n", abc);
	if((testlib = dlopen(argv[1], RTLD_LAZY|RTLD_GLOBAL))
			!= NULL) {
		testing_call = (Func)dlsym(testlib, "testing");
		assert(testing_call);
		(*testing_call)();
		fprintf(stderr, "abc = %d\n", abc);
	}
	else {
		fprintf(stderr, "dlopen error: %s\n", dlerror());
	}
	return 0;
}
