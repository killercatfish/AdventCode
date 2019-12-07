import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;
/**
 * Write a description of test here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class test {
    public static void testHouseVisit(){
        System.out.println('\f');
        
        HouseVisits houses = new HouseVisits();//create a housevisit object
        
        String content = null;
        
        try{//read in a file as one string
            content = new Scanner(new File("/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle3/Puzzle3Input.txt")).useDelimiter("\\Z").next();
            System.out.println("**Got File!**");
        }catch(FileNotFoundException e){
            System.out.println("**Could not get File!**");
        }
        
        houses.splitHouses(content);
        
        int visits = houses.getSize();
        
        System.out.println(visits);
        
        //houses.printHouses();
        
    }
}
