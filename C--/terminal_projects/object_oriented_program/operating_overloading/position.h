#include <iostream>

#ifndef USER_H
#define USER_H


class Position
{
    int z;
    public:
        int x = 3;
        int y = 4;

        Position(int x, int y);

        Position operator + (Position pos);

        void set_z(int z);

        bool operator == (Position pos);

        friend std::ostream& operator <<(std::ostream& output, Position pos);
        friend std::istream& operator >>(std::istream& input, Position& pos);
};// a friend functionis a function that is not from class User but has access to the privet members

std::ostream& operator <<(std::ostream& output, Position pos);

std::istream& operator >>(std::istream& input, Position& pos);



#endif // USER_H_INCLUDED
