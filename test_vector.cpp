// constructing vectors
#include <iostream>
#include <vector>

void func(const std::vector<std::string>& vs) {
    std::cout << vs.size() << std::endl;
    for(std::vector<std::string>::const_iterator iter = vs.begin(); iter != vs.end(); ++iter) {
        std::cout << *iter << ' ';
    }
    std::cout << std::endl;
}

int main ()
{
  // constructors used in the same order as described above:
  std::vector<int> first;                                // empty vector of ints
  std::vector<int> second (4,100);                       // four ints with value 100
  std::vector<int> third (second.begin(),second.end());  // iterating through second
  std::vector<int> fourth (third);                       // a copy of third

  // the iterator constructor can also be used to construct from arrays:
  int myints[] = {16,2,77,29};
  std::vector<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );

  std::cout << "The contents of fifth are:";
  for (std::vector<int>::iterator it = fifth.begin(); it != fifth.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  
//  std::vector<std::string> sixth{"aaa", "bbb", "ccc"};
//  std::cout << sixth.size() << std::endl;
  
  const char * a[] = {"dd", "ee", "ff", "gg"};
  func(std::vector<std::string>(a, a+4));
  const char * b[] = {"h", "i", "j", "k", "l", "m", "n"};
  std::cout << sizeof b << std::endl;
  std::cout << sizeof *b << std::endl;
  func(std::vector<std::string>(b, b+7));

  return 0;
}
