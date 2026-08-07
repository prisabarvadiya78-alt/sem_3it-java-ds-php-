// Example of upcasting

class Game 
{
    void type() 
	{
        System.out.println("Indoor & outdoor");
    }
}

class Cricket extends Game
 {
    void type() 
	{
        System.out.println("outdoor game");
    }
}

class upcasting
 {
    public static void main(String args[])
	{
        Game gm = new Game();
        Cricket ck = new Cricket();

        gm.type();
        ck.type();

        gm = ck; // gm refers to Cricket object
        gm.type(); // calls Cricket's type
    }
}