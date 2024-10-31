public class Main {
    public static void main(String[] args) {
        String role = "moderator";
        switch (role) {
            case "admin":
                System.out.println("You are admin");
                break;
            case "moderator":
                System.out.println("You are moderator");
                break;
            default:
                System.out.println("You are not moderator");
        }
    }
}