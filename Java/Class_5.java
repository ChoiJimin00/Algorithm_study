package week5;

// 여러개의 생성자 , this()

public class Class_5 {

	public static void main(String[] args) {
		Circle5 circle_1 = new Circle5(50.0, "빨강");
		Circle5 circle_2 = new Circle5(25.0);
		Circle5 circle_3 = new Circle5("주황");
		Circle5 circle_4 = new Circle5();
		
		circle_1.print();
		circle_2.print();
		circle_3.print();
		circle_4 .print();
	}

}

class Circle5{
	double radius;
	String color;
	
	public Circle5(double r, String c) { 
		radius = r; color = c;
	}
	public Circle5(double r) { 
		this(r, "하늘");
	}
	public Circle5(String c) { 
		this(10.0, c);
	}
	public Circle5() { 
		this(10.0, "노랑");
	}
	
	void print() {
		System.out.println("radius: "+ radius + " color: " + color);
	}
}