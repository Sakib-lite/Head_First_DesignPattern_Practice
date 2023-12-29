public class ModelDuck extends Duck {


    public ModelDuck() {
        flyBehavior = new FlyWithWings();
        quackBehavior = new QuackMute();
    }

    @Override
    public void display() {
        System.out.println("This is model duck");
    }
}
