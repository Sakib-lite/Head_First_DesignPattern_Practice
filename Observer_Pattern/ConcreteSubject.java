import java.util.ArrayList;

public class ConcreteSubject implements Subject {

    public ArrayList<Observer> observers = new ArrayList<>();
    public String state;


    @Override
    public void registerObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {

        observers.remove(o);
    }

    public void setState(String state){
        this.state=state;
        notifyObservers(state);
    }

    @Override
    public void notifyObservers(String message) {
      for (Observer observer: observers){
          observer.update(message);
      }
    }
}
