import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;
import java.util.*;

public class LightParser {
    
    public ArrayList<LightInstruction> parseInstructions(String fname){
        ArrayList<LightInstruction> parsedLI = new ArrayList<LightInstruction>(); //ArrayList of instructions
        
        String content = null;
        
        try{//read in a file as one string
            content = new Scanner(new File(fname)).useDelimiter("\\Z").next();
            System.out.println("**Got File!**");
        }catch(FileNotFoundException e){
            System.out.println("**Could not get File!**");
        }
        
        String lines[] = content.split("\\r?\\n");//Split by end of line, might not be perfect.
        
        for(int i = 0; i < lines.length; i++){
            LightInstruction parsed = parseLine(lines[i]);
            parsedLI.add(parsed);
        }
        
        return parsedLI;
    }
    
    private LightInstruction parseLine(String line){
        //Stringbuilder has some good methods--delete for instance
        StringBuilder input = new StringBuilder(line);
        //System.out.println(input);
        
        //y2
        int index = input.lastIndexOf(",");//get the index of the last comma
        int y2 = Integer.parseInt(input.substring(index+1));
        input.delete(index, input.length());
        //System.out.println(y2);
        
        //x2
        index = input.lastIndexOf(" ");//get the index of the last space
        int x2 = Integer.parseInt(input.substring(index+1));
        input.delete(index-8, input.length());
        //System.out.println(x2);
        
        //y1
        index = input.lastIndexOf(",");//get the index of the last comma
        int y1 = Integer.parseInt(input.substring(index+1));
        input.delete(index, input.length());
        //System.out.println(y1);
        
        //x1
        index = input.lastIndexOf(" ");//get the index of the last space
        int x1 = Integer.parseInt(input.substring(index+1));
        input.delete(index, input.length());
        //System.out.println(x1);
        
        //the instruction is all that is left.
        String instruction = input.toString();
        
        //System.out.println(instruction);
        
        LightInstruction parsed = new LightInstruction(instruction,x1,y1,x2,y2);
        
        return parsed;
    }
}
