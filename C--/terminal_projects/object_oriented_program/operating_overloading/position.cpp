#include <iostream>
#include "position.h"

Position::Position(int x, int y)
{
    this->x = x;
    this->y = y;
}

Position Position::operator + (Position pos)
{
    Position new_pos(x+pos.x, y+pos.y);
    return new_pos;
}

bool Position::operator ==(Position pos)
{
    if(x == pos.x && y == pos.y) return true;
    else return false;
}

void Position::set_z(int z)
{
    this->z = z;
}

std::ostream& operator <<(std::ostream& output, Position pos)
{
    output << "x = " << pos.x << "; y = " << pos.y << "; z = " << pos.z;
    return output;
}

std::istream& operator >>(std::istream& input, Position& pos)
{
    input >> pos.x >> pos.y >> pos.z;
    return input;
}
