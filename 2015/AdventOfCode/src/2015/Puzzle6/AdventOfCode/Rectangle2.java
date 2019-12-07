import java.util.*;
/**
 * Write a description of Rectangle here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Rectangle2 {
    
    private int length;
    private int width;
    private HashMap<Pair,Integer> lights;//status, false off.
    
    public Rectangle2(int len, int wid){
        length = len;
        width = wid;
        lights = new HashMap<Pair,Integer>();//create new rectangle
        reset();//set all false.
    }
    
    private void reset(){
        for(int i = 0; i < length; i++){
            for(int j = 0; j < width; j++){
                lights.put(new Pair(i,j),0);
            }
        }
    }
    
    public void printStatus(){
        for(int i = 0; i < length; i++){
            for(int j = 0; j < width; j++){
                Pair temp = new Pair(i,j);
                //System.out.print(temp.getX() + "," + temp.getY() + " ");
                //Ternary statement print t if true and f if false.
                System.out.print(lights.get(temp));
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
        int temp = lights.get(pt);
        temp=temp+2;
        lights.put(pt,temp);//change status of bool
    }
    
    public void turnOn(Pair pt){
        int temp = lights.get(pt);
        temp++;
        lights.put(pt,temp);//change status to true
    }
    
    public void turnOff(Pair pt){
        int temp = lights.get(pt);
        if(temp > 0){
            temp--;
            lights.put(pt,temp);//change status to false
        }
    }
    
    public int getNumLit(){
        int count = 0;
        for(Pair p : lights.keySet()){
            count=count+lights.get(p);
        }
        return count;
    }
}
