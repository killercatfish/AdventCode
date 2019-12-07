//Created a coordinate pair class.  
//http://stackoverflow.com/questions/4777622/creating-a-list-of-pairs-in-java

public class Pair {
    private int x;
    private int y;
    public Pair(int l, int r){
        this.x = l;
        this.y = r;
    }
    
    public int getX(){ 
        return x; 
    }
    
    public int getY(){ 
        return y; 
    }
    
    public void setX(int l){ 
        this.x = l; 
    }
    
    public void setY(int r){ 
        this.y = r; 
    }
    
    //Generic hashcode override.  Intended to give each point a unique hash code.
    //got this from: http://stackoverflow.com/questions/9135759/java-hashcode-for-a-point-class
    //This hash must be euqivalent to any point I deem equal.
    //Prime number is essential, but arbitrary,
    @Override
    public int hashCode() {
        int result = x;
        result = 31 * result + y;
        return result;
    }
    
    //This is how to determine if two pairs are equal
    @Override
    public boolean equals( Object obj )
    {
        boolean flag = false;
        Pair temp = ( Pair )obj;
        if( temp.x == x && temp.y == y){
            flag = true;
        }
        return flag;
    }
}