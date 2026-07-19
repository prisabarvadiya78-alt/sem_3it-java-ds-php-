class ass1_9
{
    public static void main(String args[])
    {
        int[] numbers = new int[5];
        for (int i = 0; i < 5; i++)
        {
            numbers[i] = Integer.parseInt(args[i]);
        }
        System.out.println("The numbers you entered are:");
        for (int num : numbers)
		{
            System.out.println(num);
        }
    }
}