
/**
 * Write a description of class GuessTheNumber here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class GuessTheNumber
{
    private int secretNumber;
    
    public GuessTheNumber(){
        java.util.Random r = new java.util.Random();
        secretNumber = r.nextInt(100) + 1;
        
    }
    
    public String checkMyGuess(int guess){
        if (guess > secretNumber)
            return "to high";
        else if (guess < secretNumber)
            return "too low";
        else return "well done!";
    }
}
