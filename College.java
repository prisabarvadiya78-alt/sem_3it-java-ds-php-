// useful when a small helper class is needed only in one operation

class College
{
    void display()
    {
        class Student
        {
            void show()
            {
                System.out.println("student");
            }
        }

        Student s = new Student();
        s.show();
    }

    public static void main(String args[])
    {
        College c = new College();
        c.display();
    }
}