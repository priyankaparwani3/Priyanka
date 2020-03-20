using System;

    class Customer
    {
    string _firstName;
    string _lastName;

    public Customer() : this("No FirstName provided", "No LastName provided")
    {
    }

    public Customer(string FirstName, string LastName)
    {
        this._firstName = FirstName;
        this._lastName = LastName;

    }
    public void PrintFullName()
    {
        Console.WriteLine("Full name = {0}", this._firstName + " " + this._lastName);

    }
    ~Customer()
    {

    }
       class Program
    {
        public static void Main()
        {
            Customer C1 = new Customer();
            C1.PrintFullName();
            Customer C2 = new Customer("P", "T");
            C2.PrintFullName();
        }
    }
    }

