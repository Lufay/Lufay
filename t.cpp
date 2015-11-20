// istream_iterator example
#include <iostream>     // std::cin, std::cout
#include <vector>
#include <algorithm>
#include <iterator>     // std::istream_iterator

int main () {
//  double value1, value2;
//  std::cout << "Please, insert two values: ";

  typedef std::istream_iterator<int> iit;   // stdin iterator

  std::vector<int> c(1);
  std::cout << "before:" << std::endl;
  for_each(c.begin(), c.end(), [](int x) { std::cout << x << std::endl;});

  copy(iit(std::cin), iit(), back_inserter(c));//c.begin());

  std::cout << "after:" << std::endl;
  for_each(c.begin(), c.end(), [](int x) { std::cout << x << std::endl;});

  return 0;
}
