public class Main {


    public static void main(String[] args) {

        King king = new King();
        king.display();
        king.attack();

        System.out.println("------");


        Queen queen = new Queen();
        queen.display();
        queen.attack();
        System.out.println("------");

        Troll troll = new Troll();
        troll.display();
        troll.attack();

        System.out.println("------");

        Knight knight = new Knight();
        knight.display();
        knight.attack();
        knight.setWeapon(new BowAndArrowBehavior());
        knight.attack();
    }
}
