class Knight extends Character {
    public Knight() {
        super(new AxeBehavior()); // Knight starts with an axe
    }

    void display() {
        System.out.println("I am the Knight");
    }
}