package week3;

import java.util.Scanner;

public class operator {

	public static void main(String[] args) {
		
		//1.arithmetic operator
		byte a = 3, b = 4;
		//byte c = a + b; // int에서 byte로 형 변환  x
		byte c = (byte) (a+b); // 강제 형변환
		System.out.println(c);
		
		
		//2.logical operator
		int x = 0, y = 1;
		System.out.println((x<1)||(y--<1)); //앞의 연산의 true이므로 뒤에 연산 계산 X
		System.out.println("(x,y) = " + x + ", " + y);
		System.out.println((x<1)&&(y--<1));
		System.out.println("(x,y) = " + x + ", " + y);
		System.out.println((x<1)&&(y--<1));
		System.out.println("(x,y) = " + x + ", " + y);
		
		x = 0;  y = 1;
		System.out.println(x<1| y--<1); // | bit연산자 (or)
		System.out.println("(x,y) = " + x + ", " + y);
		
		// 연습문제
		int num = 0; char ch = ' '; String st="";
		Scanner sc = new Scanner(System.in);
		num = sc.nextInt();
		ch = sc.next().charAt(0); // char 입력 받는 방법 
		st = sc.next(); 
		
		System.out.println(num+" "+ch+" "+st);
		
		//삼항 연산자 사용
		int score = sc.nextInt();
		char grade = ' ';
		
		grade = (score>=90)?'A':(score>=80)?'B':(score>=70)?'C':(score>=60)?'D':'F';
		System.out.println("당신의 학점은 "+grade+"입니다.");
		
		
		
	}

}
