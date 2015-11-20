#include <iostream>
#include <iterator>
#include <algorithm>
//#include <boost/lambda/lambda.hpp>

//using namespace boost::lambda;

std::function<int()> test(int x) {
    return [x]()mutable{return ++x;};
}

int main(int argc, char* argv[]) {
//    typedef std::istream_iterator<int> in;
//    std::for_each(in(std::cin), in(), [](int x){std::cout << (x * 3) << " ";});

    // test closure
    auto f = test(1);
    std::cout << f() << std::endl;
    std::cout << f() << std::endl;

    // test recursion
    std::function<int(int)> fib = [&fib](int n){if(n<2) return 1;return n+fib(n-1);};
    std::cout << fib(4) << std::endl;
}
