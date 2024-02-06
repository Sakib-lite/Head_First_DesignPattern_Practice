public class Milk extends CondimentDecorator {

    public Milk(Bevarage bevarage) {
        super(bevarage);
    }

    public String getDescription() {
        return bevarage.getDescription() + ",Milk";
    }

    public double cost() {
        return bevarage.cost() + 5;
    }
}
