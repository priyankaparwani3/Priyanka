﻿

using System;



namespace Tutlane

{

    public class Calculate

    {

        public void AddNumbers(int a, int b)

        {

            Console.WriteLine("a + b = {0}", a + b);

        }

        public void AddNumbers(int a, int b, int c)

        {

            Console.WriteLine("a + b + c = {0}", a + b + c);

        }

    }

    class Program

    {

        static void Main(string[] args)

        {

            Calculate c = new Calculate();

            c.AddNumbers(1, 2);

            c.AddNumbers(1, 2, 3);

            Console.WriteLine("\nPress Enter Key to Exit..");

            Console.ReadLine();

        }

    }

}
