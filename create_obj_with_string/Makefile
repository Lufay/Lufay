CXX = g++
CXXFLAGS = -g -fPIC -Wall -Wextra -pipe
LDFLAGS = -shared
#BOOST_PATH = ~/liufei/third-64/boost/

#INCPATH = -I $(BOOST_PATH)/include
#LIBPATH = -L $(BOOST_PATH)/lib
#LIBS = -lboost

SO = Derived.so

all : main assembly

main : main.cpp Base.o BaseFactory.hpp
	g++ -ldl -rdynamic main.cpp Base.o -o $@

assembly : $(SO)

Derived.so : Derived.cpp
	$(CXX) $(LDFLAGS) $(CXXFLAGS) $< -o $@

%.o : %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

.PHONY:clean
clean:
	rm -rf main $(SO) *.o
