class Main {

    User user;


    public void setUser() {
        user = new User();
        user.setPassword(12);
    }
    
}


class User {
    int password;
    int[] tokens;
    boolean isAdmin;

    private static int ROLE;


    public int getPassword() {
        return password;
    }


    public int[] getTokens() {
        return tokens;
    }

    public int getRole() {
        ROLE = 0;
        if(isAdmin) {
            ROLE = 1;
        }
        return ROLE;
    }

    public void setPassword(int password) {
        this.password = password;
    }
}