import java.util.*;

public class testRectangle {
    public void testRectangle(){
        System.out.println('\f');
        Rectangle yard = new Rectangle(1000,1000);
        
        LightParser input = new LightParser();
        
        String fname = "/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle6/Puzzle6Input.txt";
        
        ArrayList<LightInstruction> li = input.parseInstructions(fname);
        
        for(LightInstruction l : li){
            switch(l.getInstruction()){
                case "toggle":
                    yard.toggleRect(l.getStart(),l.getEnd());
                    break;
                case "turn off":
                    yard.turnOffRect(l.getStart(),l.getEnd());
                    break;
                case "turn on":
                    yard.turnOnRect(l.getStart(),l.getEnd());
                    break;
                default:
                    break;
            }
            
        }
        
        yard.printStatus();
        
        int numLit = yard.getNumLit();
        
        System.out.println("Number of lights on: " + numLit);
    }
    
    private void printLIArray(ArrayList<LightInstruction> l){
        for(LightInstruction li : l){
            System.out.println(li.getInstruction() + " (" + li.getStartX() + "," + li.getStartY() + ") (" + li.getEndX() + "," + li.getEndY() + ")");
        }
    }
    
    public void testRectangle2(){
        System.out.println('\f');

        Rectangle2 yard = new Rectangle2(1000,1000);
        
        LightParser input = new LightParser();
        
        String fname = "/Users/KCF/Dropbox/[Josh]/[ComputerScience]/AdventOfCode/Puzzle6/Puzzle6Input.txt";
        
        ArrayList<LightInstruction> li = input.parseInstructions(fname);
        
        for(LightInstruction l : li){
            switch(l.getInstruction()){
                case "toggle":
                    yard.toggleRect(l.getStart(),l.getEnd());
                    break;
                case "turn off":
                    yard.turnOffRect(l.getStart(),l.getEnd());
                    break;
                case "turn on":
                    yard.turnOnRect(l.getStart(),l.getEnd());
                    break;
                default:
                    break;
            }
            
        }
        int numLit = yard.getNumLit();
        
        System.out.println("Number of lights on: " + numLit);
    }
    
}
