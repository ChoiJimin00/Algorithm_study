package week5;

class Phone {
	String model;
	int value;
	
	void print() {
		System.out.println(value + "만원 짜리 "+ model + " 스마트폰");
	}
}

public class Class_1 {
	public static void main(String[] args) {
		Phone myPhone = new Phone();
		myPhone.print();  //필드는 기본 값이 있음
		
		myPhone.model = "Galaxy S8";
		myPhone.value = 100;
		myPhone.print();
		
		Phone yourPhone = new Phone();
		yourPhone.model = "G6";
		yourPhone.value = 80;
		yourPhone.print();
		
		myPhone = yourPhone;
		myPhone.print();
		

	}

}
