class Queen extends Character {
    public Queen() {
        super(new BowAndArrowBehavior()); // Queen starts with a bow and arrow
    }

    void display() {
        System.out.println("I am the Queen");
    }
}