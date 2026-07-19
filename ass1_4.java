import java.util.Scanner;
class ass1_4
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of a:");
        int a=sc.nextInt();
        System.out.println("Enter the value of b:");
        int b=sc.nextInt();
        System.out.println("Enter the value of c:"); // Corrected text
        int c=sc.nextInt();
        if(a<b)
        {
            if(a<c)
                System.out.println("Minimum is a :"+a);
            else
                System.out.println("Minimum is c :"+c);
        }
        else
        {
            if(b<c)
                System.out.println("Minimum is b :"+b);
            else
                System.out.println("Minimum is c :"+c);
        }
    }
}