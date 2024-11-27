public class CoffeeShop {


    public static void main(String[] args) {
        Bevarage espresso = new Espresso();
        espresso = new Milk(espresso);
        espresso = new Sugar(espresso);

        System.out.println("Your order: " + espresso.getDescription());
        System.out.println("Cost: $" + espresso.cost());
    }
}
