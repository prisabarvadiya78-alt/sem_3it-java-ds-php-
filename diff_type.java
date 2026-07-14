class Calculation
{
    void sum(int a, int b)
    {
        System.out.println(a + b);
    }

    void sum(double a, double b)
    {
        System.out.println(a + b);
    }

    void sum(float a, float b)
    {
        System.out.println(a + b);
    }
}

class diff_type
{
    public static void main(String args[])
    {
        Calculation c = new Calculation();

        c.sum(10, 20);
        c.sum(35.5, 40.5);
        c.sum(20.4f, 60.5f);
    }
}