```java
import java.util.Scanner;

public class CreditScoreEligibility {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter annual income: ");
        double annualIncome = scanner.nextDouble();
        
        System.out.print("Enter credit score: ");
        int creditScore = scanner.nextInt();
        
        if (annualIncome >= 30000 && creditScore >= 700) {
            System.out.println("Congratulations! You are eligible for a high limit credit score.");
        } else if (annualIncome >= 20000 && creditScore >= 600) {
            System.out.println("You are eligible for a credit score with a moderate limit.");
        }
        
        scanner.close();
    }
}
```