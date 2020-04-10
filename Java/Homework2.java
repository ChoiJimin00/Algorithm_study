//12191689_컴퓨터공학과_최지민
package week4;

import java.util.Scanner;

public class Homework2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("*을 이용하여 출력할 모양을 입력하세요.");
		System.out.println("1: 왼쪽으로 치우친 아래쪽이 큰 삼각형");
		System.out.println("2: 오른쪽으로 치우친 아래쪽이 큰 삼각형");
		System.out.println("3: 우싱단에서 좌하단 부분이 비어있는 정사각형");
		System.out.println("이외의 입력인 경우 종료");
		int number = sc.nextInt();
		
		while (1 <= number && number <= 3) {
			System.out.print("출력할 줄의 개수를 입력하세요 : ");
			int line = sc.nextInt();
			star(number,line);
			
			System.out.println("*을 이용하여 출력할 모양을 입력하세요.");
			System.out.println("1: 왼쪽으로 치우친 아래쪽이 큰 삼각형");
			System.out.println("2: 오른쪽으로 치우친 아래쪽이 큰 삼각형");
			System.out.println("3: 우싱단에서 좌하단 부분이 비어있는 정사각형");
			System.out.println("이외의 입력인 경우 종료");
			number = sc.nextInt();
		}
		System.out.print("프로그램이 종료되었습니다.");
	}

	public static void star(int n, int line) {
		switch (n) {
		case 1:
			for (int i = 0; i < line; i++) {
				for (int j = 0; j <= i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			System.out.println();
			break;

		case 2:
			for (int i = 0; i < line; i++) {
				for (int j = 0; j < line - i - 1; j++) { // print blank
					System.out.print(" ");
				}
				
				for (int j = 0; j <= i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			System.out.println();
			break;

		case 3:
			for (int i = 0; i < line; i++) { // left-up
				for (int j = 0; j < line - i - 1; j++) {
					System.out.print("*");
				}

				System.out.print(" ");

				for (int j = 0; j < i; j++) { // right-down
					System.out.print("*");
				}
				System.out.println();
			}
			System.out.println();
			break;
		default:
			System.out.println();
		}
	}
}