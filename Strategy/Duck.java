public abstract class Duck {


    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;


    public void setFlyBehavior(FlyBehavior fb) {
        flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb) {
        quackBehavior = qb;
    }

    public void performFly() {
        flyBehavior.fly();
    }

    public void performQuack() {
        quackBehavior.quack();
    }


    public abstract void display();

    public void swim() {
        System.out.println("All duck can swim");
    }


}
