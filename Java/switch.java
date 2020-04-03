package week3;

import java.util.Scanner;

public class Homework3 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		System.out.println("수행할 작업을 선택하세요. 1 : 구구단 출력, 2 : 두 정수 x,y에 대한 x를 y로 나눈 나머지 출력.");
		int num = in.nextInt();

		switch (num) {
		case 1:
			System.out.println("몇 단을 출력하실건가요 : ");
			int multi = in.nextInt();

			if (multi <= 1 || multi >= 10) {
				System.out.println("입력이 잘못 되었습니다.");
				break;
			}

			System.out.println(multi + " * " + 1 + " = " + multi * 1);
			System.out.println(multi + " * " + 2 + " = " + multi * 2);
			System.out.println(multi + " * " + 3 + " = " + multi * 3);
			System.out.println(multi + " * " + 4 + " = " + multi * 4);
			System.out.println(multi + " * " + 5 + " = " + multi * 5);
			System.out.println(multi + " * " + 6 + " = " + multi * 6);
			System.out.println(multi + " * " + 7 + " = " + multi * 7);
			System.out.println(multi + " * " + 8 + " = " + multi * 8);
			System.out.println(multi + " * " + 9 + " = " + multi * 9);
			break;

		case 2:
			System.out.println("x를 입력하세요 : ");
			int x = in.nextInt();
			System.out.println("y를 입력하세요 : ");
			int y = in.nextInt();
			System.out.println("x를 y로 나눈 나머지는 " + x % y + "입니다");
			break;

		default:
			System.out.println("입력이 잘못 되었습니다.");
		}
	}

}
