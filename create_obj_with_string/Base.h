#ifndef __BASE_H__
#define __BASE_H__

#include <string>

class Base {
protected:
	std::string name;
public:
	void set_name(const std::string& nm);
	virtual std::string callme();
	virtual ~Base();
};

#endif
