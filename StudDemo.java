class person {
    String fname, lname;

    person(String fname, String lname) {
        this.fname = fname;
        this.lname = lname;
    }
}

class student extends person 
{
    int rollno;
    String stream;
    int sem;

    student(String fname, String lname, int rollno, String stream, int sem) {
        super(fname, lname);
        this.rollno = rollno;
        this.stream = stream;
        this.sem = sem;
    }

    void display() {
        System.out.println("Name: " + fname + " " + lname);
        System.out.println("Rollno: " + rollno);
        System.out.println("Division: " + stream + " Sem " + sem);
    }
}

class StudDemo {
    public static void main(String[] args)
	{
        student s1 = new student("Gopi", "Rangani", 30, "M.B.B.S.", 2);
        s1.display();
    }
}