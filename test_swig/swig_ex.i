%module swig_ex
%{
    #define SWIG_FILE_WITH_INIT
    #include "swig_ex.h"
%}
int fact(int n);
