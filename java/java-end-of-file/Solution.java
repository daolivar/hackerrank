import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = 1;
        while (scan.hasNext()) {
            System.out.println(num + " " + scan.nextLine());
            num++;
        }
        scan.close();
    }
}
