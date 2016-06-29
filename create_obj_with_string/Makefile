BOOST_PATH = ~/software/boost_1_59_0

CXX = g++
CXXFLAGS = -g -fPIC -Wall -Wextra -pipe
LDFLAGS = -shared

INCPATH = -I $(BOOST_PATH)
#INCPATH = -I $(BOOST_PATH)/include
#LIBPATH = -L $(BOOST_PATH)/lib
#LIBS = -lboost

all : main assembly

main : main.cpp Base.o BaseFactory.hpp
	g++ $(INCPATH) -ldl -rdynamic main.cpp Base.o -o $@

assembly : Derived.so

Derived.so : Derived.cpp
	$(CXX) $(INCPATH) $(LDFLAGS) $(CXXFLAGS) $< -o $@

#%.o : %.cpp
#	$(CXX) $(CXXFLAGS) -c $< -o $@
Base.o : Base.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

.PHONY:clean
clean:
	rm -rf main Derived.so *.o
