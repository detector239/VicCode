#include <iostream>

using namespace std;

class User
{
    // this section is automated private
    double age;// privet means that is only used in this struct or class
    public:
        int hight;
        string first_name;
        string last_name;
        string hair_color;
        double get_age(){
            age = hight/2.0;//this is example
            return age;
        }
        User(string firstname, string lastname)//this is a constructor
        {// the constructor will run when a new variable of this class type will be declared
            this->first_name = firstname;// we use 'this->' to call a variable from this class
            this->last_name = lastname;
        }
        ~User()// this is a destructor
        {// the destructor runs when a variable of this class type is deleted
            cout << "Destructor" << endl;
        }
};

int main()
{
    User user1("Ann", "Ver"), user2("Barry", "Honor");

    cout << user1.first_name << " " << user1.last_name << endl;
    cout << user2.first_name << " " << user2.last_name << endl;

    return 0;
}
