#include <iostream>
#include <string>

int main()
{
    std::string name, guess_name;
    int age, guess_age;
    name = "Victor";
    age = 23;
    std::cout << "Guess my name: ";
    std::cin >> guess_name;
    std::cout << "Guess my age: ";
    std::cin >> guess_age;
    std::string forbidden_name = "Vic";
    if(guess_name == name && guess_age == age)
    {
        std::cout << "You guessed all question right!\n";
    }
    else if(guess_name == name || guess_age == age)
    {
        if(guess_name == name)
        {
            std::cout << "You guessed my name right!\n";
        }
        else
        {
            std::cout << "You guessed my age right!\n";
        }
    }
    else if(!(guess_name == forbidden_name))
    {
        std::cout << "You didn't guess any of the question right!\n";
    }
    else
    {
        std::cout << "You guessed the forbidden name!\n";
    }
    return 0;
}
