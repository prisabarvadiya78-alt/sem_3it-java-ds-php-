import java.util.Scanner;
class ass1_3
{
    public static void main(String args[])
    {
        int c;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of a:");
        int a=sc.nextInt();
        System.out.println("Enter the value of b:");
        int b=sc.nextInt();
        c=a;
        a=b;
        b=c;
        System.out.println("After swapping the value of a:"+ a);
        System.out.println("After swapping the value of b:"+ b);
    }
}