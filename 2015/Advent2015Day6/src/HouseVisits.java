
/**
 * Write a description of HouseVisits here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

import java.util.*;
import java.util.Scanner;
import java.io.*;
import java.io.FileNotFoundException;

public class HouseVisits {
    private static HashMap<String,Integer> houses;//house object
    
    public HouseVisits(){
        houses = new HashMap<String,Integer>();//Key is an ordered pair mapped with number visits
        int[] location = {0,0};//current location/ordered pair
        String currentKey = null;
        currentKey = updateKey(currentKey, location);
        houses.put(currentKey,1);//count the beginning location!  This will be (0,0)
    }
    
    public static void calcHouses(String directions){
        
        
        int[] location = {0,0};//current location/ordered pair
        String currentKey = null;
        currentKey = updateKey(currentKey, location);
        
        for (int i = 0; i < directions.length(); i++){
            char c = directions.charAt(i);        
            //increment or decrement the location of santa
            if(c == '^'){
                location[1]++;
            }
            else if(c == 'v'){
                location[1]--;
            }
            else if(c == '<'){
                location[0]--;
            }
            else if(c == '>'){
                location[0]++;
            }
            
            currentKey = updateKey(currentKey,location);
            
            //System.out.println("location: (" + location[0] + "," + location[1] + ")");
            
            if(houses.containsKey(currentKey)){//
                //System.out.println("Has Key!");
                int temp = houses.get(currentKey);
                //System.out.println(temp);
                temp++;
                houses.put(currentKey,temp);
                //System.out.println(currentKey);
            }
            else if(!houses.containsKey(currentKey)){
                //System.out.println("Doesn't Have Key!");
                houses.put(currentKey,1);
                //System.out.println(currentKey);
            }
        }


    }
    
    private static String updateKey(String current, int[] location){
        String newKey = location[0] + "," + location[1];
        return newKey;
    }
    
    public static void printHouses(){
        
        for(String location : houses.keySet()){
            System.out.println("location: (" + location +  ") has " + houses.get(location) + " visits.");
        }
        
    }
    
    public static int getSize(){
        return houses.size();
    }
    
    public static void splitHouses(String directions){
        StringBuilder santa = new StringBuilder();
        StringBuilder robot = new StringBuilder();
        
        for(int i = 0; i < directions.length(); i++){
            if(i % 2 == 0){
                santa.append(directions.charAt(i));
            }
            else if(i % 2 != 0){
                robot.append(directions.charAt(i));
            }
        }
        //System.out.println("santa: " + santa);
        //System.out.println("robot: " + robot);
        calcHouses(santa.toString());
        calcHouses(robot.toString());
        
    }
    
}
