import java.util.*;

/**
 * Analyses a WordleAI by running experiments and computing statistics.
 * 
 * @author 23771397 (Pritam Suwal Shrestha) AND 23728208 (Trieu Huynh)
 */
public class WordleAIAnalyser {

    // Do not modify the fields of this class.
    private WordleDictionary dictionary;
    private int wordLength;
    // You should read but NOT modify the WordleExperimentResult class
    private ArrayList<WordleExperimentResult> experimentResults;

    /**
     * Constructor takes a dictionary and word length to run experiments with.
     */
    public WordleAIAnalyser(WordleDictionary dictionary, int wordLength) {
        this.dictionary = dictionary;
        this.wordLength = wordLength;
        this.experimentResults = new ArrayList<>();
    }

    /**
     * !!! DO NOT MODIFY !!!
     * This method has been implemented for you.
     */
    public ArrayList<WordleExperimentResult> getExperimentResults() {
        return experimentResults;
    }

    /**
     * Runs an experiment on a word and stores the result in experimentResults.
     * An experiment is the WordleExperimentResult from using the WordleAI on a
     * WordleGame
     * with word as the secret word.
     * 
     * No checks or guards are needed on the word parameter.
     * It is always assumed to be the right length and to come from the dictionary.
     */
    public void runExperiment(String word) {
        WordleGame game = new WordleGame(word);
        WordleExperimentResult experiment = new WordleExperimentResult(word, WordleAI.findWord(dictionary, game));
        experimentResults.add(experiment);
    }

    /**
     * Runs and stores experiments for each word in the dictionary with the right
     * length.
     * 
     * Should call runExperiment once for each word.
     */
    public void runExperimentsWithAllWords() {
        ArrayList<String> wordsWithLength = dictionary.getWordsWithLength(wordLength);

        for (String word : wordsWithLength) {
            runExperiment(word);
        }
    }

    /**
     * Runs and stores experiments for each word in the dictionary with the right
     * length.
     * 
     * Only uses words that are lexicographically between the start and finish.
     * A word is only used if it is the same as start or comes after AND it is the
     * same as finish or comes before.
     * 
     * For example, if our words are "act", "bat", "bet", "cat"
     * Then runExperimentsWithWordsBetween("baa", "caa")
     * would only run experiments for "bat" and "bet"
     * 
     * Should call runExperiment once for each word.
     * 
     * HINT: Recall the String compareTo method.
     */
    public void runExperimentsWithWordsBetween(String start, String finish) {
        String lowerStart = start.toLowerCase();
        String lowerFinish = finish.toLowerCase();
        ArrayList<String> wordsWithLength = dictionary.getWordsWithLength(wordLength);

        Collections.sort(wordsWithLength);

        for (String word : wordsWithLength) {
            String lowerWord = word.toLowerCase();

            // Step A: Run Experiment on words between start and finish
            if ((lowerStart.compareTo(lowerWord) <= 0) && (lowerFinish.compareTo(lowerWord) >= 0)) {
                runExperiment(word);
            }
        }
    }

    /**
     * Returns a list of all experiment words that were not solved by WordleAI.
     * The returned list of words should be in lexicographic order.
     * 
     * There may be duplicates in experimentResults.
     * This method should NOT return any duplicated words!
     * 
     * HINT 1: Remeber that findWord returns null when it cannot solve the word.
     * HINT 2: See Collections.sort and the ArrayList contains method.
     */
    public ArrayList<String> getUnsolvedWords() {
        ArrayList<String> unsolvedWords = new ArrayList<>();

        for (WordleExperimentResult result : experimentResults) {
            // Step A: Checks if WordleAI was unable to find the secret word (i.e. null was
            // returned instead of
            // a list of guesses), and if the word is a duplicate (i.e. already in the
            // unsolvedWords ArrayList).
            if ((result.getGuesses() == null) && (!unsolvedWords.contains(result.getWord()))) {
                unsolvedWords.add(result.getWord());
            }
        }
        Collections.sort(unsolvedWords);

        return unsolvedWords;
    }

    /**
     * Returns an array with length 26.
     * The entry at index [0] is the number of 'a' characters guessed over all
     * experiments by WordleAI.
     * The entry at index [1] is the number of 'b' characters.
     * ...
     * The entry at index [25] is the number of 'z' characters.
     * 
     * For example, if the WordleAI guessed the words "cat"+"hat" in one experiment
     * and "log"+"cat" in another:
     * The return array would be {3, 0, 2, ... }
     * Which means 3 'a' characters, 0 'b' characters, 2 'c' characters, and so
     * on...
     * 
     * HINT: Unsolved words have no guesses and should be skipped.
     */
    public int[] getGuessLetterFrequency() {
        int[] letterFreq = new int[26];

        for (WordleExperimentResult result : experimentResults) {
            // Step A: Skips unsolved words
            if (result.getGuesses() != null) {
                // Step B: Loops over ArrayList of guessed words
                for (String word : result.getGuesses()) {
                    // Step C: Loops over characters of guessed words
                    for (int i = 0; i < word.length(); i++) {
                        char c = word.charAt(i);
                        // Step D: Checks if c is a letter
                        if (Character.isLetter(c)) {
                            // Step E: Adds 1 to the count of the index corresponding to the letter
                            letterFreq[Character.toLowerCase(c) - 'a'] += 1;
                        }
                    }
                }
            }
        }
        return letterFreq;
    }

    /**
     * Returns an array of length 7.
     * 
     * The entry at index [0] is the number of times the WordleAI guessed a word
     * correctly after 1 guess.
     * The entry at index [1] is the number of times exactly 2 guesses were needed.
     * and so on.
     * The entry at index [6] is the number of times the WordleAI did not correctly
     * guess the word.
     */
    public int[] getNumGuessesFrequency() {
        int[] guessFreq = new int[7];

        for (WordleExperimentResult result : experimentResults) {
            if (result.getGuesses() == null) {
                guessFreq[6] += 1;
            } else {
                int numGuesses = result.getGuesses().size();
                guessFreq[numGuesses - 1] += 1;
            }
        }
        return guessFreq;
    }

    /**
     * Makes a string containing a histogram picture of getNumGuessesFrequency().
     * 
     * A possible histogram might look like this:
     * ..*....
     * ..*..*.
     * .**.**.
     * .*****.
     * ******.
     *
     * The stars form bars in a histogram, and the dots represent empty space.
     * This would correspond to a frequency table of {1, 3, 5, 2, 3, 4, 0}
     * Recall that the newline '\n' character can be used to encode a line break in
     * a string.
     * Note that return string should end with a newline '\n' character.
     * 
     * Because the numbers can be large, we use a bucketSize.
     * The height of a bar in the chart is 0 if the corresponding number is in the
     * inclusive range from 0 to bucketSize-1
     * The height is 1 if the number is in the inclusive range from bucketSize to
     * bucketSize*2-1
     * The height is 2 if the number is in the inclusive range from bucketSize*2 to
     * bucketSize*3-1
     * ...and so on.
     * 
     * The height of the histogram should be the same as the height of the tallest
     * bar.
     * 
     */
    public String makeHistogram(int bucketSize) {
        int[] numGuessFrequency = getNumGuessesFrequency();
        int maxFreq = numGuessFrequency[0];

        for (int i = 1; i < numGuessFrequency.length; i++) {
            if (numGuessFrequency[i] > maxFreq) {
                // Step A: Finds the number of guesses with the highest frequency.
                maxFreq = numGuessFrequency[i];
            }
        }

        // Step 2: The height of the tallest bar
        int maxBarHeight = maxFreq / bucketSize;

        // Step 3: Array holding the output of each row of the histogram
        String[] histogramRows = new String[maxBarHeight];
        Arrays.fill(histogramRows, "");

        String histogramString = ""; // The return String
        // Step 4: Creates each row of the histogram from the bottom row to the top row.
        for (int j = 0; j < histogramRows.length; j++) {
            for (int i = 0; i < numGuessFrequency.length; i++) {
                if (numGuessFrequency[i] >= bucketSize) {
                    histogramRows[j] += "*";
                    numGuessFrequency[i] -= (bucketSize);
                } else {
                    histogramRows[j] += ".";
                }
            }
            histogramRows[j] += "\n"; // Adds return carriage to the end of each row
        }

        // Step 5: Appends each row to the return String, starting from the top row and
        // ending at the bottom row.
        for (int k = histogramRows.length - 1; k >= 0; k--) {
            histogramString += histogramRows[k];
        }
        return histogramString;
    }

    /**
     * Prints the string made by makeHistogram(bucketSize)
     * 
     * The following code:
     * WordleAIAnalyser analyser = new WordleAIAnalyser(new WordleDictionary(), 5);
     * analyser.runExperimentsWithAllWords();
     * analyser.printHistogram(50);
     * 
     * 
     * Should print this to the terminal:
     * ...*...
     * ...*...
     * ...*...
     * ..**...
     * ..**...
     * ..***..
     * ..***..
     * ..***..
     * ..***..
     * .*****.
     */
    public void printHistogram(int bucketSize) {
        // No need to modify this method!
        // It has been provided for you.
        System.out.println(makeHistogram(bucketSize));
    }
}
