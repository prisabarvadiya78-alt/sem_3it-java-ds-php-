import java.util.Scanner;
class ass1_5
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name:");
        String name=sc.nextLine();
        System.out.println("Enter Roll number:");
        int rollno=sc.nextInt();

        int[] marks = new int[5];
        int totalMarks = 0;

        System.out.println("Enter marks for 5 subjects:");
        for (int i = 0; i < 5; i++)
		{
            System.out.print("Subject " + (i + 1) + ": ");
            marks[i] = sc.nextInt();
            totalMarks += marks[i];
        }

        double percentage = totalMarks / 5.0;
        String result;
        if (percentage >= 70)
		{
            result = "Distinction";
        } 
		else if (percentage >= 60)
		{
            result = "First Class";
        }
		else if (percentage >= 50)
		{
            result = "Second Class";
        } 
		else if (percentage >= 40) 
		{
            result = "Pass Class";
        } 
		else 
		{
            result = "Fail";
        }

        System.out.println("\n--- Student Result ---");
        System.out.println("Roll Number: " + rollno);
        System.out.println("Name: " + name);
        System.out.println("Total Marks: " + totalMarks + "/500");
        System.out.printf("Percentage: %.2f%%\n", percentage);
        System.out.println("Result: " + result);
    }
}