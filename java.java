import java.util.Scanner;
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0; i < T; i++) {
            int N = sc.nextInt();
            int Q = sc.nextInt();
            ArrayList<Integer> prices = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                prices.add(sc.nextInt());
            }
            for (int j = 0; j < Q; j++) {
                String query = sc.next();
                int a = sc.nextInt();
                int b = sc.nextInt();
                if (query.equals("P")) {
                    System.out.println(sum(prices, a, b));
                } else if (query.equals("A")) {
                    prices.set(a-1, b);
                }
            }
        }
    }

    public static int sum(ArrayList<Integer> list, int a, int b) {
        int sum = 0;
        for (int i = a-1; i < b; i++) {
            sum += list.get(i);
        }
        return sum;
    }
}