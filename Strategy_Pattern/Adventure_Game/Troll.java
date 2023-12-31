class Troll extends Character {
    public Troll() {
        super(new AxeBehavior()); // Troll starts with a club
    }

    void display() {
        System.out.println("I am the Troll");
    }
}