//Java 8

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {

        int i, max = 0;

        for(i = 0; i < ar.length; i++)
        {
            if(ar[i]>max)
            {
                max = ar[i];
            }
        }

        int count_ar[] = new int [max];
        int sum  = 0;

        for(i = 0; i < ar.length; i++)
        {
            count_ar[ar[i]-1]++;
        }

        for(i = 0; i < max; i++)
        {
            if(count_ar[i] % 2 == 0)
            {
                sum += (int)(count_ar[i]/2);
            }

            if(count_ar[i] % 2 != 0)
            {
                sum += (int)((count_ar[i]-1)/2);
            }
        }
        return sum;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
