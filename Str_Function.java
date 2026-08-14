import java.lang.String;

class Str_Function 
{
    public static void main(String args[])
	{
        
        String str = "Rajkot";
        int i = str.length();
        System.out.println(i);

        System.out.println(str.concat("Gujarat"));

       
        char c = str.charAt(3);
        System.out.println(c);

       
        String str1 = "Atmiya";
        int ans = str1.compareTo("atmiya");
        System.out.println(ans); // returns 0 if true, otherwise non-zero value

        
        String st = "Atmiya";
        int ans1 = st.compareToIgnoreCase("atmiya");
        System.out.println(ans1);

     
        String s4 = "Atmiya";
        char c3[] = s4.toCharArray();
        System.out.println(c3);

       
        String s1, s2;
        s1 = "atmiya";
        s2 = s1.toUpperCase();
        System.out.println(s2);

        s2 = s1.toLowerCase();
        System.out.println(s2);

       
        s2 = s1.substring(3, 5); // "iy"
        System.out.println(s2);

       
        s1 = "atmiya";
        s2 = s1.replace('a', 'A');
        System.out.println(s2);

        
        int index = str.indexOf("a");
        System.out.println(index);

        int index1 = s1.indexOf("a", 2);
        System.out.println(index1);

       
        String str1_val = "Hello";
        String str2_val = "hello";
        System.out.println(str1_val.equals(str2_val));
        System.out.println(str1_val.equalsIgnoreCase(str2_val));

       
        String s = "Atmiya";
        System.out.println(s.startsWith("At"));
        System.out.println(s.endsWith("ya"));
    }
}