import java.util.*;

/**
 * This class contains static methods that play Wordle using a simple artificial
 * intelligence.
 *
 * @author 23771397 (Pritam Suwal Shrestha) AND 23728208 (Trieu Huynh)
 */
public class WordleAI {
    private WordleAI() {
        // Constructor is private because all methods are static
        // and instances of WordleAI should not be created
    }

    /**
     * Returns true if guess contains the letter c and false otherwise.
     */
    public static boolean guessContains(String guess, char c) {
        return guess.contains("" + c);
    }

    /**
     * Returns true if newGuess is consistent with a previousGuess and its result
     * and false otherwise.
     * 
     * The parameter previousGuess is a previous Wordle guess made by the AI.
     * The parameter result is the result of the guessWord method in WordleGame.
     * The parameter newGuess is a potential new word to guess.
     * 
     * A newGuess is consistent with the previousGuess and result if they can be
     * explained by newGuess being the secret word. That is, newGuess should not
     * contradict results from previous guesses.
     * 
     * For example, suppose we have previousGuess="dxaxx" and the result="*_.__",
     * then newGuess="dairy" or newGuess="dzzza" would return true, but
     * newGuess="testa" or newGuess="dxiry" would be false.
     * This is because only newGuess="dairy" or newGuess="dzzza" could have been the
     * secret word
     * for previousGuess="dxaxx" to get result="*_.__"
     * 
     * HINT: Can you use a new WordleGame(...) somehow?
     */
    public static boolean isConsistent(String previousGuess, String result, String newGuess) {
        // Step 1: If result is an empty String
        if (result.length() == 0) {
            return false;
        }

        // Step 2: Loops through the result String to determine whether the newGuess is
        // not consistent with
        // the previousGuess.
        for (int i = 0; i < result.length(); i++) {
            // Step A: If the result is '*' for that character of previousGuess, then that
            // same character
            // should be in the newGuess at the same position.
            if (result.charAt(i) == '*' && newGuess.charAt(i) != previousGuess.charAt(i)) {
                return false;
            }
            // Step B: If the result is '_' for that character of previousGuess, then that
            // character
            // should not be in the newGuess.
            if (result.charAt(i) == '_' && guessContains(newGuess, previousGuess.charAt(i))) {
                return false;
            }
            // Step C: If the result is '.' for that character of previousGuess, then that
            // character
            // should be in the newGuess but in a different position.
            if (result.charAt(i) == '.' && (!guessContains(newGuess, previousGuess.charAt(i))
                    || previousGuess.charAt(i) == newGuess.charAt(i))) {
                return false;
            }

        }
        // Step 3: If consistent
        return true;
    }

    /**
     * Returns true if result contains only '*' characters
     * and false if it contains a non-'*' character.
     */
    public static boolean isAllStars(String result) {
        // Step 1: If result is an empty String
        if (result.length() == 0) {
            return false;
        }
        // Step 2: Loops through result and returns false if any of the characters are
        // not *
        for (int i = 0; i < result.length(); i++) {
            if (result.charAt(i) != '*') {
                return false;
            }
        }

        return true;
    }

    /**
     * This method runs the AI algorithm.
     * Given a dictionary and a game, makes a series of calls to
     * game.guessWord(word)
     * to find the secret word in game.
     * Returns an ArrayList containing the words in the order they were guessed.
     * If the secret word could not be found, returns null.
     * 
     * The AI algorithm is very specific!
     * It uses a simple strategy similar to one you may have used when playing
     * Wordle.
     * 
     * The AI starts by guessing the the lexicographicaly smallest word.
     * 
     * Then, for every guess after that, the AI guesses a word that does not
     * contradict any previous
     * results it has seen. That is, it makes guesses that are consistent (see
     * isConsistent)
     * with all guesses made so far.
     * 
     * If there are multiple possible guesses that are consistent, then the AI
     * will pick the lexicographically smallest option.
     * 
     * WordleGame has been modified to only allow 6 guesses. After this, it will
     * return an
     * empty string "".
     * 
     * If the game ends because the AI has run out of guesses, then findWord returns
     * null.
     * Otherwise, findWord returns once it has made a correct guess. This can
     * be checked using the isAllStars method above. In this case, a list of the
     * AI's
     * guesses in the order they were made is returned.
     * 
     * HINT 1: You will almost certainly need to read the unit test and use the
     * debugger for this method.
     * HINT 2: See Collections.sort in the Java class libraries for lexicographical
     * ordering.
     */
    public static ArrayList<String> findWord(WordleDictionary dictionary, WordleGame game) {
        // Step 1: Initialises new ArrayLists to keep track of the words guessed and the
        // respective results of
        // the guesses.
        ArrayList<String> wordsGuessed = new ArrayList<>();
        ArrayList<String> resultsGuessed = new ArrayList<>();
        // Step 2: Creates ArrayList of words in the dictionary that are the same length
        // as the secretWord.
        ArrayList<String> wordsWithLength = dictionary.getWordsWithLength(game.getWordLength());
        // Step 3: Sorts wordsWithLength in ascending lexicographic order.
        Collections.sort(wordsWithLength);

        if (wordsWithLength.size() == 0) {
            // Step 4: If there are no words in the dictionary with the same length as the
            // secretWord.
            return null;
        } else {
            // Step 5: Guesses the first word.
            resultsGuessed.add(game.guessWord(wordsWithLength.get(0)));
            wordsGuessed.add(wordsWithLength.get(0));
        }
        for (int j = 1; j < wordsWithLength.size(); j++) { // start from second word already guessed with the first
                                                           // word.
            String newGuess = wordsWithLength.get(j);
            // Step A: Checks whether a word is consistent with all the previously guessed
            // words.
            boolean allConsistent = true;

            for (int i = 0; i < wordsGuessed.size(); i++) {
                if (!isConsistent(wordsGuessed.get(i), resultsGuessed.get(i), newGuess)) {
                    allConsistent = false;
                }
            }
            // Step B: Makes a guess with the word if it is consistent with all previous
            // guesses.
            if (allConsistent) {
                String result = game.guessWord(newGuess);
                wordsGuessed.add(newGuess);
                resultsGuessed.add(result);
            }
            // Step C: Checks if the correct word has been guessed.
            if (isAllStars(resultsGuessed.get(resultsGuessed.size() - 1))) {
                return wordsGuessed;
            }
            // Step D: Checks if the AI has run out of guesses.
            if (resultsGuessed.get(resultsGuessed.size() - 1) == "") {
                return null;
            }
        }
        return null;
    }
}
