#include <iostream>
#include "Base.h"

void Base::set_name(const std::string& nm) {
	name = nm;
}

std::string Base::callme() {
	return "Base::" + name;
}

Base::~Base() {
	std::cout << "Destroy Base::" << name << std::endl;
}
