import java.util.Scanner;
class ass1_2
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Length:");
        int l=sc.nextInt();
        System.out.println("Enter the Width:");
        int w=sc.nextInt();
        System.out.println("Area of Rectangle is: "+ (l*w));
    }
}