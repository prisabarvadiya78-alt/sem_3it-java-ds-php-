class bank 
{
    double p, r;
    int n;
    void setdata(double pa, double ra, int ny) {
        p = pa;
        r = ra;
        n = ny;
}
    double simpleinterest()
	{
        return(p*r*n/100);
    }
}

class bank_para
{
    public static void main(String[] args)
	{
        bank b1 = new bank();
        bank b2 = new bank();

        b1.setdata(5000, 12, 5);
        b2.setdata(10000, 12, 5);

        double si = b1.simpleinterest();

        System.out.println("simple interest 1 is: " + si);
        System.out.println("simple interest 2 is: " + b2.simpleinterest());
    }
}