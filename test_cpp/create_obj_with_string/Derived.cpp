#include <iostream>
#include "Derived.h"

REGISTER_DEF_TYPE(Derived);

std::string Derived::callme() {
	return "Derived::" + name;
}

Derived::~Derived() {
	std::cout << "Destroy Derived::" << name << std::endl;
}
