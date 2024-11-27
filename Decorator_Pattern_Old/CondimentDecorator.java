abstract  public class CondimentDecorator implements Bevarage {

    protected Bevarage bevarage;

    public CondimentDecorator(Bevarage bevarage){
        this.bevarage=bevarage;
    }

    public String getDescription(){
        return bevarage.getDescription();
    }

}
