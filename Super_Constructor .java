class Fruite
 {
    Fruite()
	{
        System.out.println("I am super class constructor fruite");
    }
}

class Mango extends Fruite
 {
    Mango()
	{
        super();
        System.out.println("I am a sub class mango");
    }
}

class Super_Constructor 
{
    public static void main(String[] args)
	{
        Mango m = new Mango();
    }
}