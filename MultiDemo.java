// Example of Multilevel Inheritance

class X
 {
    public void methodX() 
	{
        System.out.println("Class X method");
    }
}

class Y extends X
 {
    public void methodY()
	{
        System.out.println("Class Y method");
    }
}

class Z extends Y 
{
    public void methodZ()
	{
        System.out.println("Class Z method");
    }
}

class MultiDemo
 {
    public static void main(String args[])
	{
        Z obj = new Z();
        obj.methodX();
        obj.methodY();
        obj.methodZ();
    }
}