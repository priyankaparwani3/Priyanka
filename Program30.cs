

using System;



namespace Tutlane

{

    interface IUser

    {

        void GetDetails(string x);

    }

    class User : IUser

    {

        public void GetDetails(string a)

        {

            Console.WriteLine("Name: {0}", a);

        }

    }

    class User1 : IUser

    {

        public void GetDetails(string a)

        {

            Console.WriteLine("Location: {0}", a);

        }

    }

    class Program

    {

        static void Main(string[] args)

        {

            IUser u = new User();

            u.GetDetails("Priyanka Parwani");

            IUser u1 = new User1();

            u1.GetDetails("Mumbai");

            Console.WriteLine("\nPress Enter Key to Exit..");

            Console.ReadLine();

        }

    }

}

