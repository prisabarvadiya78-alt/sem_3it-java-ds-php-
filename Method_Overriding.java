// Example of Hierarchical inheritance with method overriding

class Bank
 {
    int getInterest() 
	{
        return 0;
    }
}

class SBI extends Bank 
{
    int getInterest() 
	{
        return 8;
    }
}

class ICICI extends Bank 
{
    int getInterest() 
	{
        return 7;
    }
}

class AXIS extends Bank 
{
    int getInterest()
	{
        return 9;
    }
}

class Method_Overriding 
{
    public static void main(String args[])
	{
        SBI s = new SBI();
        ICICI i = new ICICI();
        AXIS a = new AXIS();

        System.out.println("SBI Interest Rate: " + s.getInterest());
        System.out.println("ICICI Interest Rate: " + i.getInterest());
        System.out.println("AXIS Interest Rate: " + a.getInterest());
    }
}