import java.util.Scanner;

class ass1_7
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int choice;
        
        do {
            // Display menu
            System.out.println("\n---- Menu ----");
            System.out.println("1. Factorial");
            System.out.println("2. Even or Odd");
            System.out.println("3. Exit");
            System.out.print("Enter your choice (1-3): ");
            choice = sc.nextInt();
            
            switch (choice) {
                case 1:
                    // Factorial
                    System.out.print("Enter a number to find factorial: ");
                    int num = sc.nextInt();
                    if (num < 0)
					{
                        System.out.println("Factorial not defined for negative numbers.");
                    } 
					else 
					{
                        long factorial = 1;
                        for (int i = 1; i <= num; i++) {
                            factorial *= i;
                    }
                        System.out.println("Factorial of " + num + " is " + factorial);
                    }
                    break;
                    
                case 2:
                    // Even or Odd
                    System.out.print("Enter a number to check Even or Odd: ");
                    int n = sc.nextInt();
                    if (n % 2 == 0) {
                        System.out.println(n + " is Even.");
                    } 
					else
					{
                        System.out.println(n + " is Odd.");
                    }
                    break;
                    
                case 3:
                    System.out.println("Exiting the program. thank you!");
                    break;
                    
                default:
                    System.out.println("Invalid choice! Please enter 1 to 3.");
            }
        }
		while (choice != 3);
        
     
    }
}