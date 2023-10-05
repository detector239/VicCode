#include <iostream>
#include <string>

using namespace std;

struct Bamboo
{
    int hight;// this section is automated public
    int thickness;
    string name;
    string color;
    double get_age(){
        age = thickness/2.0;//this is example
        return age;
    }
private:
    double age;// privet means that is only used in this struct or class
};

int main()
{
    Bamboo bamboo1;
    bamboo1.hight = 2000;
    bamboo1.thickness = 36;
    bamboo1.color = "brown";
    bamboo1.name = "parent";
    cout << "hight1 = " << bamboo1.hight << endl;
    cout << "thickness1 = " << bamboo1.thickness << endl;
    cout << "name1 = " << bamboo1.name << endl;
    cout << "color1 = " << bamboo1.color << endl;
    cout << "age1 = " << bamboo1.get_age() << endl << endl;

    Bamboo bamboo2;
    bamboo2.hight = 4500;
    bamboo2.thickness = 28;
    bamboo2.color = "brown";
    bamboo2.name = "child";
    cout << "hight2 = " << bamboo2.hight << endl;
    cout << "thickness2 = " << bamboo2.thickness << endl;
    cout << "name2 = " << bamboo2.name << endl;
    cout << "color2 = " << bamboo2.color << endl;
    cout << "age2 = " << bamboo1.get_age() << endl;
    return 0;
}
