public class Finally_block
{
    public static void main(String args[])
    {
        try
        {
            System.out.println("inside the try block");
            int data = 25 / 0;
            System.out.println(data);
        }
        catch (ArithmeticException e) // (NullPointerException cut karke ArithmeticException likha hai)
        {
            System.out.println(e);
        }
        finally
        {
            System.out.println("finally block is always executed");
        }

        System.out.println("rest of the code...");
    }
}