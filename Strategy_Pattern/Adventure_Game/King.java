class King extends Character {
    public King() {
        super(new SwordBehavior()); // King starts with a sword
    }

    void display() {
        System.out.println("I am the King");
    }
}
