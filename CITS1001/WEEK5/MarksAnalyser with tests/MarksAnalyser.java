import java.util.ArrayList;

/**
 * MarksAnalyser stores a collection of Student records.
 * Complete the code missing from methods below for practice
 * at using ArrayList and for-each loops.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MarksAnalyser
{
    /*
     * Arbitrary length list of Student objects representing a 
     * specific group of students for a unit or lab class.
     */
    private ArrayList<Student> courselist;

    /**
     * Create an empty courselist
     */
    public MarksAnalyser()
    {
        // COMPLETE THIS 1
        courselist = new ArrayList<Student>();
    }

    /**
     * Add the provided student record to the end of the class list.
     * @param member The Student object to be added.
     */
    public void joinClass(Student student)
    {
        // COMPLETE THIS 2
        courselist.add(student);
    }

    /**
     * @return the number of students in the class list.
     */
    public int numberOfStudents()
    {
       // COMPLETE THIS 3
       return courselist.size();
    }

    /**
     * Generate a class list of student names (only) in a string, 
     * with a newline (\n) after each student.
     * @return String list of names separated by newlines
     */
    public String showCourseNames() 
    {   
        // COMPLETE THIS 4
        String classList = "";
        
        for (int i = 0; i < courselist.size(); i++){
            classList = classList + courselist.get(i).getName() + "\n";
        }
        
        return classList; 
    }

    /**
     * Generate a class list of comma-separated student names and marks in a string, 
     * with a newline (\n) after each student.
     * @return String list of names and marks separated by commas and newlines
     */
    public String showCourse() 
    {
        // COMPLETE THIS 5
        
        String studentInfo = "";
        
         for (int i = 0; i < courselist.size(); i++){
            studentInfo = studentInfo + courselist.get(i).getName() +  ", " + courselist.get(i).getMark() +  "\n";
        }
        return studentInfo; 
    }

    /**
     * Get a specific Student object record from the class list
     * @param String name of the student in the class list
     * @return Student object if the name is present or 
     * null if the name does not appear in the class list
     */
    public Student findStudent(String name) 
    {
        // COMPLETE THIS 6
        return null;
    }

    /**
     * Find the maximum mark, ignoring the student name.
     * @return int the largest mark in courselist.
     */
    public int maximum()
    {
        // COMPLETE THIS 7
        return -1; 
    }

    /**
     * Find the average mark for the class list.
     * @return double average value
     */
    public double average()
    {
        // COMPLETE THIS 8
        return 0.0; 
    }

    /**
     * Find all students with a mark of threshold or above.
     * @param int threshold only Students with a mark of at least threshold are returned
     * @return ArrayList of all Students who meet the cut off
     */
    public ArrayList<Student> starStudents(int threshold)
    {
        // COMPLETE THIS 9
        return null; 
    }

    /** 
     * CHALLENGE: only attempt this method after all of the other work and if you are confident. 
     * Generate a histogram of marks in courselist using strings of asterisks. 
     * Assume marks are in 0-100, so group marks into 00..19, 20..39, ..., 80..100. 
     * @result String with each bin represented by limits and *s, e.g. 00..19 : *** 
     */
    public String printHistogram()
    {
        // COMPLETE THIS 10
        return ""; 
    }
}
