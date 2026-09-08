class Test_throws_ex
{
    static int divideNum(int m, int n) throws ArithmeticException
    {
        int div = m / n;
        return div;
    }

    // main method
    public static void main(String args[])
    {
        try
        {
            System.out.println(divideNum(45, 0));
        }
        catch (ArithmeticException e)
        {
            System.out.println("Number cannot be divided by 0");
        }

        System.out.println("Rest of the code..");
    }
}