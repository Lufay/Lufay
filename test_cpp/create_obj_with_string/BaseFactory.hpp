#ifndef __BASE_FACTORY_H__
#define __BASE_FACTORY_H__

#include <string>
//#include <unordered_map>
#include <map>
#include <boost/shared_ptr.hpp>
#include "Base.h"

typedef boost::shared_ptr<Base> BasePtr;

//如何确保T是一种Base呢？
template<typename T>
BasePtr createT() {
	return BasePtr(new T());		//可以改用智能指针
}

class BaseFactory {
public:
	typedef BasePtr (*pfunc_get_base)();
//	static unordered_map<std::string, pfunc_get_base> map_func;
	static std::map<std::string, pfunc_get_base> map_func;

	static BasePtr create_sub_class(const std::string& class_name) {
//		auto iter = map_func.find(class_name);
		std::map<std::string, pfunc_get_base>::iterator iter = map_func.find(class_name);
		if ( iter == map_func.end() ) {
			throw "Can't find the class " + class_name;
		}
		return (iter->second)();
	}
};

template<typename T>
class RegisterFactory : public BaseFactory {
public:
	RegisterFactory(const std::string& class_name) {
		map_func.insert(std::make_pair(class_name, &createT<T>));
	}
};

#define REGISTER_DEC_TYPE(NAME) static RegisterFactory<NAME> reg
#define REGISTER_DEF_TYPE(NAME) RegisterFactory<NAME> NAME::reg(#NAME)

#endif
