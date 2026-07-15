class Fruits
 {
    String fruite_nm;

    Fruits(String f_nm)
	{
        fruite_nm = f_nm;
    }
}

class para_Construct
{
    public static void main(String args[]) 
	{
      
        Fruits f1 = new Fruits("Mango");
        System.out.println("Fruits name: " + f1.fruite_nm);
    }
}