#include <iostream>
#include <dlfcn.h>
#include "BaseFactory.hpp"

std::map<std::string, BaseFactory::pfunc_get_base> BaseFactory::map_func;

void load() {
	void * handle = dlopen("./Derived.so", RTLD_NOW|RTLD_GLOBAL);
	if ( !handle ) {
		std::cerr << dlerror() << std::endl;
		return;
	}
	std::cout << "Load OK!!!" << std::endl;

	BasePtr bp = BaseFactory::create_sub_class("Derived");
	if ( !bp ) {
		std::cerr << "Create sub class Derived failed !!!" << std::endl;
		return;
	}
	bp->set_name("you");
	std::cout << bp->callme() << std::endl;
}

int main() {
	load();
}
