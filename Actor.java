class Actor
 {
    String lastname;
    String firstname;

    Actor(String lastname, String firstname)
	{
        this.lastname = lastname;
        this.firstname = firstname;
    }

    public static void main(String args[])
	{
        Actor a = new Actor("Devgn", "Ajay");
        System.out.println("Name of Actor: " + a.firstname + " " + a.lastname);
    }
}