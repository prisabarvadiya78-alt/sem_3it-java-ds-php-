// Example of static method

class calculate 
{
    static int cube(int x)

	{
        return x * x * x;
    }
}

class Static_method 
{
    public static void main(String args[]) 
	{
        int result = calculate.cube(5);
        System.out.println(result);
        result = calculate.cube(10);
        System.out.println(result);
    }
}