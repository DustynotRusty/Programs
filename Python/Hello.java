class X
{
	int a;
	void read(int m)
	{
		a=m;
	}
	void print()
	{
		System.out.println("a: "+ a);
	}
}
class Y
{
	void print()
	{
		System.out.println("Heyyy");
	}

}
class Hello
{
	public static void main(String[] args) 
	{
		X x1= new X();
		x1.read(5);
		x1.print(); 
		Y x2 = new Y();
		x2.print();

	}
}