public class Sugar extends CondimentDecorator {

    public Sugar(Bevarage bevarage) {
        super(bevarage);
    }


    public String getDescription() {
        return bevarage.getDescription() + ", Sugar";
    }

    public double cost() {
        return bevarage.cost() + 6;
    }
}
