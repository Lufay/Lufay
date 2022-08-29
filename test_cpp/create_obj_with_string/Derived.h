#ifndef __DERIVED_H__
#define __DERIVED_H__

#include "Base.h"
#include "BaseFactory.hpp"

class Derived : public Base {
	REGISTER_DEC_TYPE(Derived);
public:
	virtual std::string callme();
	virtual ~Derived();
};


#endif
