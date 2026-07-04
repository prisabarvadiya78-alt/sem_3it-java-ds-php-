class twod_array
{
   public static void main(String args[])
   {
     int a[][]={
		 {99,44,78,89},
		 {76,78,98,90},
		 {12,13,15,65},
		 {34,54,67,87}
		 };
	 for(int i=0;i<a.length;i++)
	 {
	   for(int j=0;j<a[i].length;j++)
	   {
	   System.out.print(a[i][j]+"\t");
	   }
	     System.out.println();
	 } 
  }
}
