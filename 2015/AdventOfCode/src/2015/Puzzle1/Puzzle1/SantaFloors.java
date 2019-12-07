import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;

public class SantaFloors {//use the rule ( is up 1 floor ) is down 1 floor
    public static int santaFloors(String instructions){
        int floor = 0;
        
        //String s = "((())";

        for (int i = 0; i < instructions.length(); i++){
            char c = instructions.charAt(i);        
            if(c == '('){
                floor++;
            }
            else if(c == ')'){
                floor--;
            }
        }
        return floor;
    }
    
    public static void testSantaFloors(){
        System.out.println('\f');
        String s = "(())))))";
        String content = null;
        
        try{//read in a file as one string
            content = new Scanner(new File("/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle1/PuzzleInput.txt")).useDelimiter("\\Z").next();
            System.out.println("**Got File!**");
        }catch(FileNotFoundException e){
            System.out.println("**Could not get File!**");
        }
        
        System.out.println(content);
        
        int floor = santaFloors(content);
        System.out.println(floor);
    }
}
