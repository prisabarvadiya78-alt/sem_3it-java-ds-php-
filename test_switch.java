class test_switch
{
   public static void main(String args[])
   {
     int x=Integer.parseInt(args[0]);
	 switch(x)
	 {
	 case 1:System.out.println("Monday");break;
	 case 2:System.out.println("Tuesday");break;
	 case 3:System.out.println("wednesday");break;
	 case 4:System.out.println("Thursday");break;
	 case 5:System.out.println("friday");break;
	 case 6:System.out.println("saturday");break;
	 case 7:System.out.println("sunday");break;
	default:System.out.println("Invalid number of day");
	}
	}
	}