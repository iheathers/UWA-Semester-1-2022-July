import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
/**
 * The test class MarksAnalyserTest.
 *
 * @author  Rachel CO
 * @version March 2013 (revised 2019)
 */
public class MarksAnalyserTest
{
    MarksAnalyser java1001, emptyclass; // class lists
    Student lewiscarroll; // example student used for testing

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @Before
    public void setUp()
    {
        emptyclass = new MarksAnalyser(); // no students in this class

        java1001 = new MarksAnalyser();
        //one way of adding students
        lewiscarroll = new Student("Lewis Carroll",75);
        java1001.joinClass(lewiscarroll);
        //another way of doing it
        java1001.joinClass(new Student("Ada Lovelace",99));
        java1001.joinClass(new Student("Bill Gates",45));
        java1001.joinClass(new Student("Claude Shannon",96));
        java1001.joinClass(new Student("Mickey Mouse",5));
        java1001.joinClass(new Student("Alan Turing",99));
    }

    /**
     * test size is returned correctly
     */
    @Test
    public void testNumberOfStudents() 
    {
        assertEquals(6, java1001.numberOfStudents());
        java1001.joinClass(new Student("Minnie Mouse",60));
        assertEquals(7, java1001.numberOfStudents());
        assertEquals(0, emptyclass.numberOfStudents());
    }

    @Test
    public void testFindStudentIsThere() 
    {
        assertEquals(lewiscarroll, java1001.findStudent("Lewis Carroll"));
    }

    @Test
    public void testFindStudentNotThere() 
    {
        assertEquals(null, java1001.findStudent("Queen Elizabeth"));
    }

    @Test
    public void testShowCourseNames()
    {
        String answer = "Lewis Carroll\n" +
                        "Ada Lovelace\n" +
                        "Bill Gates\n" +
                        "Claude Shannon\n" +
                        "Mickey Mouse\n" +
                        "Alan Turing\n";
        assertEquals(answer, java1001.showCourseNames());
    }

    @Test
    public void testShowCourse()
    {
        String answer = "Lewis Carroll, 75\n" +
                        "Ada Lovelace, 99\n" +
                        "Bill Gates, 45\n" +
                        "Claude Shannon, 96\n" +
                        "Mickey Mouse, 5\n" +
                        "Alan Turing, 99\n";
        assertEquals(answer, java1001.showCourse());
    }

    /**
     * normal maximum test
     */
    @Test
    public void testMaximumNormal() {
        assertEquals(99, java1001.maximum());
    }

    @Test
    public void testAverageNormal()  {
        //special test condition when comparing doubles
        //final param delta is the maximum delta between expected 
        //and actual for which both numbers are still considered equal
        assertEquals(69.83, java1001.average(), 0.01); 
    }

    /**
     * there are students at or above the given threshold
     */
    @Test
    public void testStarStudentsPositive() {
        ArrayList<Student> stars = new ArrayList<Student>();
        stars = java1001.starStudents(75);
        assertEquals(4, stars.size());
        assertTrue(stars.contains(lewiscarroll));
    }

    /**
     * no students at or above the threshold
     * returns an empty array list, not null
     */
    @Test
    public void testStarStudentsNegative() {
        assertEquals(0, java1001.starStudents(100).size());
    }

    /**
     * histogram test
     */        
    @Test
    public void testHistogram() {
        String s80plus = "80..100: ***\n"; //3 students with marks >= 80
        String s60plus = "60..79 : *\n";
        String s40plus = "40..59 : *\n";
        String s20plus = "20..39 : \n";
        String s0plus  = "00..19 : *\n";

        String hstr = s80plus + s60plus + s40plus + s20plus + s0plus;

        assertEquals(hstr,java1001.printHistogram());
    }
}
