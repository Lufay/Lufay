extern int abc;

void func() {
	printf("hi, func in so\n");
}

void testing() {
	func();
	abc = 1;
}
