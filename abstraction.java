abstract class bike
{
  bike()
  {
    System.out.println("bike is created");
  }
  abstract void run();
  void changegear()
  {
   System.out.println("gear changed");
  
  }
}
class honda extends bike
{
  void run()
  {
    System.out.println("running safely...");
   }
} 
class abstraction
{
    public static void main(String args[])
 {
          bike obj=new honda();
          obj.run();
          obj.changegear();

  }
} 
  