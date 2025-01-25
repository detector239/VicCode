#include <iostream>

int main()
{
    std::string greeting = "Hello";
    std::cout << greeting[0]/*here we call a specific character from a string*/ << std::endl;

    std::string complete_greeting = greeting + " there";
    complete_greeting += "!";

    std::cout << complete_greeting + " How are you?" << std::endl;

    std::cout << complete_greeting.length() << std::endl;

    complete_greeting.insert(3, "     "); // .insert(where to insert, what to insert)
    std::cout << complete_greeting << std::endl;

    complete_greeting.erase(3, 5);// .erase(where to erase. how many characters to erase)
    std::cout << complete_greeting << std::endl;

    complete_greeting.replace(complete_greeting.find("there")/*it will return the position of the first character*/, 5, "here");// .replace(from where will replace, how many characters will replace, what will replace)
    std::cout << complete_greeting << std::endl;

    std::cout << complete_greeting.substr(0, 5) << std::endl;//from subtraction: .substr(from where to subtract, how many characters to subtract)

    std::cout << complete_greeting.find_first_of("e") << std::endl;// it will find the first character that we indicate, in the string
    return 0;
}
