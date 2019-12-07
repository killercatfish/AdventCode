
/**
 * Write a description of LightInstruction here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class LightInstruction {
    
    private String instruction;
    private Pair start;
    private Pair end;
    
    public LightInstruction(String inst, int x1, int y1, int x2, int y2){
        instruction = inst;
        start = new Pair(x1,y1);
        end = new Pair(x2,y2);
    }
    
    public Pair getStart(){
        return start;
    }
    
    public Pair getEnd(){
        return end;
    }
    
    public String getInstruction(){
        return instruction;
    }
    
    public int getStartX(){
        return start.getX();
    }
    
    public int getStartY(){
        return start.getY();
    }
    
    public int getEndX(){
        return end.getX();
    }
    
    public int getEndY(){
        return end.getY();
    }
   
}
