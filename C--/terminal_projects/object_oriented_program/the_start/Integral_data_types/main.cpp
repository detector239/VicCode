#include <iostream>
#include <climits>

int main()
{
    short a;
    int b;
    long c;
    long long d;
    // "unsigned" is without a sign like "-1" is signed and "1" is unsinged (only positiv values)
    // short <= int <= long <= long long
    unsigned short aa;
    unsigned int bb;
    unsigned long cc;
    unsigned long long dd;

    std::cout << "short: " << sizeof(short)*8 << " bits\n" << "limits: " << "MIN: " << SHRT_MIN << "; MAX: " << SHRT_MAX << std::endl << std::endl;
    std::cout << "int: " << sizeof(int)*8 << " bits\n" << "limits: " << "MIN: " << INT_MIN << "; MAX: " << INT_MAX << std::endl << std::endl;
    std::cout << "long: " << sizeof(long)*8 << " bits\n" << "limits: " << "MIN: " << LONG_MIN << "; MAX: " << LONG_MAX << std::endl << std::endl;
    std::cout << "long long: " << sizeof(long long)*8 << " bits\n" << "limits: " << "MIN: " << LLONG_MIN << "; MAX: " << LLONG_MAX << std::endl << std::endl;

    std::cout << "Ushort: " << sizeof(unsigned short)*8 << " bits\n" << "limits: " << "MIN: " << 0 << "; MAX: " << USHRT_MAX << std::endl << std::endl;
    std::cout << "Uint: " << sizeof(unsigned int)*8 << " bits\n" << "limits: " << "MIN: " << 0 << "; MAX: " << UINT_MAX << std::endl << std::endl;
    std::cout << "Ulong: " << sizeof(unsigned long)*8 << " bits\n" << "limits: " << "MIN: " << 0 << "; MAX: " << ULONG_MAX << std::endl << std::endl;
    std::cout << "Ulong long: " << sizeof(unsigned long long)*8 << " bits\n" << "limits: " << "MIN: " << 0 << "; MAX: " << ULLONG_MAX << std::endl << std::endl;
    return 0;
}
