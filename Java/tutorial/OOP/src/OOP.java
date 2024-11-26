import java.util.ArrayList;

public class OOP {
    public static void main(String[] args) {
        User u = new User("Victor", "Gold");
        User u2 = new User("Dan", "Gold");
        ArrayList<User> users = new ArrayList<User>();
        users.add(new User("Tom", "Silver"));

        User.admins = new ArrayList<User>();
        User.admins.add(u);
        User.admins.add(u2);

        for (int i=0; i < User.admins.size(); i++){
            System.out.println(User.admins.get(i).get_name());
        }
//        This is another method of writing this code
        for (User user : users) {
            System.out.println(user.get_name());
        }

        Student s = new Student();
        s.set_verified(true);
        System.out.println(s.get_verified());
        s.set_name("Gabriel");
        System.out.println(s.get_name());

        User.print_admins();

    }
}