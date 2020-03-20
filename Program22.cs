using System;

public class Employee
{
    public string FirstName;
    public string LastName;

    public void PrintFullName()
    {
        Console.WriteLine(FirstName + " " + LastName);

    }
}

public class PartTimeEmployee : Employee
{
    public new void PrintFullName()
    {
        base.PrintFullName();

    }
}

public class FullTimeEmployee : Employee
{

}

public class Program
{
    public static void Main()
    {
        FullTimeEmployee FTE = new FullTimeEmployee();
        FTE.FirstName = "FullTime";
        FTE.LastName = "Employee";
        FTE.PrintFullName();

        PartTimeEmployee PTE = new PartTimeEmployee();
        PTE.FirstName = "PartTime";
        PTE.LastName = "Employee";
        PTE.PrintFullName();
    }
}

