//12191689_컴퓨터공학과_최지민
package week5;

public class Homework {

	public static void main(String[] args) {
		Square s1 = new Square("빨강",5);
		Square s2 = new Square("주황");
		Square s3 = new Square(3);
		Square s4 = new Square();
		
		s1.printSquare();
		s2.printSquare();
		s3.printSquare();
		s4.printSquare();
	}
}

class Square {
	private String color;
	private int Area;
	
	Square(String c, int a){ color = c; Area = a;}
	Square(String c){ color = c; Area = 1;}
	Square(int a){ color = "하얀"; Area = a;}
	Square(){ color = "하얀"; Area = 1;}
	
	void printSquare() {
		System.out.println("이 정사각형은 넓이가 "+Area+"인 "+color+"색 입니다.");
	}
}