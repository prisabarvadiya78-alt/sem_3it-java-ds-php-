abstract class shape
{
  abstract void draw();
}
     class rectangle extends shape
	 {
           void draw()
       {
           System.out.println("drawing rectangle");
    }
       }
	 class circle extends shape
	 {
           void draw()
       {
           System.out.println("drawing circle");
    }
       }
	 class test_abstract
{
       public static void main(String args[])	
      {
         shape s;
         s=new circle();
         s.draw();
         s=new rectangle();
         s.draw();
      }
}		 