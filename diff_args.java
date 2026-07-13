class calculation
{
    void sum(int a, int b) {
        System.out.println(a + b);
}

    void sum(int a, int b, int c) 
	{
        System.out.println(a + b + c);
    }
}

class diff_args 
{
    public static void main(String args[]) 
	{
        calculation c = new calculation();
        c.sum(20, 20);
        c.sum(10, 10, 10);
}
}