using System;

public class Customer
{
    public int ID { get; set; }
    public string Name
    {
        get; set;
    }
}
public class Program
{
    public static void Main()
    {
        int i = 10;
        int j = i;
        j = j + 1;

        Console.WriteLine("i = {0} && j = {1}", i, j);
            Customer C1 = new Customer();
            C1.ID = 101;
            C1.Name = "Mark";

        Customer C2 = C1;
        C2.Name = "Mary";
        Console.WriteLine("C1.Name = {0} && C2.Name = {1}", C1.Name, C2.Name);

        }
    }
