class counter_demo 
{
    static int count = 0; // memory only once and retain its value

    counter_demo() 
	{
        count++;
        System.out.println(count);
    }

    public static void main(String args[])
	{
        counter_demo c1 = new counter_demo();
        counter_demo c2 = new counter_demo();
        counter_demo c3 = new counter_demo();
    }
}