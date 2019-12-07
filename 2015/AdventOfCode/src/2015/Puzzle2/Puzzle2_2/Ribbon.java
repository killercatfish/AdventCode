import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;
import java.util.Arrays;

public class Ribbon {
    public static int ribbon(String rectangle){
        int[] dimensions = getDimensions(rectangle);//get integer values.
        int[] perimeters = new int[3];
        //System.out.print("after " + dimensions[0] + " " + dimensions[1] + " " + dimensions[2]);
        
        perimeters[0] = 2*(dimensions[0]+dimensions[1]);
        perimeters[1] = 2*(dimensions[0]+dimensions[2]);
        perimeters[2] = 2*(dimensions[1]+dimensions[2]);
        int volume = dimensions[0]*dimensions[1]*dimensions[2];
        
        Arrays.sort(perimeters);
        
        //System.out.print(volume + " " + perimeters[0] + " " + perimeters[1] + " " + perimeters[2]);
        
        volume+=perimeters[0];
        
        //System.out.print(" Volume: " + volume);
        return volume;
    }
    
    private static int[] getDimensions(String rectangle){
        int[] dimensions = new int[3];
        
        String[] splitRectangle = rectangle.split("x");//splits the string into an array item after each x.
        
        //System.out.println("before " + splitRectangle[0] + " " + splitRectangle[1] + " " + splitRectangle[2]);
        
        dimensions[0] = Integer.parseInt(splitRectangle[0]);//convert each element to an integer
        dimensions[1] = Integer.parseInt(splitRectangle[1]);
        dimensions[2] = Integer.parseInt(splitRectangle[2]);
        
        return dimensions;//return the length, width, height
    }
    
    private static int getSum(String content){
        int total = 0;
        
        for(String word : content.split("\\s+")){//go through inputted lst 
            total += ribbon(word);//
        }
        
        return total;
    }
    
    public static void testRibbon(){
        System.out.println('\f');
        
        String rectangle = "10x5x5";
        
        String content = null;
        
        try{//read in a file as one string
            content = new Scanner(new File("/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle2/Puzzle2Input.txt")).useDelimiter("\\Z").next();
            System.out.println("**Got File!**");
        }catch(FileNotFoundException e){
            System.out.println("**Could not get File!**");
        }
       
        
        int sum = getSum(content);
        
        System.out.println(sum);
        
    }
}
