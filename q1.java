import java.util.Scanner;
public class q1 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
      /*  int N = sc.nextInt();
       Set<String> Seen = new HashSet<>(); 
       int prevtime = -1;
       for(int i = 0; i < N; i++){
        String sender = sc.next();
        String receiver = sc.next();
        int timestrap = sc.nextInt();
        int amount = sc.nextInt();
        String key = sender + " " + receiver + " " + amount;
        if(Seen.contains(key)){
            System.out.println("Error: Duplicate transaction detected for " + key);
            return;
        }
        Seen.add(key);
        if(prevtime != -1 && timestrap < prevtime){
            System.out.println("Error: Transactions are not in chronological order.");
            return;
        }
        prevtime = timestrap;
       }
         System.out.println("All transactions are valid.");
         */
/*         String word = sc.next();
         if(word.equals(word.toUpperCase())){
            System.out.println("true");
         }
         else if(word.equals(word.toLowerCase())){
            System.out.println("true");
         }
         else if(Character.isUpperCase(word.charAt(0)) && word.substring(1).equals(word.substring(1).toLowerCase())){
            System.out.println("true");
         }
         else{
            System.out.println("false");
         
        } */

            /* 
       int n = sc.nextInt();
       String[] arr = new String[n];for(int i = 0; i< n; i++){
        arr[i] = sc.next();
       }
       int count = 0;
       for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(arr[i].charAt(i) < arr[j - 1].charAt(i)){
                count++;
            }
         }
       } System.out.println(count);
        */

       /* 
    String arr = sc.next();
    int count = 0;
    int result= 0;
    for(char ch : arr.toCharArray()){
        if (ch == '1'){
            count++;
        }
        else{
           result += count * (count + 1) / 2;
            count = 0;
        }
    }
    result += count * (count + 1) / 2;
    System.out.println(result);

*/
/* 
int n = sc.nextInt();
int[] arr = new int[n];
for(int i = 0; i < n; i++){             
    arr[i] = sc.nextInt();
}
int count = 0;
for (int i = 0; i < n; i++){
    if(arr[i] != 0){
        arr[count++] = arr[i];
    }
}
for(int i = count; i < n; i++){
    arr[i] = 0;
}
System.err.println(Arrays.toString(arr));
*/

/*
int n = sc.nextInt();
q1 solution = new q1();
System.out.println(solution.bulbswitch(n));
    }
public int bulbswitch(int n){
    return (int) Math.sqrt(n);
    */
   int n  = sc.nextInt();
   if(n <= 2){
    int charges = n * 100;
    System.out.println(charges);
   }
   else if(n <= 3){
    int charges = n * 150;
    System.out.println(charges);
   }
   else if(n <= 5){
    int charges = n * 200;
    System.out.println(charges);
   }
   else{
    System.out.println("error");
   }
}
    }

   