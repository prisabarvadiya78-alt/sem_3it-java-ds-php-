class Car
{
    private String model = "kia";

    class Engine
    {
        void show()
        {
            System.out.println(model);
        }
    }

    public static void main(String args[])
    {
        Car c = new Car();
        Car.Engine e = c.new Engine();
        e.show();
    }
}