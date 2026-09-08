class Test_throw 
{
    // defining a method
    void checkNum(int num) 
    {
        if (num < 1) 
        {
            throw new ArithmeticException("Number is negative");
        } 
        else 
        {
            System.out.println("Number is positive");
        }
    }

    // main method
    public static void main(String args[]) 
    {
        Test_throw obj = new Test_throw();
        obj.checkNum(-1);
        System.out.println("Rest of the code...");
    }
}