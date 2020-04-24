package week6;

public class StringDemo {

	public static void main(String[] args) {
		//1. == 와 != 연산자는 두 문자열이 동일한 객체인지 검사
		String s1 = "Hi, Java!";
		String s2 = "Hi, Java!";
		String s3 = new String("Hi, Java!");
		String s4 = new String("Hi, Java!");
		
		System.out.println("s1 == s2 -> "+ (s1 == s2));  // true
		System.out.println("s1 == s3 -> "+ (s1 == s3));  // false
		System.out.println("s3 == s4 -> "+ (s3 == s4));  // false
		s1 = s3;
		System.out.println("s1 == s3 -> "+ (s1 == s3));  // true
		System.out.println();
		
		//2. String Compare Method ( equals, compareTo)
		String s5 = "Hi, Java!";
		String s6 = new String("Hi, Java!");
		String s7 = "Hi, Code!";
		String s8 = "Hi, java!";
		
		System.out.println(s5.equals(s6));  // true
		System.out.println(s5.equals(s7));  // false
		System.out.println(s5.equals(s8));  // false
		System.out.println(s5.equalsIgnoreCase(s8));  // true (대소문자 무시)
		
		System.out.println(s5.compareTo(s7));  // 7 ('J' - 'C')
		System.out.println(s5.compareToIgnoreCase(s8));  // 0 (String 같음)
		System.out.println(s5.compareTo(s8));  // -39 ('J' - 'j')
		System.out.println("Hi, Java!".compareToIgnoreCase("hi, java!"));  // 0 (대소문자 무시)
		
		//3. 문자열 조작
		String s9 = new String("Hi,");
		String s10 = new String(" Java");
		String s11,s12;
		
		System.out.println("문자열 길이(s9) : "+s9.length());
		char c = s9.charAt(1); // i (1번째 인덱스 반환)
		System.out.println(c);
		
		s9 = s9.concat(s10);   //Hi, Java (주어진 문자열을 현재 문자열 뒤에 붙임)
		s11 = s9.toLowerCase();   //hi, java (전부 소문자로 반환)
		s12 = s9.substring(4,8); // Java (4~(8-1)인덱스에 해당하는 문자열)
		
		System.out.println(s9);
		System.out.println(s11);
		System.out.println(s12);
		
	}

}
