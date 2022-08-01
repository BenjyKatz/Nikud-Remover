import java.io.*;
import java.util.Scanner;

public class NRJ{
    public static void main(String[] args){
        try{
            Scanner sc = new Scanner(new File("Milon/test.csv"));
            System.out.println("hey!");
           // sc.useDelimiter(",");
            while(sc.hasNext()){
                System.out.println("in while!");
                System.out.println(sc.next());
            }
            sc.close();
        }
        catch(Exception e){
            System.out.println("no file");
        }
    }
    

}