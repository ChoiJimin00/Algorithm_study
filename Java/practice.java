package Homework;

import java.util.Scanner;

public class practice {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int star = in.nextInt();
		
		switch(star) {
		case 1:
			System.out.println("*"); break;			
		case 2:
			System.out.println("**"); break;	
		case 3:
			System.out.println("***"); break;	
		case 4:
			System.out.println("****"); break;			
		case 5:
			System.out.println("*****"); break;			
		case 6:
			System.out.println("******"); break;			
		case 7:
			System.out.println("*******"); break;	
		case 8:
			System.out.println("********"); break;	
		case 9:
			System.out.println("*********"); break;	
		case 10:
			System.out.println("**********"); break;	
			
		default:
			System.out.println("숫자를 잘못 입력하였습니다.");
			
		}

	}

}
