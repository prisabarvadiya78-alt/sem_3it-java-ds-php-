interface a
{
    void draw();
}

interface b extends a
{
    void show();
}

class xyz implements b
{
    public void draw()
    {
        System.out.println("drawing circle");
    }

    public void show()
    {
        System.out.println("show method");
    }
}

class interface_demo
{
    public static void main(String args[])
    {
        xyz obj = new xyz();
        obj.draw();
        obj.show();
    }
}