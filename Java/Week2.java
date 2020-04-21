package week2;

import java.util.Scanner;

public class Week2 {
	public static void main(String[] args) {
		
		//1, Variable 영어, _, $로 시작
		int radius;
		int _int;
		int $a;
		/* 자료형 쓰는 이유 ? - 어떤 데이터를 저장할 지 미리 정의하기 위해
		 * 클래스, 인터페이스 첫 글자는 대문자 표기 안해도 정상작동 하기는 함
		 * 지역 변수는 사용 전에 반드시 초기화 해야 함 <-> 전역 변수는 초기화 안해도 기본 값 들어가 있음
		 */
		
		//char ch = ''; // 오류 발생
		char ch = ' ';
		String s1 = ""; // 오류 발생 X
		String s2 = "A"+"B";
		System.out.println(s2 + 7);  // string클래스는 다른 자료형과 더해도 string으로 잡는다(문자 취급한다) 
		// System은 class
		
		
		//출력 결과 확인
		int x = 2; int y = 5; char c = 'A'; //'A'의 문자코드는 65 
		System.out.println(1 + x << 33);  // bit(shift) 연산  ( << x를 왼쪽으로 33만큼 이동)
		System.out.println(y >= 5 || x < 0 && x > 2); 
		System.out.println(y += 10 - x++); 
		System.out.println(x+=2); 
		System.out.println( !('A' <= c && c <='Z') ); 
		System.out.println('C'-c);  // 2
		System.out.println('5'-'0');  // 5
		System.out.println(c+1);  // 66
		System.out.println(++c);  //B
		System.out.println(c++);  // B
		System.out.println(c);  //C
		
		//2, Type conversion
		/* 자동 타입 변환 -> 메모리가 더 큰 자료형으로 자동 변환
		 * 강제 타입 변환 -> 더 작은 메모리 공간에 넣기 위해 (데이터 손실 가능성 있음)
		 */
		int i; double d; byte b;
		
		i = 7 / 4;
		System.out.println(i);
		d = 7 / 4;
		System.out.println(d);
		d = 7 / (double)4; // type conversion
		System.out.println(d);
		
		String hello = "Hello"; final double PI = 3.14;
		System.out.println(hello);
		System.out.printf("hellp = %s and PI = %5.2f\n", hello, PI); // 포맷을 지정해서 출력한다
		System.out.print(hello);
		
		//3, Input
		
		Scanner in = new Scanner(System.in); // Scanner 객체 생성
		int w = in.nextInt();
		int h = in.nextInt();
		System.out.printf("%d*%d은 %d입니다. \n",w,h,w*h);

		/*Scanner 클래스가 제공하는 데이터 입력 메서드
		 * 
		 * next() --> String
		 * nextInt() --> int
		 * nextFloat() --> float
		 * nextLine() --> String
		*/

	}
}
