import java.util.List;

// if we write "public abstract class User" then User() will become a framework for student
// that means that we no longer be able to use User() as a normal class
public class User {
    private String _name;
    private String _membership = "Bronze";

    public static List<User> admins;

    public static void print_admins(){
        for(User user : admins) {
            System.out.println(user.get_name());
        }
    }

    public User(){ // this is so we can create a new User without being forced to pass in the name and the membership
    }
    public User(String name, String membership) {
        set_name(name);
        set_membership(membership);
    }

    public String toString(){
        return get_name() + " " + get_membership();
    }

    public boolean equals(User u){
        return (get_name() == u.get_name() && get_membership() == u.get_membership());
    }


    void set_name (String name){
        _name = name;
    }

    String get_name(){
        return _name;
    }
    void set_membership (String membership){
        _membership = membership;
    }

    void set_membership (Membership membership){
        _membership = membership.name();
    }

    String get_membership(){
        return _membership;
    }

    public enum Membership {
        Bronze, Silver, Gold;
    }

}
