using System;

    public class BaseClass
    {
        public virtual void Print()
        {
            Console.WriteLine("i am a baseclass print method");
        }
    }
public class DerivedClass : BaseClass
{
    public override void Print()
    {
        Console.WriteLine("i am a baseclass print method");

    }
}
public class Program
{
    public static void Main()
    {
        BaseClass B = new DerivedClass();
        B.Print();
    }

}


