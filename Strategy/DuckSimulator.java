public class DuckSimulator {


    public static void main(String[] args) {

        MallardDuck mallardDuck = new MallardDuck();
        RedheadDuck redheadDuck = new RedheadDuck();
        RubberDuck rubberDuck = new RubberDuck();
        ModelDuck modelDuck = new ModelDuck();

        mallardDuck.display();
        mallardDuck.performQuack();
        mallardDuck.performFly();

        System.out.println("---------------");
        redheadDuck.display();
        redheadDuck.performQuack();
        redheadDuck.performFly();

        System.out.println("---------------");

        rubberDuck.display();
        rubberDuck.performQuack();
        rubberDuck.performFly();

        System.out.println("---------------");

        modelDuck.display();
        modelDuck.performQuack();
        modelDuck.setQuackBehavior(new QuackFake());
        modelDuck.performQuack();
        modelDuck.performFly();
        modelDuck.setFlyBehavior(new FlyRocketPowered());
        modelDuck.performFly();

    }
}
