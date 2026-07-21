class Student
 {
    int rollno;
    String name;
    static String college = "VSC";

    Student(int r, String n)
	{
        rollno = r;
        name = n;
    }

    void display()
	{
        System.out.println(rollno + " " + name + " " + college);
    }

    public static void main(String args[]) {
        Student s1 = new Student(10, "xyz");
        Student s2 = new Student(20, "ABC");

        s1.display();
        s2.display();
    }
}