import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;

public class WrappingPaper {
    public static int wrappingPaper(String rectangle){
        int[] dimensions = getDimensions(rectangle);//get integer values.
        
        //System.out.print("after " + dimensions[0] + " " + dimensions[1] + " " + dimensions[2]);
        
        int area1 = dimensions[0]*dimensions[1];
        int area2 = dimensions[0]*dimensions[2];
        int area3 = dimensions[1]*dimensions[2];
        int surfaceArea = 2*(area1+area2+area3);
        
        if(area1 <= area2 && area1 <= area3){
            surfaceArea+=area1;
        }
        else if(area2 <= area1 && area2 <= area3){
            surfaceArea+=area2;            
        }
        else if(area3 <= area1 && area3 <= area2){
            surfaceArea+=area3;
        }
        System.out.print(" Surface Area: " + surfaceArea);
        return surfaceArea;
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
            System.out.print("word: " + word + " ");
            total += wrappingPaper(word);//
            System.out.println(" total: " + total);
        }
        
        return total;
    }
    
    public static void testWrappingPaper(){
        System.out.println('\f');
        
        String rectangle = "1x1x10";
        
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
