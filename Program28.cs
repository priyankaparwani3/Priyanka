

using System;



namespace Priyanka

{

    struct User

    {

        public const string name = "Priyanka Parwani";

        public string location;

        public int age;

        public User(string a, int b)

        {

            location = a;

            age = b;

        }

    }

    class Program

    {

        static void Main(string[] args)

        {

            // Declare object with new keyword

            User u = new User("Mumbai", 23);

            // Declare object without new keyword

            User u1;

            Console.WriteLine("Name: {0}, Location: {1}, Age: {2}", User.name, u.location, u.age);

            // Initialize Fields

            u1.location = "Guntur";

            u1.age = 32;

            Console.WriteLine("Name: {0}, Location: {1}, Age: {2}", User.name, u1.location, u1.age);

            Console.WriteLine("\nPress Enter Key to Exit..");

            Console.ReadLine();

        }

    }

}
