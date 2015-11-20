#include <iostream>
#include <fstream>
#include <sstream>
#include <openssl/md5.h>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream fin;
    if (argc < 2) {
        cerr << "ERR: missing filename !" << endl;
        exit(1);
    }
    fin.open(argv[1]);
    if ( ! fin.is_open()) {
        cerr << "ERR: open file " << argv[1] << " failed!" << endl;
        exit(1);
    }
    fin.seekg(0, ios_base::end);
    int len = fin.tellg();
    fin.seekg(0);
    char * buffer = new char[len];
    fin.read(buffer, len);
    fin.close();
//    cout.write(buffer, len);
    unsigned char md5[16];
//    MD5_CTX ctx;
//    MD5_Init(&ctx);
//    MD5_Update(&ctx, buffer, len);
//    MD5_Final(md5, &ctx);
    MD5(reinterpret_cast<const unsigned char*>(buffer), len, md5);
    ostringstream oss;
    for(int i=0; i<16; ++i) {
        oss << hex << static_cast<unsigned short>(md5[i]);
    }
    cout << oss.str() << "  " << argv[1] << endl;

    delete buffer;
}
