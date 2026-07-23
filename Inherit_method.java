class A
{
    public void methodA()
    {
        System.out.println("Base class method");
    }
}
class B extends A
{
    public void methodB()
    {
        System.out.println("Child class method");
    }
}
class Inherit_method
{
    public static void main(String args[])
    {
        B obj = new B();
        obj.methodA(); // calling superclass
        obj.methodB(); // calling local method
    }
}