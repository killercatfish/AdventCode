import java.lang.*;

import org.apache.commons.codec.digest.DigestUtils;//access md5 hash.  Installed this library
//https://commons.apache.org/proper/commons-codec/download_codec.cgi

/**
 * Write a description of Hash here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Hash {
    public static void hash(){
        String str = "bgvyzdsv";//initial input
        String tempStr = null;//str + testAnswer
        
        DigestUtils digest = new DigestUtils();
        
        String encrypted = null;//encrypted input
        
        //add an incrementing integer.  start at 1.  concat to str.
        int testAnswer = 0;// increment this to see what the answer is
        
        do{
            testAnswer++;
            tempStr = str.concat(String.valueOf(testAnswer));
            //System.out.println(tempStr);
            encrypted = digest.md5Hex(tempStr);//get hash of current encrypted
            //System.out.println(encrypted);
        }while(!check(encrypted));
        System.out.println(encrypted + " " + testAnswer);
    }
    
    private static boolean check(String encrypted){
        System.out.println('\f');
        if(encrypted.substring(0,6).equals("000000")){
            //System.out.println(encrypted.substring(0,5));
            return true;
        }
        return false;
    }
}
