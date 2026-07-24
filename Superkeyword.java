class A {
    int a = 10;
}

class B extends A 
{
    int a = 20;

    public void display()
	{
        System.out.println("Value : " + a);
        System.out.println("Value : " + super.a);
    }
}

class Superkeyword 
{
    public static void main(String args[])
	{
        B obj = new B();
        obj.display(); // prints value of local a variable
    }
}