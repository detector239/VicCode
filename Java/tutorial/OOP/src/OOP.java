public class OOP {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        User u = new User();
        u.name = "Victor";
        u.membership = "Gold";

        User u2 = new User();
        u2.name = "Caleb";
        u2.membership = "Platinum";
        System.err.println(u.name + " " + u2.membership);
    }
}