class car 
{
    int modelYear;
    String modelName;

    
    car()
	{
        System.out.println("my car name is Audi");
    }

    car(int year, String name)
	{
        modelYear = year;
        modelName = name;
    }
}

class overload_Construct
 {
    public static void main(String args[]) 
	{
       
        car c1 = new car();
        car c2 = new car(2024, "Audi A4");
        
        System.out.println("model year: " 
		+ c2.modelYear + " and model name: " + c2.modelName);
    }
}