
BaseClass bc = new BaseClass();
DerivedClass dc = new DerivedClass();
BaseClass bcdc = new DerivedClass();

bc.Method1();
bc.Method2();
dc.Method1();
dc.Method2();
bcdc.Method1();
bcdc.Method2();

class BaseClass
{
	public virtual void Method1()
	{
		Console.WriteLine("Base - Method 1");
	}

	public void Method2()
	{
		Console.WriteLine("Base - Method 2");
	}

}

class DerivedClass: BaseClass
{

	public override void Method1()
	{
		Console.WriteLine("Derived - Method 1");
	}
	public new void Method2() 
	{
		Console.WriteLine("Derived - Method 2 ");
	}
}

