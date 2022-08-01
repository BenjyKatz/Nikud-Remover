import java.io.*;
import java.util.Scanner;

public class NR{
    public static void main(String[] args){
        Scanner sc = new Scanner("Milon/Rambam.csv");
        sc.useDelimiter(",");
        while(sc.hasNext()){
            System.out.println(sc.next());
        }
        sc.close();
    }
    

}