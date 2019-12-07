import java.util.*;
/**
 * Write a description of Rectangle here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Rectangle {
    
    private int length;
    private int width;
    private HashMap<Pair,Boolean> lights;//status, false off.
    
    public Rectangle(int len, int wid){
        length = len;
        width = wid;
        lights = new HashMap<Pair,Boolean>();//create new rectangle
        reset();//set all false.
    }
    
    private void reset(){
        for(int i = 0; i < length; i++){
            for(int j = 0; j < width; j++){
                lights.put(new Pair(i,j),false);
            }
        }
    }
    
    public void printStatus(){
        for(int i = 0; i < length; i++){
            for(int j = 0; j < width; j++){
                Pair temp = new Pair(i,j);
                //System.out.print(temp.getX() + "," + temp.getY() + " ");
                //Ternary statement print t if true and f if false.
                System.out.print(lights.get(temp) ? "T " : "F ");
            }
            System.out.println("");
        }
    }
    
    public void toggleRect(Pair srt, Pair nd){
        for(int i = srt.getY(); i <= nd.getY(); i++){
            for(int j = srt.getX(); j <= nd.getX(); j++){
                toggle(new Pair(i,j));
            }
        }
    }
    
    public void turnOffRect(Pair srt, Pair nd){
        for(int i = srt.getY(); i <= nd.getY(); i++){
            for(int j = srt.getX(); j <= nd.getX(); j++){
                turnOff(new Pair(i,j));
            }
        }
    }
    
    public void turnOnRect(Pair srt, Pair nd){
        for(int i = srt.getY(); i <= nd.getY(); i++){
            for(int j = srt.getX(); j <= nd.getX(); j++){
                turnOn(new Pair(i,j));
            }
        }
    }
    
    public void toggle(Pair pt){
        lights.put(pt,!lights.get(pt));//change status of bool
    }
    
    public void turnOn(Pair pt){
        lights.put(pt,true);//change status to true
    }
    
    public void turnOff(Pair pt){
        lights.put(pt,false);//change status to false
    }
    
    public int getNumLit(){
        int count = 0;
        for(Pair p : lights.keySet()){
            count = lights.get(p) ? count+1 : count;
        }
        return count;
    }
}
