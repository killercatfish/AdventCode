import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;
/**
 * 
 */
public class NiceString {
    private static boolean isNice(String input){//check each of the 3 conditions for being nice
        if(!checkPairs(input)){//does it have at least 3 vowels?
            return false;
        }
        else if(!repeats(input)){//does it have double letters? grab 3 and check 1st and 3rd.
            return false;
        }
       
        return true;
    }
    
    private static boolean repeats(String input){
        //use check double...find a double then call it again from a different location after + 2 so no overlap
        for(int i = 0; i < input.length()-2; i++){
            String s = input.substring(i,i+3);
            char c = s.charAt(0);
            char d = s.charAt(2);
            //System.out.println(s + " " + c + " " + d);
            if(c == d){
                return true;
            }
        }
        return false;
    }
    
    private static boolean checkPairs(String input){//compare a char to the next char and see if they are the same
        //compare current index with next index.
        for(int i = 0; i < input.length()-1; i++){
            char c = input.charAt(i);
            char d = input.charAt(i+1);
            String s = new StringBuilder().append(c).append(d).toString();
            for(int j = i+2; j < input.length()-1; j++){
                char e = input.charAt(j);
                char f = input.charAt(j+1);
                String t = new StringBuilder().append(e).append(f).toString();
                if(s.equals(t)){
                    return true;
                }
            }
            
       }
        
        return false;
    }
    
    /*
    private static boolean checkVowels(String input){//check to see if there are at least 3 vowels.
        int vowelCount=0;
        
        for(int i = 0; i < input.length(); i++){
            char c = input.charAt(i);
            if(isVowel(c)){//checks if an individual char is a vowel
                vowelCount++;
            }
            //System.out.println("Vowel Count: " + vowelCount);
            if(vowelCount == 3){
                //System.out.println("Returning with vowel count of: " + vowelCount);
                return true;
            }
        }
        
        return false;
    }
    
    private static boolean isVowel(char c){//compare a char to the vowels in the vowel array
        for(int i = 0; i < vowels.length; i++){
            if(vowels[i] == c){
                return true;
            }
        }
        return false;
    }
    
    private static boolean checkDouble(String input){//compare a char to the next char and see if they are the same
        //compare current index with next index.
        for(int i = 0; i < input.length()-1; i++){
            char c = input.charAt(i);
            char d = input.charAt(i+1);
            if(c == d){
                //System.out.println("cd: " + c + d);
                return true;
            }
        }
        
        return false;
    }
    
    private static boolean checkDisallowed(String input){//combine a char with the next char, and see if this combo is in the disallowed list
        //compare current index with next and create string to compare to disallowed
        for(int i = 0; i < input.length()-1; i++){
            char c = input.charAt(i);
            char d = input.charAt(i+1);
            String s = new StringBuilder().append(c).append(d).toString();
            for(int j = 0; j < disallowed.length; j++){
                if(disallowed[j].equals(s)){
                    //System.out.println("Returning false, found disallowed: " + s);
                    return false;
                }
            }
        }
        //System.out.println("Returning true, no disallowed pairs.");
        return true;
    }
    */
    private static int countNice(String inputs){//count how may
        int niceCount = 0;
        for(String word : inputs.split("\\s+")){//go through inputted lst 
           if(isNice(word)){
               niceCount++;
               System.out.println(word + " is nice.");
            }
            else{
                System.out.println(" " + word + " is NOT nice.");
            }
        }
        return niceCount;
    }
    
    public static void test(){
        System.out.println('\f');
        /*
        String input = "dvszwmarrgswjxmb";
        
        if(isNice(input)){
            System.out.println("This is a nice string!");
        }
        else{
            System.out.println("This is a naughty string!");
        }
        */
        String content = null;
        
        try{//read in a file as one string
            content = new Scanner(new File("/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle5/Puzzle5Input.txt")).useDelimiter("\\Z").next();
            System.out.println("**Got File!**");
        }catch(FileNotFoundException e){
            System.out.println("**Could not get File!**");
        }
        
        int niceCount = countNice(content);
        
        System.out.println("There were " + niceCount + " nice.");
        
    }
}
