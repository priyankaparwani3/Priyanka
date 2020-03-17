


using System;



namespace Priyanka

{

    class Program

    {

        static void Main(string[] args)

        {

            Users user = new Users("Priyanka Parwani", 23);

            user.GetUserDetails();

            Console.WriteLine("Press Enter Key to Exit..");

            Console.ReadLine();

        }

    }

    public class Users

    {

        public string Name { get; set; }

        public int Age { get; set; }

        public Users(string name, int age)

        {

            Name = name;

            Age = age;

        }

        public void GetUserDetails()

        {

            Console.WriteLine("Name: {0}, Age: {1}", Name, Age);

        }

    }

}
