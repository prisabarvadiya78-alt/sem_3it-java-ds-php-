interface printable
{
    void print();
}

class Test_Interface implements printable
{
    public void print()
    {
        System.out.println("Hello");
    }
}

class IntDemo
{
    public static void main(String args[])
    {
        Test_Interface obj = new Test_Interface();
        obj.print();
    }
}






















