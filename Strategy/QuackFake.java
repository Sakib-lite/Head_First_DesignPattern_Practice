public class QuackFake implements QuackBehavior {


    @Override
    public void quack() {
        System.out.println("Fake Quack");
    }
}
